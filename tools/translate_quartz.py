#!/usr/bin/env python3
"""
Tradutor automatizado do Quartz-site usando LibreTranslate (self-hosted).

Blindagem total do markup:
  * prefixo de bloco (##, >, -, emoji inicial) NUNCA passa pelo LT.
  * wikilinks (![[...]]/[[...]]) e nomes proprios (Soja, Ana Cecilia...)
    sao stasheados inteiros como placeholder e DEVOLVIDOS LITERAIS —
    o LT nem os ve, entao nao pode corromper (ex.: "[ [ [" ou "Soja"->"Soya").
  * bold/italico vao como HTML (<strong>/<em>) com format=html do LT.

Uso:
  python3 tools/translate_quartz.py --check
  python3 tools/translate_quartz.py --dry-run          # preview (default)
  python3 tools/translate_quartz.py --apply            # GRAVA
  python3 tools/translate_quartz.py --lang en,es,fr --section media
"""
import argparse
import re
import sys
import time
import urllib.parse
import urllib.request
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
SRC = "pt-br"
TARGETS = ["en", "es", "fr"]
SECTIONS = ["media", "research"]

# Disclaimer de tradução automática, anexado ao fim de cada página traduzida.
# Cita o mecanismo implementado e fica no idioma da própria página.
DISCLAIMER = {
    "en": (
        "> [!abstract] Automatic translation notice\n"
        "> This page was automatically translated from Portuguese using the "
        "LibreTranslate-based automated translator implemented in "
        "`tools/translate_quartz.py` (it preserves wikilinks, embeds and proper "
        "names via positional splitting). Machine translation may contain "
        "inaccuracies — the original Portuguese version is the authoritative source.\n"
    ),
    "es": (
        "> [!abstract] Aviso de traducción automática\n"
        "> Esta página fue traducida automáticamente del portugués utilizando el "
        "traductor automático basado en LibreTranslate implementado en "
        "`tools/translate_quartz.py` (que preserva wikilinks, embeds y nombres "
        "propios mediante división posicional). Es traducción automática y puede "
        "contener imprecisiones — la versión original en portugués es la fuente "
        "autoritativa.\n"
    ),
    "fr": (
        "> [!abstract] Avis de traduction automatique\n"
        "> Cette page a été traduite automatiquement du portugais à l'aide du "
        "traducteur automatique basé sur LibreTranslate implémenté dans "
        "`tools/translate_quartz.py` (qui préserve les wikilinks, les embeds et "
        "les noms propres par découpage positionnel). Il s'agit d'une traduction "
        "automatique pouvant contenir des inexactitudes — la version portugaise "
        "originale fait foi.\n"
    ),
}

LT_URL = "http://localhost:5000/translate"

EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF"
    "\U00002190-\U000021FF\U00002B00-\U00002BFF\U0000FE00-\U0000FE0F"
    "\U00002700-\U000027BF\u200d\u20e3]"
)
BOLD_RE = re.compile(r"\*\*(?<!\*)\*([^*]+)\*\*")
ITAL_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
# wikilink: ![[...]] ou [[...]]; o primeiro [ e obrigatorio (sem \s* que
# soltaria o ! dos embeds). Toleramos espacos entre os colchetes internos.
WIKI_RE = re.compile(r"!?\[\s*\[\s*[^\]]*\]\s*\]\s*")
# nomes proprios que NUNCA devem ser traduzidos (sobrenomes, etc.)
PROPER_NAMES = [
    "Ana Cecília Soja", "Ana Cecilia Soja", "Cecília Soja", "Soja",
    "Maria Luiza Linhares Dantas", "Linhares Dantas", "Dantas",
    "Maycon Jorge Deláqua da Silva", "Maycon Jorge Deláqua", "Deláqua",
    "Arthur Miquelito Lopes", "Miquelito Lopes", "Miquelito",
    "Claudia Linhares Sales", "Linhares Sales",
]
PROPER_RE = re.compile("|".join(re.escape(n) for n in PROPER_NAMES))
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")  # qualquer [texto](url)
EMOJI_CLASS = (
    r"[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF"
    r"\U00002190-\U000021FF\U00002B00-\U00002BFF\U0000FE00-\U0000FE0F"
    r"\U00002700-\U000027BF\u200d\u20e3]"
)
# prefixo de bloco no INICIO da linha: markup (##, >, -, etc.) OPCIONAL
# seguido de emojis adjacentes — tudo isso NAO vai pro LT.
PREFIX_RE = re.compile(
    r"^(?:#{1,6}\s+|>\s*|[-*]\s+|\d+\.\s+|!\s*)?" + EMOJI_CLASS + r"*"
)
# linha de tabela markdown: comeca e termina com | (ignora espacos)
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
TABLE_SEP_RE = re.compile(r"^\s*\|[\s:\-|]+\|\s*$")  # linha separadora | :--- | :--- |
CALLOUT_RE = re.compile(r"^(>\s*\[!.*?\]\s*)(.*)$")


def lt_translate(text: str, target: str, fmt="text", src="pt") -> str:
    if not text.strip():
        return text
    data = urllib.parse.urlencode({
        "q": text, "source": src, "target": target, "format": fmt,
    }).encode()
    req = urllib.request.Request(LT_URL, data=data, headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    })
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())["translatedText"]
        except Exception:  # noqa
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))
    return text


def protect(text: str):
    """Converte bold/italic para HTML (que o LT preserva em format=html).
    Wikilinks e nomes proprios NAO passam por aqui — sao removidos via
    split posicional em translate_spans (nunca vao pro LT)."""
    store = {}

    def stash(tok):
        key = f"§{len(store)}§"
        store[key] = tok
        return key

    # bold/italic -> HTML (LT com format=html preserva as tags)
    text = BOLD_RE.sub(lambda m: f"<strong>{m.group(1)}</strong>", text)
    text = ITAL_RE.sub(lambda m: f"<em>{m.group(1)}</em>", text)
    usa_html = ("<strong>" in text) or ("<em>" in text) or ("<br" in text)
    return text, store, usa_html


def restore(text: str, store: dict) -> str:
    # HTML -> markdown (tolerante a espacos/quebras que o LT possa inserir)
    text = re.sub(r"<\s*strong\s*>", "**", text)
    text = re.sub(r"<\s*/\s*strong\s*>", "**", text)
    text = re.sub(r"<\s*em\s*>", "*", text)
    text = re.sub(r"<\s*/\s*em\s*>", "*", text)
    text = re.sub(r"<\s*br\s*/?\s*>", "<br>", text)  # normaliza <br/> -> <br>
    return text


# trechos que NUNCA vao pro LT: wikilinks inteiros + nomes proprios
PROT_RE = re.compile(WIKI_RE.pattern + r"|" + PROPER_RE.pattern)


def translate_spans(text: str, target: str) -> str:
    """Traduz o texto, mantendo wikilinks e nomes proprios LITERAIS
    (split posicional) e protegendo bold/italic via HTML."""
    if not text.strip():
        return text
    parts, last = [], 0
    for mm in PROT_RE.finditer(text):
        before = text[last:mm.start()]
        if before:
            parts.append(_translate_bold(before, target))
            # garante espaco apos trecho traduzido se o nome comeca com letra
            if parts[-1] and not parts[-1][-1].isspace() and mm.group(0)[0].isalpha():
                parts.append(" ")
        parts.append(mm.group(0))  # literal
        last = mm.end()
    if last < len(text):
        after = text[last:]
        if after:
            parts.append(_translate_bold(after, target))
    return "".join(parts)


def _translate_bold(text: str, target: str) -> str:
    if not text.strip():
        return text
    prot, store, html = protect(text)
    fmt = "html" if html else "text"
    out = lt_translate(prot, target, fmt=fmt)
    return restore(out, store)

def translate_with_links(text: str, target: str) -> str:
    """Traduz o texto, preservando URLs de links Markdown inteiras
    (so a ancora e traduzida; o url nunca vai pro LT). Aplica fallback de
    link local nao-traduzido para o idioma de fallback (en) + aviso."""
    parts, last = [], 0
    for mm in LINK_RE.finditer(text):
        if mm.start() > last:
            parts.append(translate_spans(text[last:mm.start()], target))
        anchor, url = mm.group(1), mm.group(2)
        anchor_tr = translate_spans(anchor, target)
        new_url, fallback = local_link(url, target)
        if fallback:
            anchor_tr = anchor_tr.rstrip() + " " + FALLBACK_TAG[target]
        parts.append(f"[{anchor_tr}]({new_url})")
        last = mm.end()
    if last < len(text):
        parts.append(translate_spans(text[last:], target))
    return "".join(parts)


def translate_text_preserving_wiki(text: str, target: str) -> str:
    """Traduz o texto, mantendo wikilinks literais (split posicional)."""
    if not WIKI_RE.search(text):
        return translate_with_links(text, target)
    parts, last = [], 0
    for mm in WIKI_RE.finditer(text):
        if mm.start() > last:
            parts.append(translate_with_links(text[last:mm.start()], target))
        # wikilink: ![[slug]] / [[slug]] / ![[slug|texto]] / [[slug|texto]
        raw = mm.group(0)
        has_bang = raw.startswith("!")
        # conteudo entre os colchetes: tira "!" + "[[" do inicio e "]]" do fim
        body = raw[3:-2] if has_bang else raw[2:-2]
        if "|" in body:
            wslug, wtext = body.split("|", 1)
        else:
            wslug, wtext = body, ""
        new_slug, fallback = local_link(wslug, target)
        if fallback:
            wtext = (wtext + " " if wtext and not wtext.endswith(" ") else wtext)
            wtext += FALLBACK_TAG[target]
        opener = "![[" if has_bang else "[["
        parts.append(f"{opener}{new_slug}|{wtext}]]" if wtext else f"{opener}{new_slug}]]")
        last = mm.end()
    if last < len(text):
        parts.append(translate_with_links(text[last:], target))
    return "".join(parts)


# ---------- sanitize de espacamento e fallback de links locais ----------

LOCAL_PREFIXES = ("pt-br/", "en/", "es/", "fr/")
FALLBACK_TAG = {
    "en": "(in English)",
    "es": "(en español)",
    "fr": "(en français)",
}
FALLBACK_LANG = "en"  # idioma de fallback quando a pagina alvo nao existe


def _slug_exists(lang: str, slug: str) -> bool:
    """Verifica se content/<lang>/<slug>.md ou <slug>/index.md existe."""
    base = CONTENT / lang / slug
    return (base.with_suffix(".md")).exists() or (base / "index.md").exists()


def local_link(url: str, target: str):
    """Recebe um slug local (ex: pt-br/foo/bar). O idioma desejado e o
    idioma da pagina atual (target). Se a pagina existe em target, usa
    target; senao cai no fallback (en) e sinaliza; se nem no fallback,
    mantem o url original (nao quebra o link)."""
    if not url.startswith(LOCAL_PREFIXES):
        return url, False
    lang, slug = url.split("/", 1)
    if _slug_exists(target, slug):
        return f"{target}/{slug}", False
    if _slug_exists(FALLBACK_LANG, slug):
        return f"{FALLBACK_LANG}/{slug}", True
    return url, False


def sanitize(line: str) -> str:
    """Corrige espacamentos que o MT gruda:
    - qualquer nao-espaco colado em '['  -> ' ['
    - ')' colado em letra (sem '*')       -> ') '
    - " l ' etat " (apostrofo FR espacado) -> l'etat
    """
    # espaco antes de '[' so se o char anterior for letra ou ')' (nao quebra
    # wikilinks '[[...' nem embeds '![...')
    line = re.sub(r"(?<=[A-Za-zÀ-ÿ])\[", r" [", line)
    line = re.sub(r"(?<=[\])])\[", r" [", line)
    # ')' seguido de letra (sem espaco e sem '*') ganha espaco
    line = re.sub(r"\)(?=[A-Za-zÀ-ÿ])(?!\*)", r") ", line)
    # apostrofo frances colado: ' x ' -> x'
    line = re.sub(r"(?<=[A-Za-zÀ-ÿ]) ' (?=[A-Za-zÀ-ÿ])", "'", line)
    return line


def translate_line(line: str, target: str) -> str:
    if not line.strip():
        return line
    # tabela markdown: traduz CELULA A CELULA preservando os delimitadores |
    if TABLE_ROW_RE.match(line):
        if TABLE_SEP_RE.match(line):
            return line  # linha separadora | :--- | :--- | -> intacta
        cells = [c for c in line.strip().strip("|").split("|")]
        translated = [translate_text_preserving_wiki(c, target) for c in cells]
        return sanitize("| " + " | ".join(translated) + " |")
    # callout "> [!note] Texto" -> traduz so o Texto
    mc = CALLOUT_RE.match(line)
    if mc:
        label, rest = mc.group(1), mc.group(2)
        return label + (translate_text_preserving_wiki(rest, target) if rest.strip() else rest)
    # separa prefixo de bloco (##, >, -, emoji) do texto
    m = PREFIX_RE.match(line)
    if m and m.end() < len(line):
        prefix, rest = line[:m.end()], line[m.end():]
        translated = translate_text_preserving_wiki(rest, target)
        # limpa artifacts que o LT as vezes injeta no inicio (ex.: "- ", "# ")
        translated = re.sub(r"^[\-\*\#]\s+", "", translated)
        # garante 1 espaco apos prefixo (emoji + texto)
        if not prefix.endswith(" "):
            prefix += " "
        return sanitize(prefix + translated)
    if m and m.end() == len(line):
        return line  # linha so de markup/emoji
    return sanitize(translate_text_preserving_wiki(line, target))


def translate_body(body: str, target: str) -> str:
    out = "\n".join(translate_line(l, target) for l in body.split("\n"))
    # disclaimer de traducao automatica no fim da pagina (no idioma alvo)
    disc = DISCLAIMER.get(target, "")
    if disc:
        out = out.rstrip() + "\n\n" + disc.rstrip() + "\n"
    return out


def split_frontmatter(md: str):
    if md.startswith("---"):
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", md, re.S)
        if m:
            return m.group(1), m.group(2)
    return "", md


def get_frontmatter_field(fm: str, key: str):
    m = re.search(rf"(?m)^{key}:\s*(.*)$", fm)
    return m.group(1).strip() if m else None


def set_frontmatter_field(fm: str, key: str, value: str):
    # coloca entre aspas para garantir YAML valido (titulos com ':' ou '#')
    safe = value.replace('"', '\\"')
    new = f'{key}: "{safe}"'
    if re.search(rf"(?m)^{key}:", fm):
        return re.sub(rf"(?m)^{key}:.*$", new, fm, count=1)
    return fm + f"\n{new}\n"


def list_target_files(section: str):
    files = []
    base = CONTENT / SRC / section
    if not base.exists():
        return files
    for p in sorted(base.rglob("*.md")):
        # ignora o proprio index de secao? NAO — traduzimos os index.md tambem.
        # (o slug do Quartz resolve index.md e <dir>.md para o mesmo path,
        #  logo em main() pulamos index.md que conflite com irmão .md existente)
        files.append(p.relative_to(CONTENT / SRC))
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--lang", default=",".join(TARGETS))
    ap.add_argument("--section", default=",".join(SECTIONS))
    ap.add_argument("--overwrite", action="store_true",
                    help="regrava arquivos de destino que ja existem "
                         "(sem isto, destinos existentes sao preservados)")
    args = ap.parse_args()

    if args.check:
        try:
            print("LT OK ->", lt_translate("Olá mundo de teste!", "en"))
        except Exception as e:  # noqa
            print("LT FALHOU:", e); sys.exit(1)
        return

    targets = [t for t in args.lang.split(",") if t in TARGETS]
    sections = [s for s in args.section.split(",") if s in SECTIONS]
    if not args.apply:
        print("[DRY-RUN] nenhum arquivo gravado. Use --apply para gravar.\n")

    total = 0
    for section in sections:
        files = list_target_files(section)
        print(f"== secao '{section}': {len(files)} arquivos ==")
        for rel in files:
            total += 1
            md = (CONTENT / SRC / rel).read_text(encoding="utf-8")
            fm, body = split_frontmatter(md)
            for lang in targets:
                out_path = CONTENT / lang / rel
                if out_path.exists():
                    if not args.overwrite:
                        print(f"  pulado {lang}/{rel} (ja existe; use --overwrite)")
                        continue
                    # overwrite ligado: sobrescreve, EXCETO manuais en/.md planos
                    # (anomaly-detection.md, dark-matter-shocks.md,
                    #  satellite-trail-removal.md) que sao trabalho manual
                    if lang == "en" and out_path.name != "index.md":
                        print(f"  pulado {lang}/{rel} (manual en preservado)")
                        continue
                # index.md conflita com irmão <dir>.md ja existente (mesmo slug)
                if out_path.name == "index.md":
                    sibling = out_path.parent.with_suffix(".md")
                    if sibling.exists():
                        print(f"  pulado {lang}/{rel} (conflito de slug com {sibling.name})")
                        continue
                if args.apply:
                    translated = translate_body(body, lang)
                    # traduz metadados exibidos (title/description) por idioma,
                    # mantendo slug/URL intacto (so a exibicao muda)
                    out_fm = fm
                    if lang != SRC:
                        for field in ("title", "description"):
                            val = get_frontmatter_field(fm, field)
                            if val:
                                tr = translate_line(val, lang).strip()
                                out_fm = set_frontmatter_field(out_fm, field, tr)
                    out_path.parent.mkdir(parents=True, exist_ok=True)
                    out_path.write_text(f"---\n{out_fm}\n---\n{translated}", encoding="utf-8")
                    print(f"  gravado {lang}/{rel}")
                else:
                    sample = "\n".join(l for l in body.splitlines() if l.strip())[:240]
                    prev = translate_text_preserving_wiki(sample, lang) if sample.strip() else ""
                    print(f"  [{lang}] {rel}\n    {prev[:140]}")
        print()
    if args.apply:
        print(f"PRONTO: {total} arquivos x {len(targets)} idiomas gravados.")


if __name__ == "__main__":
    main()
