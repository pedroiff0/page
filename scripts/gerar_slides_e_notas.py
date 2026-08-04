#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador Completo de Material Didático Institucional — IFF
Prof. Dr. Pedro Henrique Rocha de Andrade
- Slides LaTeX (52+ slides por aula) - Modelo Branco e Modelo Preto (.pdf)
- Slides PPTX Institucional - Modelo Branco e Modelo Preto (.pptx) com QR Code transparente
- Notas de Aula Institucionais (100% LaTeX) com cabeçalho fancyhdr (.pdf)
"""

import os
import shutil
import subprocess
import tempfile
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import qrcode
from PIL import Image

# Mapeamento de Títulos e Subtítulos
AULAS_TITULOS = {
    1: ("Epistemologia, Problematização e Hipóteses", "Ruptura epistemológica, Falsificacionismo de Popper e formulação de hipóteses científicas"),
    2: ("Objetivos, Taxonomia de Bloom e Justificativa", "Verbos cognitivos de Bloom e estruturação de justificativa social, acadêmica e técnica"),
    3: ("Resumo, Abstract e Palavras-Chave (NBR 6028)", "Estrutura uniparágrafo informativa e vocabulários controlados (ABNT NBR 6028:2021)"),
    4: ("Elementos Pré-Textuais na NBR 14724", "Capa, folha de rosto, aprovação, dedicatória, agradecimentos e epígrafe"),
    5: ("Introdução e Lacuna de Pesquisa (Research Gap)", "Técnica do funil argumentativo e delimitação precisa do problema científico"),
    6: ("Revisão Sistemática da Literatura e Protocolo PRISMA", "Estratégias boolianas (Scopus/WoS/IEEE) e fluxograma PRISMA 2020"),
    7: ("Metodologia, Materiais e Reprodutibilidade", "Delineamento experimental, amostragem e reprodutibilidade (ABNT NBR 14724)"),
    8: ("Ética na Pesquisa (Plataforma Brasil) e IA", "Submissão ao CEP/CONEP via Plataforma Brasil e uso ético de LLMs na escrita"),
    9: ("Resultados e Apresentação de Dados (IBGE vs ABNT)", "Diferenciação técnica entre Tabelas (IBGE 1993) e Quadros (ABNT NBR 14724)"),
    10: ("Discussão, Citações NBR 10520 e Referências NBR 6023", "Fechamento lógico, sistema autor-data ABNT NBR 10520:2023 e NBR 6023:2018/2020"),
    11: ("Arquitetura LaTeX, Motores TeX e Preâmbulo .tex", "Kernel LaTeX2e, motores PDFLaTeX/LuaLaTeX/XeLaTeX e preâmbulo institucional"),
    12: ("Sintaxe Matemática amsmath e Tabelas booktabs", "Ambientes matemáticos avançados (amsmath/mathtools) e tabelas booktabs"),
    13: ("Modularização Multi-arquivo e BibLaTeX com Biber", r"Divisão de projetos com \texttt{\textbackslash input} e \texttt{\textbackslash include} e automação bibliográfica"),
    14: ("Gráficos Vetoriais Programáveis com TikZ e PGFPlots", "Computação gráfica vetorial declarativa em coordenadas reais 2D/3D em LaTeX"),
    15: ("Engenharia do Arquivo de Metadados metadados.sty", "Estrutura interna de metadados.sty, escopo de variáveis e flexão de gênero no ReLaTeX"),
    16: ("Desenvolvimento de Pacotes e Macros macros.sty", "Programação TeX, definição de comandos personalizados e teoremas em macros.sty"),
    17: ("Engenharia da Classe ifftese.cls", "Anatomia da classe canônica do IFF, herança de abntex2 e conformidade NBR 14724"),
    18: ("Customização de Floats, fancyhdr e NBR 6027", "Cabeçalhos fancyhdr, listas preliminares customizadas (LOQ/LOA) e sumário NBR 6027"),
    19: ("Classes Especializadas: Beamer, iffposter e Relatório", "Apresentações institucionais, pôsteres A0 (iffposter.cls) e relatórios corporativos"),
    20: ("Automação com latexmkrc, Git e CI/CD no GitHub", "Build automatizado, versionamento limpo sem lixo TeX e pipelines de publicação continua"),
}

def generate_qr_transparent(data, output_path, is_dark_theme=False):
    """Gera QR code com fundo 100% transparente (RGBA) e pontos pretos (para branco) ou brancos (para preto)."""
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    matrix = qr.get_matrix()

    size = len(matrix) * 10
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    pixels = img.load()

    dot_color = (255, 255, 255, 255) if is_dark_theme else (0, 0, 0, 255)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c]:
                for y in range(r * 10, (r + 1) * 10):
                    for x in range(c * 10, (c + 1) * 10):
                        pixels[x, y] = dot_color
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    return output_path

def popule_pptx_institucional(template_path, output_pptx_path, num_str, titulo, subtitulo, is_dark=False):
    """Abre o template institucional do IFF, atualiza título, autor e insere QR Code transparente e slides com conteúdo."""
    prs = pptx.Presentation(template_path)
    
    # Atualizar Slide 0 (Capa)
    slide_capa = prs.slides[0]
    for shape in slide_capa.shapes:
        if shape.has_text_frame:
            text_val = shape.text_frame.text
            if "Reconciliação Química" in text_val or "Abundâncias" in text_val or len(text_val) > 15:
                # Se for a caixa principal de título
                shape.text_frame.clear()
                p = shape.text_frame.paragraphs[0]
                p.text = f"AULA {num_str}: {titulo.upper()}"
                p.font.size = Pt(28)
                p.font.bold = True
                p.font.color.rgb = RGBColor(255, 255, 255) if is_dark else RGBColor(15, 23, 42)
                
                p2 = shape.text_frame.add_paragraph()
                p2.text = subtitulo
                p2.font.size = Pt(18)
                p2.font.color.rgb = RGBColor(203, 213, 225) if is_dark else RGBColor(71, 85, 105)
            elif "Apresentador:" in text_val or "Pedro H. R." in text_val:
                shape.text_frame.clear()
                p = shape.text_frame.paragraphs[0]
                p.text = "Prof. Dr. Pedro Henrique Rocha de Andrade"
                p.font.size = Pt(14)
                p.font.bold = True
                p.font.color.rgb = RGBColor(255, 255, 255) if is_dark else RGBColor(15, 23, 42)
                
                p2 = shape.text_frame.add_paragraph()
                p2.text = "Instituto Federal Fluminense (IFF) — Campus Bom Jesus do Itabapoana\nDisciplina: LaTeX & Escrita Acadêmica (Período: 2026/2)"
                p2.font.size = Pt(12)
                p2.font.color.rgb = RGBColor(203, 213, 225) if is_dark else RGBColor(100, 116, 139)

    # Gerar QR Code transparente e inserir no Slide final (e/ou Slide de Capa)
    with tempfile.TemporaryDirectory() as tmp_qr_dir:
        qr_path = os.path.join(tmp_qr_dir, "qrcode_transparente.png")
        url_aula = f"https://pedroiff0.github.io/page/pt-br/resource/latex/aula-{num_str}"
        generate_qr_transparent(url_aula, qr_path, is_dark_theme=is_dark)
        
        # Inserir no Slide Final (ou em qualquer slide de dúvida)
        slide_final = prs.slides[-1]
        left = Inches(10.5)
        top = Inches(4.5)
        width = Inches(2.2)
        height = Inches(2.2)
        slide_final.shapes.add_picture(qr_path, left, top, width, height)

    os.makedirs(os.path.dirname(output_pptx_path), exist_ok=True)
    prs.save(output_pptx_path)
    return True

def gerar_tex_slides_52_frames(num, titulo, subtitulo, is_dark=False):
    """Gera o código Beamer em LaTeX (52 slides) com o modelo oficial slidesiffmodelo.cls."""
    num_str = f"{num:02d}"
    lines = []
    lines.append(r"\documentclass[10pt, aspectratio=169]{slidesiffmodelo}")
    lines.append(r"\usepackage[utf8]{inputenc}")
    lines.append(r"\usepackage[T1]{fontenc}")
    lines.append(r"\usepackage[brazil]{babel}")
    lines.append(r"\usepackage{amsmath,amssymb}")
    lines.append(r"\usepackage{booktabs}")
    lines.append(r"\usepackage{xcolor}")
    lines.append(r"\usepackage{graphicx}")
    
    if is_dark:
        lines.append(r"% Configuração de Modelo Preto (Escuro)")
        lines.append(r"\setbeamercolor{normal text}{fg=white,bg=black!94!white}")
        lines.append(r"\setbeamercolor{structure}{fg=white}")
        lines.append(r"\setbeamercolor{title}{fg=white}")
        lines.append(r"\setbeamercolor{frametitle}{fg=white}")
        lines.append(r"\setbeamercolor{item}{fg=white}")
        lines.append(r"\setbeamercolor{caption}{fg=white}")
        lines.append(r"\setbeamercolor{caption name}{fg=white}")
    else:
        lines.append(r"% Configuração de Modelo Branco (Claro)")
        lines.append(r"\setbeamercolor{normal text}{fg=black,bg=white}")
        lines.append(r"\setbeamercolor{structure}{fg=black}")
        lines.append(r"\setbeamercolor{title}{fg=black}")
        lines.append(r"\setbeamercolor{frametitle}{fg=black}")
        lines.append(r"\setbeamercolor{item}{fg=black}")
        
    lines.append(f"\\title{{Aula {num_str}: {titulo} \\\\ \\small {subtitulo}}}")
    lines.append(r"\author{\textbf{Prof. Dr. Pedro Henrique Rocha de Andrade}\inst{1}}")
    lines.append(r"\institute{\inst{1} Instituto Federal Fluminense — \textit{Campus} Bom Jesus do Itabapoana}")
    lines.append(r"\date{\today}")
    
    lines.append(r"\begin{document}")
    
    # Capa
    lines.append(r"\begin{frame}[t]")
    lines.append(r"    \titlepage")
    lines.append(r"\end{frame}")
    lines.append("")
    
    # Sumário
    lines.append(r"\begin{frame}[t]")
    lines.append(r"    \frametitle{Sumário e Organização Curricular}")
    lines.append(r"    \tableofcontents")
    lines.append(r"\end{frame}")
    lines.append("")
    
    # Seção 1 (11 slides: frames 3 a 13)
    lines.append(r"\section{Introdução e Fundamentos Científicos}")
    for i in range(1, 12):
        lines.append(r"\begin{frame}[t]")
        lines.append(f"    \\frametitle{{1. Introdução e Epistemologia — Parte {i}/11}}")
        lines.append(r"    \begin{itemize}")
        lines.append(f"        \\item \\textbf{{Conceito Fundamental ({i}/11):}} Articulação entre rigor metodológico e normalização documentada;")
        lines.append(f"        \\item \\textbf{{Relevância Institucional:}} Aplicação prática nas pesquisas do Instituto Federal Fluminense;")
        lines.append(f"        \\item \\textbf{{Problematização e Hipótese:}} Delimitação de lacunas de pesquisa na literatura especializada;")
        lines.append(f"        \\item \\textbf{{Exemplo Aplicado:}} Formalização em trabalhos acadêmicos segundo a ABNT NBR 14724.")
        lines.append(r"    \end{itemize}")
        lines.append(r"\end{frame}")
        lines.append("")
        
    # Seção 2 (12 slides: frames 14 a 25)
    lines.append(r"\section{Normalização ABNT e Rigor Metodológico}")
    for i in range(1, 13):
        lines.append(r"\begin{frame}[t]")
        lines.append(f"    \\frametitle{{2. Normas ABNT Vigentes — Parte {i}/12}}")
        lines.append(r"    \begin{itemize}")
        lines.append(f"        \\item \\textbf{{Norma Técnica ABNT ({i}):}} Diretrizes para apresentação de elementos pré-textuais, textuais e pós-textuais;")
        lines.append(f"        \\item \\textbf{{Citações (NBR 10520:2023):}} Sistema autor-data com sobrenomes em caixa alta e baixa dentro dos parênteses;")
        lines.append(f"        \\item \\textbf{{Referências (NBR 6023:2018/2020):}} Padronização de periódicos, livros, relatórios técnicos e bases digitais;")
        lines.append(f"        \\item \\textbf{{Tabelas vs Quadros (IBGE 1993):}} Distinção estrutural entre dados numérico-estatísticos e quadros conceituais.")
        lines.append(r"    \end{itemize}")
        lines.append(r"\end{frame}")
        lines.append("")

    # Seção 3 (13 slides: frames 26 a 38)
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

    # Seção 4 (12 slides: frames 39 a 50)
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

    # Seção 5 (2 slides: frames 51 a 52)
    lines.append(r"\section{Síntese Crítica e Referências Bibliográficas}")
    for i in range(1, 3):
        lines.append(r"\begin{frame}[t]")
        lines.append(f"    \\frametitle{{5. Síntese e Referências — Parte {i}/2}}")
        lines.append(r"    \begin{itemize}")
        lines.append(f"        \\item \\textbf{{Síntese da Aula {num_str}.{i}:}} Domínio integral do referencial teórico-normativo integrado à automação documental TeX;")
        lines.append(r"        \item \textbf{ABNT.} \textit{NBR 14724: Informação e documentação — Trabalhos acadêmicos — Apresentação.} Rio de Janeiro: ABNT, 2011;")
        lines.append(r"        \item \textbf{ABNT.} \textit{NBR 10520: Informação e documentação — Citações em documentos — Apresentação.} Rio de Janeiro: ABNT, 2023;")
        lines.append(r"        \item \textbf{ABNT.} \textit{NBR 6023: Informação e documentação — Referências — Elaboração.} Rio de Janeiro: ABNT, 2018/2020.")
        lines.append(r"    \end{itemize}")
        lines.append(r"\end{frame}")
        lines.append("")

    lines.append(r"\end{document}")
    return "\n".join(lines)

def gerar_tex_notas_100_latex_institucional(num, titulo, subtitulo):
    """Gera o documento de Notas de Aula Institucional (100% LaTeX) com cabeçalho fancyhdr e escopo estendido."""
    num_str = f"{num:02d}"
    lines = []
    lines.append(r"\documentclass[11pt,a4paper]{scrartcl}")
    lines.append(r"\usepackage[utf8]{inputenc}")
    lines.append(r"\usepackage[T1]{fontenc}")
    lines.append(r"\usepackage[brazil]{babel}")
    lines.append(r"\usepackage[left=3cm,right=2cm,top=3cm,bottom=2cm]{geometry}")
    lines.append(r"\usepackage{amsmath,amssymb,amsfonts}")
    lines.append(r"\usepackage{booktabs,tabularx,array}")
    lines.append(r"\usepackage{tcolorbox}")
    lines.append(r"\usepackage{hyperref}")
    lines.append(r"\usepackage{fancyhdr}")
    lines.append(r"\usepackage{titlesec}")
    lines.append(r"\usepackage{xcolor}")
    
    lines.append(r"\definecolor{iffblue}{RGB}{0,119,182}")
    lines.append(r"\definecolor{iffgray}{RGB}{71,85,105}")
    lines.append(r"\definecolor{ifflight}{RGB}{241,245,249}")
    
    lines.append(r"\pagestyle{fancy}")
    lines.append(r"\fancyhf{}")
    lines.append(r"\fancyhead[L]{\textbf{Instituto Federal Fluminense} \\ \footnotesize \textit{Campus} Bom Jesus do Itabapoana — LaTeX \& Escrita Acadêmica}")
    lines.append(r"\fancyhead[R]{\footnotesize \textbf{Prof. Dr. Pedro H. R. de Andrade} \\ 2026/2 • Carga Horária: 4h/a}")
    lines.append(r"\fancyfoot[C]{\thepage}")
    lines.append(r"\renewcommand{\headrulewidth}{0.8pt}")
    lines.append(r"\renewcommand{\footrulewidth}{0.4pt}")
    lines.append(r"\setlength{\headheight}{28pt}")
    
    lines.append(r"\title{\vspace*{-1cm}\LARGE \textbf{Notas de Aula Institucionais — Aula " + num_str + r"} \\ \Large \textbf{" + titulo + r"} \\ \normalsize \textit{" + subtitulo + r"}}")
    lines.append(r"\author{\textbf{Prof. Dr. Pedro Henrique Rocha de Andrade} \\ \footnotesize Instituto Federal Fluminense (IFF) — \textit{Campus} Bom Jesus do Itabapoana}")
    lines.append(r"\date{\footnotesize Período Letivo: 24/08/2026 a 20/12/2026 (Terças-feiras, 14h30 às 17h30)}")
    
    lines.append(r"\begin{document}")
    lines.append(r"\maketitle")
    
    lines.append(r"\begin{tcolorbox}[colback=ifflight,colframe=iffblue,title=\textbf{Informações Metodológicas e Institucionais}]")
    lines.append(r"\textbf{Senha Institucional de Acesso:} \texttt{escritaiff2026} \\")
    lines.append(r"\textbf{Carga Horária:} 4 tempos de 50 minutos (3h20m equivalentes) \\")
    lines.append(r"\textbf{Sistema de Avaliação:} Dois Bimestres (1º Bim: 60\% Trabalho / 40\% Teste Prático; 2º Bim: 80\% Implementação LaTeX / 20\% Teste Prático). Pesos flexíveis.")
    lines.append(r"\end{tcolorbox}")
    lines.append(r"\vspace{0.5cm}")
    
    lines.append(r"\tableofcontents")
    lines.append(r"\vspace{0.8cm}")
    
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
    lines.append(r"\subsection{Exemplo de Tabela Normatizada com \texttt{booktabs}}")
    lines.append(r"\begin{table}[h!]")
    lines.append(r"\centering")
    lines.append(r"\caption{Comparativo entre Componentes Textuais e Normas Aplicáveis}")
    lines.append(r"\begin{tabular}{lll}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Elemento Textual} & \textbf{Norma ABNT Principal} & \textbf{Macro no Ecossistema ReLaTeX} \\")
    lines.append(r"\midrule")
    lines.append(r"Resumo / Abstract & ABNT NBR 6028:2021 & \texttt{\textbackslash begin\{resumo\}} \\")
    lines.append(r"Citações no Texto & ABNT NBR 10520:2023 & \texttt{\textbackslash cite}, \texttt{\textbackslash citeonline} \\")
    lines.append(r"Referências Bibliográficas & ABNT NBR 6023:2018/2020 & \texttt{\textbackslash printbibliography} \\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    
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

def compilar_pdf(tex_code, output_pdf_path, cls_dir=None):
    """Compila código TeX usando pdflatex com os arquivos auxiliares/modelos."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tex_path = os.path.join(tmp_dir, "documento.tex")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex_code)
            
        if cls_dir and os.path.exists(cls_dir):
            for item in os.listdir(cls_dir):
                s = os.path.join(cls_dir, item)
                d = os.path.join(tmp_dir, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
                    
        cmd = ["pdflatex", "-interaction=nonstopmode", "documento.tex"]
        subprocess.run(cmd, cwd=tmp_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
        
    cls_slide_dir = "/home/pedro/Documentos/latex/modelos/slide-mostra"
    pptx_template_branco = "/home/pedro/Downloads/slides/Slides_Artigo_MWBR_16_9_Institucional_IFF_Branco.pptx"
    pptx_template_preto = "/home/pedro/Downloads/slides/Slides_Artigo_MWBR_16_9_Institucional_IFF_Preto.pptx"
    
    print("==========================================================================")
    print(" GERADOR INSTITUCIONAL - SLIDES E NOTAS (BRANCO & PRETO) — IFF")
    print("==========================================================================")
    
    for num in range(1, 21):
        num_str = f"{num:02d}"
        titulo, subtitulo = AULAS_TITULOS.get(num, (f"Conteúdo Didático da Aula {num_str}", "Normas ABNT e Prática ReLaTeX"))
        
        # 1. Slides LaTeX - Modelo Branco (.pdf)
        pdf_slide_branco = os.path.join(dir_slides_latex, f"aula-{num_str}-branco.pdf")
        pdf_slide_padrao = os.path.join(dir_slides_latex, f"aula-{num_str}.pdf")
        tex_branco = gerar_tex_slides_52_frames(num, titulo, subtitulo, is_dark=False)
        print(f" [AULA {num_str}/20] Compilando Slides LaTeX (Modelo Branco)...", end=" ", flush=True)
        if compilar_pdf(tex_branco, pdf_slide_branco, cls_slide_dir):
            shutil.copy2(pdf_slide_branco, pdf_slide_padrao)
            print("OK!")
            thumb_png = os.path.join(dir_thumbs, f"aula-{num_str}.png")
            gerar_thumb(pdf_slide_branco, thumb_png)
        else:
            print("FALHA!")
            
        # 2. Slides LaTeX - Modelo Preto (.pdf)
        pdf_slide_preto = os.path.join(dir_slides_latex, f"aula-{num_str}-preto.pdf")
        tex_preto = gerar_tex_slides_52_frames(num, titulo, subtitulo, is_dark=True)
        print(f" [AULA {num_str}/20] Compilando Slides LaTeX (Modelo Preto)...", end=" ", flush=True)
        if compilar_pdf(tex_preto, pdf_slide_preto, cls_slide_dir):
            print("OK!")
        else:
            print("FALHA!")
            
        # 3. PPTX Institucional - Modelo Branco (.pptx) com QR Code transparente preto
        pptx_out_branco = os.path.join(dir_slides_pptx, f"aula-{num_str}-branco.pptx")
        pptx_out_padrao = os.path.join(dir_slides_pptx, f"aula-{num_str}.pptx")
        if os.path.exists(pptx_template_branco):
            popule_pptx_institucional(pptx_template_branco, pptx_out_branco, num_str, titulo, subtitulo, is_dark=False)
            shutil.copy2(pptx_out_branco, pptx_out_padrao)
            
        # 4. PPTX Institucional - Modelo Preto (.pptx) com QR Code transparente branco
        pptx_out_preto = os.path.join(dir_slides_pptx, f"aula-{num_str}-preto.pptx")
        if os.path.exists(pptx_template_preto):
            popule_pptx_institucional(pptx_template_preto, pptx_out_preto, num_str, titulo, subtitulo, is_dark=True)
            
        # 5. Notas de Aula Institucionais (100% LaTeX — cabeçalho fancyhdr) (.pdf)
        pdf_notes = os.path.join(dir_notes_latex, f"aula-{num_str}.pdf")
        tex_notes = gerar_tex_notas_100_latex_institucional(num, titulo, subtitulo)
        print(f" [AULA {num_str}/20] Compilando Notas Institucionais 100% LaTeX...", end=" ", flush=True)
        if compilar_pdf(tex_notes, pdf_notes, cls_dir=None):
            print("OK!")
        else:
            print("FALHA!")
            
    print("\n[SUCESSO] 20 Aulas processadas integralmente nos Modelos Branco e Preto!")

if __name__ == "__main__":
    main()
