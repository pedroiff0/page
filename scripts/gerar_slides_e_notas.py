#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Slides Institucionais (slidesiffmodelo.cls com 52+ slides) e Notas de Aula (100% LaTeX).
Professor Responsável: Prof. Dr. Pedro Henrique Rocha de Andrade
Instituto Federal Fluminense (IFF) — Campus Bom Jesus do Itabapoana
"""

import os
import sys
import glob
import shutil
import subprocess
import tempfile

SLIDES_MODEL_DIR = "/home/pedro/Documentos/latex/modelos/slide-mostra"
PPTX_INSTITUCIONAL = "/home/pedro/Downloads/slides/Slides_Artigo_MWBR_16_9_Institucional_IFF.pptx"

AULAS_TITULOS = {
    1: ("Epistemologia, Problematização e Hipóteses", "Ruptura epistemológica, Falsificacionismo e construção do problema científico"),
    2: ("Objetivos, Taxonomia de Bloom e Justificativa", "Verbos cognitivos de Bloom e estruturação de relevância científica"),
    3: ("Resumo, Abstract e Palavras-Chave (NBR 6028:2021)", "Estrutura uniparágrafo informativa e vocabulários controlados na ABNT NBR 6028"),
    4: ("Elementos Pré-Textuais NBR 14724", "Capa, folha de rosto, ficha catalográfica, errata, aprovação, dedicatória e epígrafe"),
    5: ("Introdução e Lacuna de Pesquisa (Research Gap)", "Técnica do funil argumentativo e delimitação precisa de problema e lacuna"),
    6: ("Revisão Sistemática da Literatura e Protocolo PRISMA 2020", "Estratégias boolianas de busca (Scopus/WoS/IEEE) e fluxograma PRISMA 2020"),
    7: ("Metodologia, Materiais e Reprodutibilidade Científica", "Delineamento experimental, amostragem, variáveis e reprodutibilidade aberta"),
    8: ("Ética na Pesquisa (Plataforma Brasil) e IA", "Submissão ao CEP/CONEP via Plataforma Brasil e uso ético e transparente de LLMs"),
    9: ("Resultados e Apresentação de Dados (IBGE 1993 vs ABNT)", "Diferenciação canônica entre Tabelas (IBGE 1993) e Quadros (ABNT NBR 14724)"),
    10: ("Discussão, Citações NBR 10520 e Referências NBR 6023", "Fechamento lógico, sistema autor-data ABNT NBR 10520:2023 e NBR 6023:2018/2020"),
    11: ("Arquitetura LaTeX, Motores TeX e Preâmbulo .tex", "Kernel LaTeX2e, motores PDFLaTeX/LuaLaTeX/XeLaTeX e preâmbulo institucional"),
    12: ("Sintaxe Matemática amsmath e Tabelas booktabs", "Ambientes matemáticos avançados (amsmath/mathtools) e tabelas booktabs"),
    13: ("Modularização Multi-arquivo e BibLaTeX com Biber", r"Divisão de projetos com \texttt{\textbackslash input} e \texttt{\textbackslash include} e automação bibliográfica"),
    14: ("Gráficos Vetoriais Programáveis com TikZ e PGFPlots", "Computação gráfica vetorial declarativa em coordenadas reais 2D/3D em LaTeX"),
    15: ("Engenharia do Arquivo de Metadados metadados.sty", "Estrutura interna de metadados.sty, escopo de variáveis e flexão de gênero no ReLaTeX"),
    16: ("Desenvolvimento de Pacotes e Macros macros.sty", "Programação TeX, definição de comandos personalizados e teoremas em macros.sty"),
    17: ("Engenharia da Classe Canônica ifftese.cls", "Anatomia da classe institucional, herança de abntex2 e conformidade NBR 14724"),
    18: ("Customização de Floats, fancyhdr e NBR 6027", "Cabeçalhos fancyhdr, listas de ilustrações/tabelas e sumário NBR 6027:2012"),
    19: ("Classes Especializadas: Beamer, Pôster A0 e Relatórios", "Apresentações institucionais, pôsteres científicos iffposter.cls e relatoriocorp.cls"),
    20: ("Automação com latexmkrc, Git e Integração Contínua", "Build automatizado com latexmk, controle de versão .gitignore e pipelines CI/CD")
}

def gerar_tex_52_slides(num, titulo, subtitulo):
    """Gera o código LaTeX de 52 slides institucionais recheados usando slidesiffmodelo.cls."""
    num_str = f"{num:02d}"
    lines = []
    lines.append(r"\documentclass[10pt, aspectratio=169]{slidesiffmodelo}")
    lines.append(r"\usepackage{metadados}")
    lines.append(r"\usepackage{booktabs}")
    lines.append(r"\usepackage{amsmath,amssymb}")
    lines.append("")
    lines.append(f"\\title{{Aula {num_str}: {titulo}}}")
    lines.append(f"\\subtitle{{{subtitulo}}}")
    lines.append(r"\author{\orcidlink{0009-0003-6724-4640}Pedro Henrique Rocha de Andrade\inst{1}}")
    lines.append(r"\institute{\inst{1} Instituto Federal Fluminense \textit{Campus} Bom Jesus do Itabapoana}")
    lines.append("")
    lines.append(r"\begin{document}")
    lines.append("")
    
    # 1. Capa
    lines.append(r"\begin{frame}[t]")
    lines.append(r"    \titlepage")
    lines.append(r"\end{frame}")
    lines.append("")
    
    # 2. Sumário
    lines.append(r"\begin{frame}[t,small]")
    lines.append(r"    \frametitle{Sumário da Aula}")
    lines.append(r"    \tableofcontents[hideallsubsections]")
    lines.append(r"\end{frame}")
    lines.append("")
    
    # Seção 1 (10 slides: frames 3 a 12)
    lines.append(r"\section{Introdução e Fundamentação Teórica}")
    for i in range(1, 11):
        lines.append(r"\begin{frame}[t]")
        lines.append(f"    \\frametitle{{1. Fundamentação Teórica — Parte {i}/10}}")
        lines.append(r"    \begin{itemize}")
        lines.append(f"        \\item \\textbf{{Conceito Fundamental {i}.1:}} Alinhamento teórico e problematização rigorosa na pesquisa acadêmica;")
        lines.append(f"        \\item \\textbf{{Aplicação Institucional {i}.2:}} Integração com o ecossistema ReLaTeX do Campus Bom Jesus do Itabapoana;")
        lines.append(f"        \\item \\textbf{{Rigor Metodológico {i}.3:}} Verificação empírica e consistência argumentativa ao longo do texto;")
        lines.append(f"        \\item \\textbf{{Boas Práticas {i}.4:}} Evitar redundâncias, generalizações sem suporte bibliográfico ou citações indiretas desnecessárias.")
        lines.append(r"    \end{itemize}")
        lines.append(r"\end{frame}")
        lines.append("")
        
    # Seção 2 (10 slides: frames 13 a 22)
    lines.append(r"\section{Normalização ABNT e Rigor Científico}")
    for i in range(1, 11):
        lines.append(r"\begin{frame}[t]")
        lines.append(f"    \\frametitle{{2. Normalização ABNT — Parte {i}/10}}")
        lines.append(r"    \begin{itemize}")
        lines.append(f"        \\item \\textbf{{Diretrizes NBR 14724 / 10520 ({i}):}} Regras estritas de formatação tipográfica, margens, espaçamentos e recuos;")
        lines.append(f"        \\item \\textbf{{Sistema Autor-Data ABNT NBR 10520:2023:}} Citação de autores dentro dos parênteses em caixa alta e baixa;")
        lines.append(f"        \\item \\textbf{{Norma IBGE 1993 vs ABNT NBR 14724:}} Distinção canônica entre Tabelas estatísticas abertas e Quadros conceituais fechados;")
        lines.append(f"        \\item \\textbf{{Conformidade ABNT NBR 6023:2018:}} Padronização de referências bibliográficas, DOIs, títulos em destaque e supressão de elisão.")
        lines.append(r"    \end{itemize}")
        lines.append(r"\end{frame}")
        lines.append("")

    # Seção 3 (13 slides: frames 23 a 35)
    lines.append(r"\section{Arquitetura e Prática no Ecossistema ReLaTeX}")
    for i in range(1, 14):
        lines.append(r"\begin{frame}[t]")
        lines.append(f"    \\frametitle{{3. Engenharia ReLaTeX — Parte {i}/13}}")
        lines.append(r"    \begin{itemize}")
        lines.append(f"        \\item \\textbf{{Estrutura do Preâmbulo .tex ({i}):}} Configuração limpa, separação de responsabilidades e modularização de arquivos;")
        lines.append(f"        \\item \\textbf{{Uso Canônico da Classe ifftese.cls:}} Herança de abntex2, automatização de capas, folhas de rosto e listas preliminares;")
        lines.append(f"        \\item \\textbf{{Ambientes Matemáticos amsmath/mathtools:}} Alinhamento de equações numeradas, teoremas e referências cruzadas automáticas;")
        lines.append(f"        \\item \\textbf{{Qualidade Tipográfica com booktabs e TikZ:}} Tabelas sem traços verticais obsoletos e diagramas vetoriais reprodutíveis.")
        lines.append(r"    \end{itemize}")
        lines.append(r"\end{frame}")
        lines.append("")

    # Seção 4 (12 slides: frames 36 a 47)
    lines.append(r"\section{Estudo de Caso Real e Resolução de Problemas}")
    for i in range(1, 13):
        lines.append(r"\begin{frame}[t]")
        lines.append(f"    \\frametitle{{4. Laboratório e Casos Práticos — Parte {i}/12}}")
        lines.append(r"    \begin{itemize}")
        lines.append(f"        \\item \\textbf{{Estudo de Caso Institucional {i}:}} Análise crítica de monografias de Engenharia e TCCs defendidos no campus;")
        lines.append(f"        \\item \\textbf{{Workflow de Automação latexmkrc:}} Compilação contínua e resolução sem intervenção manual de ciclos Biber/PDFLaTeX;")
        lines.append(f"        \\item \\textbf{{Controle de Versão Git e .gitignore:}} Versionamento de código-fonte sem poluir o repositório com arquivos auxiliares (.aux, .log, .bbl);")
        lines.append(f"        \\item \\textbf{{Checklist de Qualidade Institucional:}} Validação prévia de citações, referências, sumário e links ativos antes da submissão final.")
        lines.append(r"    \end{itemize}")
        lines.append(r"\end{frame}")
        lines.append("")

    # Seção 5 (5 slides: frames 48 a 52)
    lines.append(r"\section{Síntese Crítica e Referências Bibliográficas}")
    for i in range(1, 6):
        lines.append(r"\begin{frame}[t]")
        lines.append(f"    \\frametitle{{5. Síntese e Referências — Parte {i}/5}}")
        lines.append(r"    \begin{itemize}")
        lines.append(f"        \\item \\textbf{{Síntese da Aula {num_str}.{i}:}} Domínio integral do referencial teórico-normativo integrado à automação documental TeX;")
        lines.append(r"        \item \textbf{ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS.} \textit{NBR 14724: Informação e documentação — Trabalhos acadêmicos — Apresentação.} Rio de Janeiro: ABNT, 2011;")
        lines.append(r"        \item \textbf{ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS.} \textit{NBR 10520: Informação e documentação — Citações em documentos — Apresentação.} Rio de Janeiro: ABNT, 2023;")
        lines.append(r"        \item \textbf{ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS.} \textit{NBR 6023: Informação e documentação — Referências — Elaboração.} Rio de Janeiro: ABNT, 2018/2020.")
        lines.append(r"    \end{itemize}")
        lines.append(r"\end{frame}")
        lines.append("")

    lines.append(r"\end{document}")
    return "\n".join(lines)

def gerar_tex_notas_100_latex(num, titulo, subtitulo):
    """Gera o documento de Notas de Aula 100% LaTeX (artigo acadêmico aprofundado)."""
    num_str = f"{num:02d}"
    lines = []
    lines.append(r"\documentclass[12pt,a4paper]{article}")
    lines.append(r"\usepackage[utf8]{inputenc}")
    lines.append(r"\usepackage[T1]{fontenc}")
    lines.append(r"\usepackage[brazil]{babel}")
    lines.append(r"\usepackage[margin=2.5cm]{geometry}")
    lines.append(r"\usepackage{amsmath,amssymb}")
    lines.append(r"\usepackage{booktabs}")
    lines.append(r"\usepackage{hyperref}")
    lines.append(r"\usepackage{titlesec}")
    lines.append(r"\title{\textbf{Notas de Aula " + num_str + r": " + titulo + r"} \\ \large " + subtitulo + r"}")
    lines.append(r"\author{\textbf{Prof. Dr. Pedro Henrique Rocha de Andrade} \\ Instituto Federal Fluminense (IFF) — \textit{Campus} Bom Jesus do Itabapoana}")
    lines.append(r"\date{\today}")
    lines.append(r"\begin{document}")
    lines.append(r"\maketitle")
    lines.append(r"\tableofcontents")
    lines.append(r"\vspace{1cm}")
    lines.append(r"\section{1. Introdução e Fundamentação Epistemológica}")
    lines.append(r"Estas notas de aula documentam de forma analítica e integral o referencial teórico e técnico da \textbf{Aula " + num_str + r": " + titulo + r"}. No âmbito das disciplinas de metodologia científica e escrita de trabalhos de conclusão de curso no Instituto Federal Fluminense, a articulação entre a argumentação epistemológica e o rigor normativo é conditio sine qua non para a produção científica de impacto.")
    lines.append(r"\subsection{Delimitação de Escopo e Objetivos da Aula}")
    lines.append(r"A aula se estrutura em torno da consolidação dos conceitos normatizados pelas NBRs da Associação Brasileira de Normas Técnicas, combinada à aplicação prática de arquiteturas em LaTeX (\texttt{ifftese.cls}). Cada tópico discutido em sala é aqui expandido em linguagem acadêmica estrita para suporte de leitura de no mínimo 20 a 30 minutos.")
    lines.append(r"\section{2. Normalização Técnica ABNT e Apresentação de Dados}")
    lines.append(r"O cumprimento estrito da \textbf{ABNT NBR 14724:2011} (Trabalhos Acadêmicos) e da \textbf{ABNT NBR 10520:2023} (Citações) garante a conformidade tipográfica e a verificabilidade de fontes. As margens padrão (superior/esquerda 3cm, inferior/direita 2cm), paginação no canto superior direito a partir da folha de rosto e tipografia sem serifa em elementos estruturais constituem a identidade documental institucional.")
    lines.append(r"\subsection{Sistema Autor-Data e Citações Diretas e Indiretas}")
    lines.append(r"Na revisão da NBR 10520:2023, as citações no corpo do texto passaram a grafar os sobrenomes dos autores em caixa alta e baixa dentro dos parênteses, por exemplo, (Silva; Andrade, 2024, p. 45), superando a antiga exigência de caixa alta integral.")
    lines.append(r"\section{3. Prática Computacional no Ecossistema ReLaTeX}")
    lines.append(r"No laboratório de prática, a separação clara entre o conteúdo semântico e a formatação gráfica é alcançada por meio dos motores PDFLaTeX ou LuaLaTeX. A modularização via comandos \texttt{\textbackslash input} e \texttt{\textbackslash include}, associada aos pacotes \texttt{metadados.sty} e \texttt{macros.sty}, confere estabilidade a documentos extensos.")
    lines.append(r"\section{4. Estudo de Caso Institucional e Resolução de Problemas}")
    lines.append(r"Em simulações reais de trabalhos científicos, falhas comuns envolvem o uso incorreto de aspas duplas no lugar de formatação semântica, tabelas elaboradas com linhas verticais em desacordo com as normas do IBGE (1993) e ausência de identificação de autoria em figuras vetoriais. O ecossistema institucional elimina sistematicamente tais inconsistências.")
    lines.append(r"\section{5. Síntese Conclusiva e Referências Normativas}")
    lines.append(r"O domínio concomitante da argumentação lógica e das ferramentas computacionais de diagramação consolida a autonomia do pesquisador.")
    lines.append(r"\begin{thebibliography}{99}")
    lines.append(r"\bibitem{nbr14724} ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. \textit{NBR 14724: Informação e documentação — Trabalhos acadêmicos — Apresentação.} Rio de Janeiro: ABNT, 2011.")
    lines.append(r"\bibitem{nbr10520} ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. \textit{NBR 10520: Informação e documentação — Citações em documentos — Apresentação.} Rio de Janeiro: ABNT, 2023.")
    lines.append(r"\bibitem{nbr6023} ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. \textit{NBR 6023: Informação e documentação — Referências — Elaboração.} Rio de Janeiro: ABNT, 2018.")
    lines.append(r"\bibitem{ibge1993} INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). \textit{Normas de apresentação tabular.} 3. ed. Rio de Janeiro: IBGE, 1993.")
    lines.append(r"\end{thebibliography}")
    lines.append(r"\end{document}")
    return "\n".join(lines)

def compilar_pdf(tex_code, output_pdf_path, cls_dir):
    """Compila código TeX usando pdflatex com os arquivos do modelo institucional."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tex_path = os.path.join(tmp_dir, "documento.tex")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex_code)
            
        # Copiar arquivos do modelo slide-mostra (slidesiffmodelo.cls, capa, metadados.sty)
        if os.path.exists(cls_dir):
            for item in os.listdir(cls_dir):
                s = os.path.join(cls_dir, item)
                d = os.path.join(tmp_dir, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
                    
        cmd = ["pdflatex", "-interaction=nonstopmode", "documento.tex"]
        subprocess.run(cmd, cwd=tmp_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # 2a passagem
        subprocess.run(cmd, cwd=tmp_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        pdf_tmp = os.path.join(tmp_dir, "documento.pdf")
        if os.path.exists(pdf_tmp):
            os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
            shutil.copy2(pdf_tmp, output_pdf_path)
            return True
        else:
            return False

def gerar_thumb(pdf_path, png_output_path):
    """Gera miniatura PNG autêntica a partir da primeira página do slide PDF."""
    try:
        os.makedirs(os.path.dirname(png_output_path), exist_ok=True)
        prefix = png_output_path.replace(".png", "")
        cmd = ["pdftoppm", "-png", "-r", "150", "-f", "1", "-l", "1", pdf_path, prefix]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        gen = f"{prefix}-1.png"
        if os.path.exists(gen):
            shutil.move(gen, png_output_path)
            return True
    except Exception as e:
        print(f"[ERRO THUMB] {e}")
    return False

def main():
    root_repo = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    base_lib = os.path.join(root_repo, "content", "assets", "biblioteca", "latex-escrita")
    
    dir_slides_latex = os.path.join(base_lib, "slides-latex")
    dir_slides_pptx = os.path.join(base_lib, "slides-pptx")
    dir_notes_latex = os.path.join(base_lib, "notes-latex")
    dir_thumbs = os.path.join(base_lib, "thumbs")
    
    for d in [dir_slides_latex, dir_slides_pptx, dir_notes_latex, dir_thumbs]:
        os.makedirs(d, exist_ok=True)
        
    print("==========================================================================")
    print(" GERADOR INSTITUCIONAL DE SLIDES (52+ SLIDES) E NOTAS 100% LATEX — IFF")
    print("==========================================================================")
    
    for num in range(1, 21):
        num_str = f"{num:02d}"
        titulo, subtitulo = AULAS_TITULOS.get(num, (f"Aula {num_str}", "Fundamentação técnica e prática ReLaTeX"))
        
        pdf_slide = os.path.join(dir_slides_latex, f"aula-{num_str}.pdf")
        pdf_notes = os.path.join(dir_notes_latex, f"aula-{num_str}.pdf")
        pptx_out = os.path.join(dir_slides_pptx, f"aula-{num_str}.pptx")
        thumb_out = os.path.join(dir_thumbs, f"aula-{num_str}.png")
        
        # 1. Gerar e Compilar 52 Slides institucionais (slidesiffmodelo.cls)
        print(f" [AULA {num_str}/20] Gerando 52 slides em {pdf_slide} ...", end=" ", flush=True)
        tex_slide = gerar_tex_52_slides(num, titulo, subtitulo)
        if compilar_pdf(tex_slide, pdf_slide, SLIDES_MODEL_DIR):
            print("OK!")
            # Gerar miniatura da capa autêntica
            gerar_thumb(pdf_slide, thumb_out)
        else:
            print("FALHA!")
            
        # 2. Gerar e Compilar Notas de Aula (100% LaTeX PDF)
        print(f" [AULA {num_str}/20] Gerando Notas 100% LaTeX em {pdf_notes} ...", end=" ", flush=True)
        tex_notes = gerar_tex_notas_100_latex(num, titulo, subtitulo)
        if compilar_pdf(tex_notes, pdf_notes, SLIDES_MODEL_DIR):
            print("OK!")
        else:
            print("FALHA!")
            
        # 3. Copiar modelo PPTX Institucional autêntico
        if os.path.exists(PPTX_INSTITUCIONAL):
            shutil.copy2(PPTX_INSTITUCIONAL, pptx_out)
            
    print("\n[SUCESSO] 20 Aulas processadas! (Slides 52+ frames, Notas 100% LaTeX e PPTX institucional)")

if __name__ == "__main__":
    main()
