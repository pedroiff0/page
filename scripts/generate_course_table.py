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

# Configuração canônica de nomes de Módulos (por índice de módulo 1..6)
MODULOS_TITULOS = {
    1: "📘 Módulo I — Epistemologia, Metodologia e Elementos Pré-Textuais",
    2: "📘 Módulo II — Estrutura Textual e Construção Argumentativa",
    3: "📘 Módulo III — Resultados, Discussão e Elementos Pós-Textuais",
    4: "📗 Módulo IV — Fundamentos de LaTeX e Arquitetura de Documentos",
    5: "📗 Módulo V — Domínio da Classe ifftese.cls e Ecossistema ReLaTeX",
    6: "📗 Módulo VI — Defesa, Apresentação Científica, Pôsteres e Relatórios",
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
    """Gera o bloco markdown do carrossel ilustrado com thumbs autênticas."""
    lines = ['<div class="grid cards" markdown>\n']
    
    for l in sorted(lessons, key=lambda x: x["num"]):
        num_str = f"{l['num']:02d}"
        thumb_url = f"/assets/biblioteca/{course_slug}/thumbs/aula-{num_str}.png"
        link_url = f"{rel_base_url}/{l['basename']}"
        
        # O card do carrossel
        lines.append(f'- <img src="{thumb_url}" alt="Capa Aula {num_str}" /> **[{l["title"]}]({link_url})**  ')
        lines.append(f'  *Conteúdo programático da aula {num_str}, fundamentação técnica e automação.*')
        
    lines.append('\n</div>')
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
        
    # Identificar rel_base_url a partir da pasta content
    rel_path_from_content = os.path.relpath(course_dir, os.path.join(root_repo, "content"))
    # Para o Quartz, wikilinks ou links markdown são baseados no caminho exato a partir do root content
    rel_base_url = rel_path_from_content
    
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
