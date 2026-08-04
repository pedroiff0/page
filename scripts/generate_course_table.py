#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador Automático de Tabelas (Base de Dados) e Carrossel de Aulas para Cursos no Quartz.
Desenvolvido para o ecossistema institucional do IFF Campus Bom Jesus do Itabapoana.
Professor Responsável: Prof. Dr. Pedro Henrique Rocha de Andrade

Funcionamento:
1. Varre o diretório do curso (ex: content/pt-br/resource/latex ou content/templates/ModeloCurso).
2. Identifica todos os arquivos que começam com 'aula-*.md'.
3. Lê os metadados YAML (title, modulo, normas) e o primeiro título H1 (# ...).
4. Verifica na biblioteca de assets (/assets/biblioteca/<slug-do-curso>/) se existem:
   - slides-latex/aula-XX.pdf
   - slides-pptx/aula-XX.pdf
   - thumbs/aula-XX.png
5. Atualiza automaticamente no 'index.md' do curso os blocos:
   - <!-- COURSE_CAROUSEL_START --> ... <!-- COURSE_CAROUSEL_END -->
   - <!-- COURSE_TABLE_START --> ... <!-- COURSE_TABLE_END -->

Uso:
  python3 scripts/generate_course_table.py --dir content/pt-br/resource/latex --slug latex-escrita
  python3 scripts/generate_course_table.py --all
"""

import os
import re
import sys
import glob
import argparse

# Configuração canônica de nomes de Módulos (por índice de módulo 1..5 para 20 aulas)
MODULOS_TITULOS = {
    1: "📘 Módulo I — Epistemologia, Metodologia Científica e Elementos Pré-Textuais (Aulas 01 a 04)",
    2: "📘 Módulo II — Estrutura Textual, Introdução, PRISMA e Metodologia (Aulas 05 a 08)",
    3: "📘 Módulo III — Resultados, Discussão, Citações NBR 10520 e Referências NBR 6023 (Aulas 09 a 12)",
    4: "📗 Módulo IV — Arquitetura LaTeX (.tex), Motores, Sintaxe, Tabelas e Gráficos (Aulas 13 a 16)",
    5: "📗 Módulo V — Engenharia ReLaTeX (.cls e .sty), Metadados, Macros e Automação (Aulas 17 a 20)",
}

def parse_lesson_file(file_path):
    """Lê metadados (título, número da aula, normas) de um arquivo de aula markdown."""
    filename = os.path.basename(file_path)
    match = re.match(r"^aula-(\d+)-(.*?)\.md$", filename)
    if not match:
        return None
    
    num_aula = int(match.group(1))
    slug_aula = match.group(2)
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Extrair título do frontmatter YAML (title: ...)
    title = None
    yaml_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if yaml_match:
        yaml_block = yaml_match.group(1)
        title_match = re.search(r"^title:\s*[\"']?(.*?)[\"']?\s*$", yaml_block, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
            
    # Se não houver no YAML, buscar no primeiro H1
    if not title:
        h1_match = re.search(r"^#\s+(.*?)$", content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
            
    if not title:
        title = f"Aula {num_aula:02d}: {slug_aula.replace('-', ' ').title()}"

    # Limpar prefixo "Aula XX: " se já estiver no title para evitar duplicação na tabela
    clean_title = re.sub(r"^Aula\s*\d+:\s*", "", title, flags=re.IGNORECASE).strip()

    # Tentar extrair norma (ex: ABNT NBR ..., PRISMA, etc.) ou definir como '-'
    normas = "—"
    normas_match = re.findall(r"(ABNT NBR \d+[:\d]*|IBGE 1993|PRISMA \d*|CEP\s*/\s*CONEP)", content)
    if normas_match:
        # Pegar as normas exclusivas encontradas
        normas_uniq = sorted(list(set([n.strip() for n in normas_match])))
        normas = " / ".join(normas_uniq[:2]) # limitar a no máximo 2 na coluna da tabela

    return {
        "num": num_aula,
        "filename": filename,
        "basename": filename.replace(".md", ""),
        "title": title,
        "clean_title": clean_title,
        "normas": normas
    }

def check_asset_exists(root_repo, asset_rel_path):
    """Verifica se um asset existe no sistema de arquivos do site."""
    full_path = os.path.join(root_repo, "content", asset_rel_path.lstrip("/"))
    return os.path.exists(full_path)

def generate_carousel(lessons, course_slug, rel_base_url):
    """Gera marcação HTML+CSS de carrossel contínuo na horizontal com blur nas capas que dissipa no hover."""
    lines = []
    lines.append("<style>")
    lines.append(".course-carousel-wrapper {")
    lines.append("  display: flex;")
    lines.append("  overflow-x: auto;")
    lines.append("  scroll-snap-type: x mandatory;")
    lines.append("  gap: 1.5rem;")
    lines.append("  padding: 1.5rem 0.5rem;")
    lines.append("  scrollbar-width: thin;")
    lines.append("  scrollbar-color: var(--secondary, #0077b6) transparent;")
    lines.append("  -webkit-overflow-scrolling: touch;")
    lines.append("}")
    lines.append(".course-carousel-card {")
    lines.append("  flex: 0 0 280px;")
    lines.append("  scroll-snap-align: start;")
    lines.append("  border: 1px solid var(--lightgray, #e2e8f0);")
    lines.append("  border-radius: 14px;")
    lines.append("  overflow: hidden;")
    lines.append("  background: var(--light, #ffffff);")
    lines.append("  box-shadow: 0 4px 15px rgba(0,0,0,0.06);")
    lines.append("  transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1);")
    lines.append("  display: flex;")
    lines.append("  flex-direction: column;")
    lines.append("  text-decoration: none;")
    lines.append("  position: relative;")
    lines.append("}")
    lines.append(".course-carousel-card:hover {")
    lines.append("  transform: translateY(-6px);")
    lines.append("  box-shadow: 0 14px 28px rgba(0,0,0,0.14);")
    lines.append("  border-color: var(--secondary, #0077b6);")
    lines.append("}")
    lines.append(".course-carousel-thumb-box {")
    lines.append("  position: relative;")
    lines.append("  width: 100%;")
    lines.append("  height: 160px;")
    lines.append("  overflow: hidden;")
    lines.append("  background: #1e293b;")
    lines.append("}")
    lines.append(".course-carousel-thumb {")
    lines.append("  width: 100%;")
    lines.append("  height: 100%;")
    lines.append("  object-fit: cover;")
    lines.append("  filter: blur(3.5px) brightness(0.85);")
    lines.append("  transform: scale(1.08);")
    lines.append("  transition: filter 0.4s ease, transform 0.4s ease, brightness 0.4s ease;")
    lines.append("}")
    lines.append(".course-carousel-card:hover .course-carousel-thumb {")
    lines.append("  filter: blur(0px) brightness(1);")
    lines.append("  transform: scale(1.0);")
    lines.append("}")
    lines.append(".course-carousel-badge {")
    lines.append("  position: absolute;")
    lines.append("  top: 12px;")
    lines.append("  left: 12px;")
    lines.append("  background: rgba(0, 0, 0, 0.75);")
    lines.append("  color: #fff;")
    lines.append("  padding: 4px 10px;")
    lines.append("  border-radius: 20px;")
    lines.append("  font-size: 0.75rem;")
    lines.append("  font-weight: 700;")
    lines.append("  backdrop-filter: blur(4px);")
    lines.append("  border: 1px solid rgba(255,255,255,0.2);")
    lines.append("  z-index: 2;")
    lines.append("}")
    lines.append(".course-carousel-body {")
    lines.append("  padding: 1.25rem;")
    lines.append("  display: flex;")
    lines.append("  flex-direction: column;")
    lines.append("  justify-content: space-between;")
    lines.append("  flex-grow: 1;")
    lines.append("}")
    lines.append(".course-carousel-title {")
    lines.append("  font-size: 0.98rem;")
    lines.append("  font-weight: 700;")
    lines.append("  margin-bottom: 0.5rem;")
    lines.append("  color: var(--dark, #0f172a);")
    lines.append("  line-height: 1.35;")
    lines.append("}")
    lines.append(".course-carousel-desc {")
    lines.append("  font-size: 0.82rem;")
    lines.append("  color: var(--gray, #64748b);")
    lines.append("  line-height: 1.45;")
    lines.append("  margin: 0;")
    lines.append("}")
    lines.append("</style>")
    lines.append("")
    lines.append('<div class="course-carousel-wrapper">')
    for l in sorted(lessons, key=lambda x: x["num"]):
        num_str = f"{l['num']:02d}"
        title = l['clean_title']
        thumb_rel = f"/assets/biblioteca/{course_slug}/thumbs/aula-{num_str}.png"
        note_link = f"{rel_base_url}/{l['basename']}"
        desc = l.get('normas', 'Referencial teórico, normas técnicas e prática ReLaTeX.')
        lines.append(f'  <a href="{note_link}" class="course-carousel-card">')
        lines.append(f'    <div class="course-carousel-thumb-box">')
        lines.append(f'      <span class="course-carousel-badge">AULA {num_str}</span>')
        lines.append(f'      <img src="{thumb_rel}" alt="Capa Aula {num_str}" class="course-carousel-thumb" />')
        lines.append(f'    </div>')
        lines.append(f'    <div class="course-carousel-body">')
        lines.append(f'      <div class="course-carousel-title">{title}</div>')
        lines.append(f'      <p class="course-carousel-desc">Normas em Foco: {desc}</p>')
        lines.append(f'    </div>')
        lines.append(f'  </a>')
    lines.append('</div>')
    return "\n".join(lines)


def generate_modules_table(lessons, course_slug, rel_base_url, root_repo):
    """Gera as tabelas de Ementa Analítica divididas por módulo 100% em português."""
    lines = []
    
    # Agrupar aulas em Módulos de 4 em 4 aulas (1..4 = Módulo 1, 5..8 = Módulo 2, etc.)
    modulos = {}
    for l in sorted(lessons, key=lambda x: x["num"]):
        mod_idx = ((l["num"] - 1) // 4) + 1
        if mod_idx not in modulos:
            modulos[mod_idx] = []
        modulos[mod_idx].append(l)
        
    for mod_idx in sorted(modulos.keys()):
        mod_name = MODULOS_TITULOS.get(mod_idx, f"📘 Módulo {mod_idx} — Conteúdo Programático")
        lines.append(f"### {mod_name}\n")
        lines.append("| Aula | Título da Lição & Conteúdo | Normas (ABNT / IBGE) | Material Didático |")
        lines.append("| :---: | :--- | :---: | :--- |")
        
        for l in modulos[mod_idx]:
            num_str = f"{l['num']:02d}"
            note_link = f"[Notas de Aula]({rel_base_url}/{l['basename']})"
            
            # Checar slides LaTeX PDF
            s_latex_rel = f"/assets/biblioteca/{course_slug}/slides-latex/aula-{num_str}.pdf"
            if check_asset_exists(root_repo, s_latex_rel):
                s_latex_link = f"[Slides LaTeX (.pdf)]({s_latex_rel})"
            else:
                s_latex_link = f"*[Slides LaTeX em desenvolvimento]*"
                
            # Checar slides PPTX PDF
            s_pptx_rel = f"/assets/biblioteca/{course_slug}/slides-pptx/aula-{num_str}.pdf"
            if check_asset_exists(root_repo, s_pptx_rel):
                s_pptx_link = f"[Slides PPTX (.pdf)]({s_pptx_rel})"
            else:
                s_pptx_link = f"*[Slides PPTX em desenvolvimento]*"
                
            mat_col = f"{note_link}<br>{s_latex_link}<br>{s_pptx_link}"
            
            row = f"| **{num_str}** | **{l['clean_title']}**<br>Fundamentação teórica, normas técnicas e prática ReLaTeX. | **{l['normas']}** | {mat_col} |"
            lines.append(row)
            
        lines.append("\n---\n")
        
    return "\n".join(lines)

def update_course_index(course_dir, course_slug, root_repo):
    """Atualiza o index.md de um curso específico com a base de dados de aulas."""
    index_file = os.path.join(course_dir, "index.md")
    if not os.path.exists(index_file):
        print(f"[{course_dir}] AVISO: index.md não encontrado. Ignorando.")
        return False
        
    # Identificar rel_base_url a partir da pasta content com barra inicial absoluta para o Quartz
    rel_path_from_content = os.path.relpath(course_dir, os.path.join(root_repo, "content"))
    rel_base_url = "/" + rel_path_from_content.lstrip("/")
    
    # Encontrar todos os arquivos aula-*.md
    lesson_files = glob.glob(os.path.join(course_dir, "aula-*.md"))
    if not lesson_files:
        print(f"[{course_dir}] AVISO: Nenhum arquivo aula-*.md encontrado.")
        return False
        
    lessons = []
    for f in lesson_files:
        data = parse_lesson_file(f)
        if data:
            lessons.append(data)
            
    print(f"[{course_dir}] Encontradas {len(lessons)} aulas para o curso '{course_slug}'.")
    
    # Gerar carrossel e tabela de módulos
    carousel_md = generate_carousel(lessons, course_slug, rel_base_url)
    table_md = generate_modules_table(lessons, course_slug, rel_base_url, root_repo)
    
    # Substituir no index.md entre os marcadores
    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Se não existirem marcadores no index.md, vamos inseri-los ou avisar
    if "<!-- COURSE_CAROUSEL_START -->" not in content:
        print(f"[{course_dir}] Marcadores do carrossel não encontrados, inserindo em volta do carrossel existente...")
        # Substitui a tag <div class="grid cards" markdown> ... </div> pelo bloco marcado
        pattern_cards = r"(<div class=\"grid cards\" markdown>.*?</div>)"
        if re.search(pattern_cards, content, re.DOTALL):
            content = re.sub(
                pattern_cards,
                "<!-- COURSE_CAROUSEL_START -->\n\\1\n<!-- COURSE_CAROUSEL_END -->",
                content,
                count=1,
                flags=re.DOTALL
            )
            
    if "<!-- COURSE_TABLE_START -->" not in content:
        print(f"[{course_dir}] Marcadores de tabela não encontrados, inserindo em volta da ementa...")
        pattern_ementa = r"(### 📘 Módulo I.*?)(?=\n## |\Z)"
        if re.search(pattern_ementa, content, re.DOTALL):
            content = re.sub(
                pattern_ementa,
                "<!-- COURSE_TABLE_START -->\n\\1\n<!-- COURSE_TABLE_END -->\n",
                content,
                count=1,
                flags=re.DOTALL
            )
            
    # Substituir conteúdo do carrossel
    content = re.sub(
        r"<!-- COURSE_CAROUSEL_START -->.*?<!-- COURSE_CAROUSEL_END -->",
        f"<!-- COURSE_CAROUSEL_START -->\n{carousel_md}\n<!-- COURSE_CAROUSEL_END -->",
        content,
        flags=re.DOTALL
    )
    
    # Substituir conteúdo da tabela
    content = re.sub(
        r"<!-- COURSE_TABLE_START -->.*?<!-- COURSE_TABLE_END -->",
        f"<!-- COURSE_TABLE_START -->\n{table_md}\n<!-- COURSE_TABLE_END -->",
        content,
        flags=re.DOTALL
    )
    
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"[{course_dir}] SUCESSO! index.md atualizado automaticamente com {len(lessons)} aulas na tabela e carrossel.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Gerador Automático de Tabelas de Aulas do Quartz")
    parser.add_argument("--dir", help="Caminho para a pasta do curso (ex: content/pt-br/resource/latex)")
    parser.add_argument("--slug", default="latex-escrita", help="Slug da biblioteca em /assets/biblioteca/")
    parser.add_argument("--all", action="store_true", help="Atualiza todos os cursos configurados no repositório")
    args = parser.parse_args()
    
    root_repo = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    if args.all:
        cursos = [
            ("content/pt-br/resource/latex", "latex-escrita"),
            ("content/templates/ModeloCurso", "modelo-curso"),
        ]
        for cdir, cslug in cursos:
            full_cdir = os.path.join(root_repo, cdir)
            if os.path.exists(full_cdir):
                update_course_index(full_cdir, cslug, root_repo)
    elif args.dir:
        full_cdir = os.path.join(root_repo, args.dir)
        update_course_index(full_cdir, args.slug, root_repo)
    else:
        # Padrão: atualiza o curso principal
        update_course_index(os.path.join(root_repo, "content/pt-br/resource/latex"), "latex-escrita", root_repo)

if __name__ == "__main__":
    main()
