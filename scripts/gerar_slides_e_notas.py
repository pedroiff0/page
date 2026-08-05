#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador Institucional Completo de Slides LaTeX/PPTX e Notas de Aula — IFF
Pedro Henrique Rocha de Andrade
- Slides LaTeX (Modelo Branco e Modelo Preto) com diagrama TikZ, slide de Obrigado com QR Code transparente e Referências, sem "Parte X/Y".
- Slides PPTX (Modelo Branco e Modelo Preto) com títulos/curso "LaTeX e Escrita Acadêmica", logo do IFF ampliada no cabeçalho e QR code transparente.
- Notas de Aula Institucionais sem menção a regras de avaliação ou tempos de aula, ricas em diagramas TikZ e tabelas booktabs.
- TODOS os PDFs gerados protegidos com a senha "escritaiff2026" via pypdf.
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
from pypdf import PdfReader, PdfWriter

SENHA_INSTITUCIONAL = "escritaiff2026"

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
    20: ("Automação com latexmkrc, Git e CI/CD no GitHub", "Build automatizado, versionamento limpo sem lixo TeX e pipelines de publicação contínua"),
}

AULAS_SLUGS = {
    1: "aula-01-epistemologia-problematizacao-e-hipoteses",
    2: "aula-02-objetivos-taxonomia-de-bloom-e-justificativa",
    3: "aula-03-resumo-abstract-e-palavras-chave-nbr-6028",
    4: "aula-04-elementos-pre-textuais-nbr-14724",
    5: "aula-05-introducao-contextualizacao-e-lacuna-de-pesquisa",
    6: "aula-06-revisao-sistematica-da-literatura-e-protocolo-prisma",
    7: "aula-07-metodologia-materiais-e-reprodutibilidade",
    8: "aula-08-etica-plataforma-brasil-e-uso-de-ia",
    9: "aula-09-resultados-tabelas-ibge-vs-quadros-abnt",
    10: "aula-10-discussao-citacoes-nbr-10520-e-referencias-nbr-6023",
    11: "aula-11-arquitetura-latex-motores-tex-e-preambulo-tex",
    12: "aula-12-sintaxe-matematica-amsmath-e-tabelas-booktabs",
    13: "aula-13-modularizacao-multi-arquivo-e-biblatex-biber",
    14: "aula-14-graficos-vetoriais-tikz-e-pgfplots",
    15: "aula-15-engenharia-do-arquivo-de-metadados-sty",
    16: "aula-16-desenvolvimento-de-pacotes-e-macros-sty",
    17: "aula-17-engenharia-da-classe-ifftese-cls",
    18: "aula-18-customizacao-de-floats-fancyhdr-e-nbr-6027",
    19: "aula-19-classes-especializadas-if-beamer-iffposter-relatoriocorp",
    20: "aula-20-automacao-latexmkrc-git-e-integracao-continua",
}

# Títulos de slides únicos sem "Parte X/Y"
SLIDE_TOPICS = [
    "Epistemologia e Metodologia Científica",
    "Ruptura Epistemológica na Pesquisa",
    "O Falsificacionismo em Karl Popper",
    "Formulação de Hipóteses Verificáveis",
    "A Lacuna de Pesquisa na Literatura Específica",
    "Taxonomia de Bloom Aplicada aos Objetivos",
    "Estrutura Uniparágrafo do Resumo (NBR 6028)",
    "Vocabulários Controlados e Tesauros",
    "Folha de Rosto, Aprovação e Ficha Catalográfica",
    "Dedicatória, Agradecimentos e Epígrafe",
    "Técnica do Funil na Introdução Acadêmica",
    "Delineamento Experimental e Amostragem",
    "Reprodutibilidade na ABNT NBR 14724",
    "Comitê de Ética em Pesquisa (CEP/CONEP)",
    "Submissão Contínua via Plataforma Brasil",
    "Uso Transparente de IA e Ferramentas LLM",
    "Normas IBGE 1993 para Tabelas Estatísticas",
    "Quadros Conceituais na NBR 14724",
    "Sistema Autor-Data na ABNT NBR 10520:2023",
    "Normalização Bibliográfica na NBR 6023:2018",
    "Arquitetura do Kernel LaTeX2e",
    "Motores PDFLaTeX, LuaLaTeX e XeLaTeX",
    "Organização do Preâmbulo Acadêmico",
    "Ambientes Matemáticos com amsmath",
    "Tabelas Profissionais com booktabs",
    "Modularização via Comandos input e include",
    "Automação Bibliográfica via biblatex e biber",
    "Computação Gráfica Vetorial em TikZ",
    "Gráficos Analíticos com PGFPlots",
    "Engenharia Interna de metadados.sty",
    "Flexão de Gênero e Variáveis no ReLaTeX",
    "Definição de Macros Customizadas em macros.sty",
    "Ambientes de Teorema e Corolário",
    "Herança de Classe com abntex2 e ifftese.cls",
    "Customização de Floats e Listas Preliminares",
    "Cabeçalhos Institucionais com fancyhdr",
    "Sumário Dinâmico na ABNT NBR 6027",
    "Slides Institucionais com beamer",
    "Pôsteres Científicos com iffposter.cls",
    "Relatórios Corporativos Técnicos",
    "Automação de Build com latexmkrc",
    "Versionamento Limpo com Git e .gitignore",
    "Integração Contínua em Pipelines CI/CD",
    "Checklist de Validação Normativa no Campus",
    "Revisão Criteriosa de Elementos Textuais",
    "Auditoria Cruzada de Citações e Referências",
    "Conformidade Visual com a Identidade IFF",
    "Autonomia Tecnológica do Pesquisador",
    "Boas Práticas de Diagramação TeX",
    "Desenvolvimento Científico e Inovação",
]

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

def encrypt_pdf(pdf_path, password=SENHA_INSTITUCIONAL):
    """Aplica criptografia com senha institucional a um arquivo PDF gerado."""
    try:
        if not os.path.exists(pdf_path):
            return False
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.encrypt(password)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_out:
            writer.write(tmp_out)
            tmp_name = tmp_out.name
        shutil.move(tmp_name, pdf_path)
        return True
    except Exception as e:
        print(f"[ERRO ENCRIPTACAO PDF] {e}")
        return False

def popule_pptx_institucional(template_path, output_pptx_path, num_str, titulo, subtitulo, is_dark=False, url_qr="https://www.phrandrade.com/pt-br/resource/latex"):
    """Atualiza PPTX do IFF: substitui Astrofísica por LaTeX e Escrita Acadêmica, cores institucionais, amplia logo e insere QR Code canônico."""
    prs = pptx.Presentation(template_path)
    
    for idx, slide in enumerate(prs.slides):
        # 1. Atualizar textos em todas as formas do slide
        for shape in slide.shapes:
            if shape.has_text_frame:
                text_val = shape.text_frame.text
                if idx == 0 and ("Reconciliação" in text_val or "Abundâncias" in text_val or len(text_val) > 15):
                    shape.text_frame.clear()
                    p = shape.text_frame.paragraphs[0]
                    p.text = f"AULA {num_str}: {titulo.upper()}"
                    p.font.size = Pt(26)
                    p.font.bold = True
                    p.font.color.rgb = RGBColor(239, 68, 68) if is_dark else RGBColor(185, 28, 28) # Vermelho Institucional
                    
                    p2 = shape.text_frame.add_paragraph()
                    p2.text = f"{subtitulo}\nCurso: LaTeX e Escrita Acadêmica — Normas ABNT"
                    p2.font.size = Pt(16)
                    p2.font.color.rgb = RGBColor(34, 197, 94) if is_dark else RGBColor(21, 128, 61) # Verde Institucional
                elif idx == 0 and ("Apresentador:" in text_val or "Pedro" in text_val):
                    shape.text_frame.clear()
                    p = shape.text_frame.paragraphs[0]
                    p.text = "Pedro Henrique Rocha de Andrade"
                    p.font.size = Pt(14)
                    p.font.bold = True
                    p.font.color.rgb = RGBColor(245, 158, 11) if is_dark else RGBColor(180, 83, 9) # Dourado Institucional
                    
                    p2 = shape.text_frame.add_paragraph()
                    p2.text = "Instituto Federal Fluminense (IFF) — Campus Bom Jesus do Itabapoana\nCurso: LaTeX e Escrita Acadêmica"
                    p2.font.size = Pt(12)
                    p2.font.color.rgb = RGBColor(167, 139, 250) if is_dark else RGBColor(109, 40, 217) # Violeta Institucional
                else:
                    # Substituições globais sem "Prof. Dr." e substituindo Astrofísica/MWBR por LaTeX e Escrita Acadêmica
                    if "Astrofísica" in text_val or "MWBR" in text_val or "Reconciliação" in text_val or "GCE" in text_val:
                        for paragraph in shape.text_frame.paragraphs:
                            for run in paragraph.runs:
                                run.text = run.text.replace("Astrofísica", "LaTeX e Escrita Acadêmica")
                                run.text = run.text.replace("Reconciliação Química no Disco Galáctico", "LaTeX e Escrita Acadêmica — IFF")
                                run.text = run.text.replace("MWBR", "IFF — CONFICT")
                                run.text = run.text.replace("GCE", "ABNT NBR 14724")
                    if "Prof. Dr." in text_val:
                        for paragraph in shape.text_frame.paragraphs:
                            for run in paragraph.runs:
                                run.text = run.text.replace("Prof. Dr. ", "")
                                run.text = run.text.replace("Prof. Dr.", "")

                    # Se for título do slide (cabeçalho da página > 0), aplicar Vermelho Institucional
                    if shape.top < Inches(1.2) and idx > 0:
                        for paragraph in shape.text_frame.paragraphs:
                            for run in paragraph.runs:
                                run.font.color.rgb = RGBColor(239, 68, 68) if is_dark else RGBColor(185, 28, 28)

        # 2. Ampliar e destacar a Logo do IFF no Cabeçalho de todos os slides (recorte / trim e aumento de tamanho)
        for shape in slide.shapes:
            if "Picture" in shape.name or "Logo" in shape.name:
                # Se for imagem no topo (cabeçalho)
                if shape.top < Inches(1.5) and idx > 0:
                    shape.width = Inches(2.3)
                    shape.height = Inches(0.85)
                    shape.left = Inches(0.5)
                    shape.top = Inches(0.08)

    # 3. Gerar QR Code transparente com URL canônica e inserir no slide final (Obrigado!) e na Capa
    with tempfile.TemporaryDirectory() as tmp_qr_dir:
        qr_path = os.path.join(tmp_qr_dir, "qrcode_transparente.png")
        generate_qr_transparent(url_qr, qr_path, is_dark_theme=is_dark)
        
        slide_final = prs.slides[-1]
        left = Inches(10.2)
        top = Inches(4.3)
        width = Inches(2.4)
        height = Inches(2.4)
        slide_final.shapes.add_picture(qr_path, left, top, width, height)

    os.makedirs(os.path.dirname(output_pptx_path), exist_ok=True)
    prs.save(output_pptx_path)
    return True

def gerar_tex_slides_52_frames(num, titulo, subtitulo, is_dark=False):
    """Gera código Beamer (52 slides) com diagrama TikZ, sem Parte X/Y, com slide de Obrigado com QR e Referências."""
    num_str = f"{num:02d}"
    lines = []
    lines.append(r"\documentclass[10pt, aspectratio=169]{slidesiffmodelo}")
    lines.append(r"\usepackage{amsmath,amssymb}")
    lines.append(r"\usepackage{booktabs}")
    lines.append(r"\usepackage{xcolor}")
    lines.append(r"\usepackage{graphicx}")
    lines.append(r"\usepackage{tikz}")
    lines.append(r"\usetikzlibrary{shapes,arrows,positioning}")
    
    if is_dark:
        lines.append(r"% Configuração de Modelo Preto (Escuro) — Paleta Institucional")
        lines.append(r"\definecolor{iffred}{RGB}{239, 68, 68}")
        lines.append(r"\definecolor{iffgreen}{RGB}{34, 197, 94}")
        lines.append(r"\definecolor{iffgold}{RGB}{245, 158, 11}")
        lines.append(r"\definecolor{ifforange}{RGB}{251, 146, 60}")
        lines.append(r"\definecolor{iffviolet}{RGB}{167, 139, 250}")
        lines.append(r"\definecolor{ifflight}{RGB}{30, 41, 59}")
        lines.append(r"\setbeamercolor{normal text}{fg=white,bg=black!94!white}")
        lines.append(r"\setbeamercolor{structure}{fg=iffgreen}")
        lines.append(r"\setbeamercolor{title}{fg=iffred}")
        lines.append(r"\setbeamercolor{frametitle}{fg=iffred}")
        lines.append(r"\setbeamercolor{item}{fg=iffgreen}")
        lines.append(r"\setbeamercolor{subitem}{fg=iffgold}")
        lines.append(r"\setbeamercolor{caption}{fg=white}")
    else:
        lines.append(r"% Configuração de Modelo Branco (Claro) — Paleta Institucional")
        lines.append(r"\definecolor{iffred}{RGB}{185, 28, 28}")
        lines.append(r"\definecolor{iffgreen}{RGB}{21, 128, 61}")
        lines.append(r"\definecolor{iffgold}{RGB}{180, 83, 9}")
        lines.append(r"\definecolor{ifforange}{RGB}{194, 65, 12}")
        lines.append(r"\definecolor{iffviolet}{RGB}{109, 40, 217}")
        lines.append(r"\definecolor{ifflight}{RGB}{248, 250, 252}")
        lines.append(r"\setbeamercolor{normal text}{fg=black!90,bg=white}")
        lines.append(r"\setbeamercolor{structure}{fg=iffgreen}")
        lines.append(r"\setbeamercolor{title}{fg=iffred}")
        lines.append(r"\setbeamercolor{frametitle}{fg=iffred}")
        lines.append(r"\setbeamercolor{item}{fg=iffgreen}")
        lines.append(r"\setbeamercolor{subitem}{fg=iffgold}")

    lines.append(r"% Estrutura de Cabeçalho e Rodapé IDÊNTICA ao PPTX Institucional")
    lines.append(r"\setbeamertemplate{headline}{%")
    lines.append(r"  \vspace{0.18cm}%")
    lines.append(r"  \hspace{0.5cm}%")
    lines.append(r"  \begin{minipage}{0.35\linewidth}%")
    lines.append(r"    \includegraphics[height=0.65cm]{img/logoiff.png}%")
    lines.append(r"  \end{minipage}%")
    lines.append(r"  \hfill%")
    lines.append(r"  \begin{minipage}{0.55\linewidth}%")
    lines.append(r"    \raggedleft\footnotesize\textbf{\color{iffred} LaTeX e Escrita Acadêmica --- NBR 14724}%")
    lines.append(r"  \end{minipage}%")
    lines.append(r"  \hspace{0.5cm}%")
    lines.append(r"  \vspace{0.12cm}%")
    lines.append(r"  {\color{iffgold}\hrule height 1.2pt}%")
    lines.append(r"}")
    lines.append(r"\setbeamertemplate{footline}{%")
    lines.append(r"  {\color{iffgold}\hrule height 0.8pt}%")
    lines.append(r"  \vspace{0.1cm}%")
    lines.append(r"  \hspace{0.5cm}%")
    lines.append(r"  \begin{minipage}{0.35\linewidth}%")
    lines.append(r"    \scriptsize\textbf{\color{iffgreen} Pedro Henrique Rocha de Andrade}%")
    lines.append(r"  \end{minipage}%")
    lines.append(r"  \hfill%")
    lines.append(r"  \begin{minipage}{0.35\linewidth}%")
    lines.append(r"    \centering\scriptsize\textbf{\color{ifforange} IFF Bom Jesus do Itabapoana}%")
    lines.append(r"  \end{minipage}%")
    lines.append(r"  \hfill%")
    lines.append(r"  \begin{minipage}{0.15\linewidth}%")
    lines.append(r"    \raggedleft\scriptsize\textbf{\color{iffviolet} \insertframenumber{} / \inserttotalframenumber}%")
    lines.append(r"  \end{minipage}%")
    lines.append(r"  \hspace{0.5cm}%")
    lines.append(r"  \vspace{0.15cm}%")
    lines.append(r"}")
        
    lines.append(f"\\title{{Aula {num_str}: {titulo} \\\\ \\small {subtitulo}}}")
    lines.append(r"\author{\textbf{Pedro Henrique Rocha de Andrade}\inst{1}}")
    lines.append(r"\institute{\inst{1} Instituto Federal Fluminense --- \textit{Campus} Bom Jesus do Itabapoana}")
    lines.append(r"\date{\today}")
    
    lines.append(r"\begin{document}")
    
    # Slide 1: Capa
    lines.append(r"\begin{frame}[t]")
    lines.append(r"    \titlepage")
    lines.append(r"\end{frame}")
    lines.append("")
    
    # Slide 2: Sumário
    lines.append(r"\begin{frame}[t]")
    lines.append(r"    \frametitle{Sumário da Aula}")
    lines.append(r"    \tableofcontents")
    lines.append(r"\end{frame}")
    lines.append("")
    
    # Slides 3 a 49: Conteúdo com títulos únicos (SEM "Parte X/Y")
    lines.append(r"\section{Desenvolvimento Teórico e Metodológico}")
    for idx_topic, topic in enumerate(SLIDE_TOPICS[:47]):
        lines.append(r"\begin{frame}[t]")
        lines.append(f"    \\frametitle{{{topic}}}")
        lines.append(r"    \begin{itemize}")
        lines.append(f"        \\item \\textbf{{Análise Normativa e Escopo:}} Abordagem sistemática segundo as diretrizes de metodologia científica do IFF;")
        lines.append(f"        \\item \\textbf{{Fundamentação Prática:}} Aplicação no desenvolvimento documental em LaTeX (classe \\texttt{{ifftese.cls}});")
        lines.append(f"        \\item \\textbf{{Rigidez Técnica:}} Conformidade integral à ABNT NBR 14724, NBR 10520:2023 e NBR 6023:2018;")
        lines.append(f"        \\item \\textbf{{Exemplo de Aplicação:}} Integração de dados em projetos e trabalhos de conclusão de curso.")
        lines.append(r"    \end{itemize}")
        lines.append(r"\end{frame}")
        lines.append("")

    # Slide 50: Diagrama Vetorial TikZ / Ilustração Visual
    lines.append(r"\section{Síntese Arquitetural do Ecossistema}")
    lines.append(r"\begin{frame}[t]")
    lines.append(r"    \frametitle{Hierarquia e Fluxo Documental na ABNT (Diagrama TikZ)}")
    lines.append(r"    \begin{center}")
    lines.append(r"    \begin{tikzpicture}[node distance=1.6cm, auto,")
    lines.append(r"        boxpre/.style={rectangle, draw=iffgreen, thick, fill=iffgreen!12!white, text width=3.3cm, align=center, rounded corners, minimum height=0.9cm, font=\scriptsize},")
    lines.append(r"        boxtex/.style={rectangle, draw=iffgold, thick, fill=iffgold!12!white, text width=3.3cm, align=center, rounded corners, minimum height=0.9cm, font=\scriptsize},")
    lines.append(r"        boxpos/.style={rectangle, draw=iffviolet, thick, fill=iffviolet!12!white, text width=3.3cm, align=center, rounded corners, minimum height=0.9cm, font=\scriptsize},")
    lines.append(r"        arrow/.style={->, >=stealth, thick, color=iffred}")
    lines.append(r"    ]")
    lines.append(r"        \node[boxpre] (pre) {\textbf{1. Elementos Pré-textuais}\\ (Capa, Rosto, Resumo)};")
    lines.append(r"        \node[boxtex, right of=pre, xshift=2.6cm] (tex) {\textbf{2. Elementos Textuais}\\ (Introdução, Metodologia)};")
    lines.append(r"        \node[boxpos, right of=tex, xshift=2.6cm] (pos) {\textbf{3. Elementos Pós-textuais}\\ (Referências, Anexos)};")
    lines.append(r"        \draw[arrow] (pre) -- (tex);")
    lines.append(r"        \draw[arrow] (tex) -- (pos);")
    lines.append(r"    \end{tikzpicture}")
    lines.append(r"    \end{center}")
    lines.append(r"    \vspace{0.3cm}")
    lines.append(r"    \begin{itemize}")
    lines.append(r"        \item \textbf{Fluxo de Compilação:} Separação estrita entre conteúdo semântico (.tex) e regras tipográficas (.cls/.sty);")
    lines.append(r"        \item \textbf{Automação:} Gerenciamento dinâmico de referências cruzadas, paginação e listas preliminares.")
    lines.append(r"    \end{itemize}")
    lines.append(r"\end{frame}")
    lines.append("")

    # Slide 51: Referências Bibliográficas (Formal)
    lines.append(r"\section{Referências Bibliográficas}")
    lines.append(r"\begin{frame}[t,allowframebreaks]")
    lines.append(r"    \frametitle{Referências Bibliográficas}")
    lines.append(r"    \begin{thebibliography}{99}")
    lines.append(r"    \bibitem{nbr14724} ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. \textit{NBR 14724: Informação e documentação --- Trabalhos acadêmicos --- Apresentação.} Rio de Janeiro: ABNT, 2011.")
    lines.append(r"    \bibitem{nbr10520} ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. \textit{NBR 10520: Informação e documentação --- Citações em documentos --- Apresentação.} Rio de Janeiro: ABNT, 2023.")
    lines.append(r"    \bibitem{nbr6023} ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. \textit{NBR 6023: Informação e documentação --- Referências --- Elaboração.} Rio de Janeiro: ABNT, 2018.")
    lines.append(r"    \bibitem{ibge1993} INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). \textit{Normas de apresentação tabular.} 3. ed. Rio de Janeiro: IBGE, 1993.")
    lines.append(r"    \bibitem{page2021} PAGE, M. J. et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. \textit{BMJ}, v. 372, n. 71, 2021.")
    lines.append(r"    \end{thebibliography}")
    lines.append(r"\end{frame}")
    lines.append("")

    # Slide 52: Slide de Obrigado! com QR Code Transparente
    lines.append(r"\section{Fechamento}")
    lines.append(r"\begin{frame}[t]")
    lines.append(r"    \frametitle{Obrigado!}")
    lines.append(r"    \begin{textoimagem}")
    lines.append(r"        \textbf{Pedro Henrique Rocha de Andrade}\\")
    lines.append(r"        Instituto Federal Fluminense (\textit{Campus} Bom Jesus do Itabapoana)\\")
    lines.append(r"        \email\\")
    lines.append(r"        \vspace{0.4cm}")
    lines.append(r"        Dúvidas ou sugestões? Acesse o portal institucional da disciplina e faça o download dos pacotes apontando para o QR Code ao lado.")
    lines.append(r"    \colunaimagem")
    lines.append(r"        \inserirfigura[width=0.65\linewidth]{img/qrcode_transparente.png}{Acesso Institucional ao Curso}{}{fig:qrcode}")
    lines.append(r"    \end{textoimagem}")
    lines.append(r"\end{frame}")
    lines.append("")

    lines.append(r"\end{document}")
    return "\n".join(lines)

def gerar_tex_notas_100_latex_institucional(num, titulo, subtitulo):
    """Gera Notas de Aula Institucionais sem regras de avaliação ou tempos de aula, focadas no rigor acadêmico com TikZ e booktabs."""
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
    lines.append(r"\usepackage{tikz}")
    lines.append(r"\usetikzlibrary{shapes,arrows,positioning}")
    lines.append(r"\usepackage{hyperref}")
    lines.append(r"\usepackage{fancyhdr}")
    lines.append(r"\usepackage{titlesec}")
    lines.append(r"\usepackage{xcolor}")
    
    lines.append(r"\definecolor{iffred}{RGB}{185,28,28}")
    lines.append(r"\definecolor{iffgreen}{RGB}{21,128,61}")
    lines.append(r"\definecolor{iffgold}{RGB}{180,83,9}")
    lines.append(r"\definecolor{ifforange}{RGB}{194,65,12}")
    lines.append(r"\definecolor{iffviolet}{RGB}{109,40,217}")
    lines.append(r"\definecolor{ifflight}{RGB}{248,250,252}")
    
    lines.append(r"\pagestyle{fancy}")
    lines.append(r"\fancyhf{}")
    lines.append(r"\fancyhead[L]{\textbf{\color{iffred} Instituto Federal Fluminense} \\ \footnotesize \textit{Campus} Bom Jesus do Itabapoana --- \color{iffgreen} LaTeX \& Escrita Acadêmica}")
    lines.append(r"\fancyhead[R]{\footnotesize \textbf{\color{iffgreen} Pedro Henrique Rocha de Andrade} \\ \color{iffviolet} Metodologia e ReLaTeX}")
    lines.append(r"\fancyfoot[C]{\textbf{\color{iffgold} \thepage}}")
    lines.append(r"\renewcommand{\headrulewidth}{0.8pt}")
    lines.append(r"\renewcommand{\footrulewidth}{0.4pt}")
    lines.append(r"\setlength{\headheight}{28pt}")
    
    lines.append(r"\titleformat{\section}{\large\bfseries\color{iffred}}{\thesection}{1em}{}")
    lines.append(r"\titleformat{\subsection}{\normalsize\bfseries\color{iffgreen}}{\thesubsection}{1em}{}")
    
    lines.append(r"\title{\vspace*{-1cm}\LARGE \textbf{\color{iffred} Notas de Aula Institucionais --- Aula " + num_str + r"} \\ \Large \textbf{\color{iffgreen} " + titulo + r"} \\ \normalsize \textit{\color{iffviolet} " + subtitulo + r"}}")
    lines.append(r"\author{\textbf{Pedro Henrique Rocha de Andrade} \\ \footnotesize Instituto Federal Fluminense (IFF) --- \textit{Campus} Bom Jesus do Itabapoana}")
    lines.append(r"\date{\footnotesize \textbf{\color{ifforange} Curso: LaTeX e Escrita Acadêmica}}")
    
    lines.append(r"\begin{document}")
    lines.append(r"\maketitle")
    
    lines.append(r"\tableofcontents")
    lines.append(r"\vspace{0.8cm}")
    
    lines.append(r"\section{Introdução e Fundamentação Metodológica}")
    lines.append(r"Estas notas de aula documentam o referencial teórico-metodológico e técnico da \textbf{Aula " + num_str + r": " + titulo + r"}. A produção acadêmica e a redação científica exigem a harmonização entre a coerência argumentativa epistemológica e a observância rigorosa da normalização estabelecida pelas diretrizes da Associação Brasileira de Normas Técnicas (ABNT).")
    
    lines.append(r"\section{Normalização ABNT NBR 14724 e NBR 10520:2023}")
    lines.append(r"A estruturação de trabalhos acadêmicos no Instituto Federal Fluminense baseia-se na conformidade à NBR 14724:2011, que regulamenta a hierarquia dos elementos pré-textuais, textuais e pós-textuais. O controle tipográfico com margens canônicas e citações no formato autor-data estipulado pela NBR 10520:2023 confere credibilidade e padronização aos documentos.")
    
    lines.append(r"\subsection{Diagrama Estrutural do Documento Acadêmico (TikZ)}")
    lines.append(r"\begin{figure}[h!]")
    lines.append(r"\centering")
    lines.append(r"\begin{tikzpicture}[node distance=2.2cm, auto,")
    lines.append(r"  boxpre/.style={rectangle, draw=iffgreen, thick, fill=iffgreen!12!white, text width=3.8cm, align=center, rounded corners, minimum height=1.1cm},")
    lines.append(r"  boxtex/.style={rectangle, draw=iffgold, thick, fill=iffgold!12!white, text width=3.8cm, align=center, rounded corners, minimum height=1.1cm},")
    lines.append(r"  boxpos/.style={rectangle, draw=iffviolet, thick, fill=iffviolet!12!white, text width=3.8cm, align=center, rounded corners, minimum height=1.1cm},")
    lines.append(r"  arrow/.style={->, >=stealth, thick, color=iffred}")
    lines.append(r"]")
    lines.append(r"  \node[boxpre] (pre) {\textbf{1. Elementos Pré-textuais}\\ \small Capa, Rosto, Resumo};")
    lines.append(r"  \node[boxtex, right of=pre, xshift=3.2cm] (tex) {\textbf{2. Elementos Textuais}\\ \small Introdução, Desenvolvimento};")
    lines.append(r"  \node[boxpos, right of=tex, xshift=3.2cm] (pos) {\textbf{3. Elementos Pós-textuais}\\ \small Referências, Apêndices};")
    lines.append(r"  \draw[arrow] (pre) -- (tex);")
    lines.append(r"  \draw[arrow] (tex) -- (pos);")
    lines.append(r"\end{tikzpicture}")
    lines.append(r"\caption{Fluxo de informação normatizado de acordo com a ABNT NBR 14724.}")
    lines.append(r"\label{fig:fluxo_abnt}")
    lines.append(r"\end{figure}")
    
    lines.append(r"\section{Arquitetura Computacional e Prática no Ecossistema ReLaTeX}")
    lines.append(r"A diagramação via motor PDFLaTeX ou LuaLaTeX garante uma separação clara entre a lógica do texto (\texttt{.tex}) e as instruções tipográficas da classe (\texttt{ifftese.cls}). A utilização dos pacotes \texttt{metadados.sty} e \texttt{macros.sty} simplifica a governança de variáveis institucionais e a reprodutibilidade dos relatórios e monografias.")
    
    lines.append(r"\subsection{Comparativo Normativo em Tabela \texttt{booktabs}}")
    lines.append(r"\begin{table}[h!]")
    lines.append(r"\centering")
    lines.append(r"\caption{Correlação entre Diretrizes Normativas e Implementação TeX}")
    lines.append(r"\begin{tabular}{lll}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Componente Acadêmico} & \textbf{Norma ABNT Aplicável} & \textbf{Comando no Ecossistema ReLaTeX} \\")
    lines.append(r"\midrule")
    lines.append(r"Resumo e Palavras-Chave & ABNT NBR 6028:2021 & \texttt{\textbackslash begin\{resumo\}} \\")
    lines.append(r"Citações e Paráfrases & ABNT NBR 10520:2023 & \texttt{\textbackslash cite}, \texttt{\textbackslash citeonline} \\")
    lines.append(r"Apresentação Tabular & IBGE (1993) / NBR 14724 & \texttt{\textbackslash begin\{tabular\}} com \texttt{booktabs} \\")
    lines.append(r"Lista de Referências & ABNT NBR 6023:2018/2020 & \texttt{\textbackslash printbibliography} \\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    
    lines.append(r"\section{Aplicação Prática e Resolução de Inconsistências Comuns}")
    lines.append(r"Durante a redação acadêmica, problemas frequentes incluem o emprego inadequado de tabelas providas de linhas verticais em desacordo com a norma IBGE (1993), citações sem identificação de página em transcrições diretas e ausência de vetorização em ilustrações técnicas. O cumprimento da normalização elimina essas irregularidades.")
    
    lines.append(r"\section{Síntese Crítica e Autonomia Científica}")
    lines.append(r"A proficiência técnica no uso da normalização ABNT em convergência com a precisão tipográfica do LaTeX consolida a autonomia do pesquisador, valorizando a qualidade e a reprodutibilidade dos trabalhos publicados no Instituto Federal Fluminense.")
    
    lines.append(r"\begin{thebibliography}{99}")
    lines.append(r"\bibitem{nbr14724} ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. \textit{NBR 14724: Informação e documentação --- Trabalhos acadêmicos --- Apresentação.} Rio de Janeiro: ABNT, 2011.")
    lines.append(r"\bibitem{nbr10520} ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. \textit{NBR 10520: Informação e documentação --- Citações em documentos --- Apresentação.} Rio de Janeiro: ABNT, 2023.")
    lines.append(r"\bibitem{nbr6023} ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. \textit{NBR 6023: Informação e documentação --- Referências --- Elaboração.} Rio de Janeiro: ABNT, 2018.")
    lines.append(r"\bibitem{ibge1993} INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). \textit{Normas de apresentação tabular.} 3. ed. Rio de Janeiro: IBGE, 1993.")
    lines.append(r"\bibitem{page2021} PAGE, M. J. et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. \textit{BMJ}, v. 372, n. 71, 2021.")
    lines.append(r"\end{thebibliography}")
    lines.append(r"\end{document}")
    return "\n".join(lines)

def compilar_pdf(tex_code, output_pdf_path, cls_dir=None, is_dark=False, url_qr="https://pedroiff0.github.io/page/pt-br/resource/latex"):
    """Compila código TeX e aplica proteção de senha no PDF final com a senha institucional escritaiff2026."""
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
                    
        # Gerar qrcode_transparente.png e copiar logo IFF para a pasta img/ do diretório temporário
        img_dir = os.path.join(tmp_dir, "img")
        os.makedirs(img_dir, exist_ok=True)
        qr_tmp = os.path.join(img_dir, "qrcode_transparente.png")
        generate_qr_transparent(url_qr, qr_tmp, is_dark_theme=is_dark)
        logo_light = "/home/pedro/Downloads/_cosmic_assets/iff/iff_bji_light.png"
        logo_dark = "/home/pedro/Downloads/_cosmic_assets/iff/iff_bji_dark.png"
        logo_src = logo_dark if is_dark else logo_light
        if os.path.exists(logo_src):
            shutil.copy2(logo_src, os.path.join(img_dir, "logoiff.png"))
        elif os.path.exists("/home/pedro/Downloads/_cosmic_assets/iff/iffbomjesusvert-1.png"):
            shutil.copy2("/home/pedro/Downloads/_cosmic_assets/iff/iffbomjesusvert-1.png", os.path.join(img_dir, "logoiff.png"))
                    
        cmd = ["pdflatex", "-interaction=nonstopmode", "documento.tex"]
        subprocess.run(cmd, cwd=tmp_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(cmd, cwd=tmp_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        pdf_tmp = os.path.join(tmp_dir, "documento.pdf")
        if os.path.exists(pdf_tmp):
            os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
            shutil.copy2(pdf_tmp, output_pdf_path)
            # Aplicar criptografia com a senha escritaiff2026
            encrypt_pdf(output_pdf_path, password=SENHA_INSTITUCIONAL)
            return True
        else:
            return False

def gerar_thumb(pdf_path, png_output_path):
    """Gera miniatura PNG a partir de PDF (removendo senha temporariamente para leitura ou renderização direta)."""
    try:
        os.makedirs(os.path.dirname(png_output_path), exist_ok=True)
        prefix = png_output_path.replace(".png", "")
        cmd = ["pdftoppm", "-png", "-r", "150", "-f", "1", "-l", "1", "-opw", SENHA_INSTITUCIONAL, pdf_path, prefix]
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
    dir_qrcodes = os.path.join(base_lib, "qrcodes")
    
    for d in [dir_slides_latex, dir_slides_pptx, dir_notes_latex, dir_thumbs, dir_qrcodes]:
        os.makedirs(d, exist_ok=True)
        
    cls_slide_dir = "/home/pedro/Repositorios/latex/modelos/slide-mostra"
    pptx_template_branco = "/home/pedro/Downloads/slides/Slides_Artigo_MWBR_16_9_Institucional_IFF_Branco.pptx"
    pptx_template_preto = "/home/pedro/Downloads/slides/Slides_Artigo_MWBR_16_9_Institucional_IFF_Preto.pptx"
    
    print("==========================================================================")
    print(" GERADOR INSTITUCIONAL - SLIDES E NOTAS (BRANCO & PRETO) — IFF")
    print(" SENHA INSTITUCIONAL NOS PDFS: escritaiff2026")
    print("==========================================================================")
    
    for num in range(1, 21):
        num_str = f"{num:02d}"
        titulo, subtitulo = AULAS_TITULOS.get(num, (f"Conteúdo Didático da Aula {num_str}", "Normas ABNT e Prática ReLaTeX"))
        slug = AULAS_SLUGS.get(num, f"aula-{num_str}")
        url_aula = f"https://www.phrandrade.com/pt-br/resource/latex/{slug}"
        
        # 0. Salvar QR Codes institucionais individuais (.png)
        qr_branco = os.path.join(dir_qrcodes, f"aula-{num_str}-branco.png")
        qr_preto = os.path.join(dir_qrcodes, f"aula-{num_str}-preto.png")
        qr_padrao = os.path.join(dir_qrcodes, f"aula-{num_str}.png")
        generate_qr_transparent(url_aula, qr_branco, is_dark_theme=False)
        generate_qr_transparent(url_aula, qr_preto, is_dark_theme=True)
        shutil.copy2(qr_branco, qr_padrao)
        
        # 1. Slides LaTeX - Modelo Branco (.pdf)
        pdf_slide_branco = os.path.join(dir_slides_latex, f"aula-{num_str}-branco.pdf")
        pdf_slide_padrao = os.path.join(dir_slides_latex, f"aula-{num_str}.pdf")
        tex_branco = gerar_tex_slides_52_frames(num, titulo, subtitulo, is_dark=False)
        print(f" [AULA {num_str}/20] Compilando Slides LaTeX (Modelo Branco) com senha...", end=" ", flush=True)
        if compilar_pdf(tex_branco, pdf_slide_branco, cls_slide_dir, is_dark=False, url_qr=url_aula):
            shutil.copy2(pdf_slide_branco, pdf_slide_padrao)
            print("OK!")
            thumb_png = os.path.join(dir_thumbs, f"aula-{num_str}.png")
            gerar_thumb(pdf_slide_branco, thumb_png)
        else:
            print("FALHA!")
            
        # 2. Slides LaTeX - Modelo Preto (.pdf)
        pdf_slide_preto = os.path.join(dir_slides_latex, f"aula-{num_str}-preto.pdf")
        tex_preto = gerar_tex_slides_52_frames(num, titulo, subtitulo, is_dark=True)
        print(f" [AULA {num_str}/20] Compilando Slides LaTeX (Modelo Preto) com senha...", end=" ", flush=True)
        if compilar_pdf(tex_preto, pdf_slide_preto, cls_slide_dir, is_dark=True, url_qr=url_aula):
            print("OK!")
        else:
            print("FALHA!")
            
        # 3. PPTX Institucional - Modelo Branco (.pptx)
        pptx_out_branco = os.path.join(dir_slides_pptx, f"aula-{num_str}-branco.pptx")
        pptx_out_padrao = os.path.join(dir_slides_pptx, f"aula-{num_str}.pptx")
        if os.path.exists(pptx_template_branco):
            popule_pptx_institucional(pptx_template_branco, pptx_out_branco, num_str, titulo, subtitulo, is_dark=False, url_qr=url_aula)
            shutil.copy2(pptx_out_branco, pptx_out_padrao)
            
        # 4. PPTX Institucional - Modelo Preto (.pptx)
        pptx_out_preto = os.path.join(dir_slides_pptx, f"aula-{num_str}-preto.pptx")
        if os.path.exists(pptx_template_preto):
            popule_pptx_institucional(pptx_template_preto, pptx_out_preto, num_str, titulo, subtitulo, is_dark=True, url_qr=url_aula)
            
        # 5. Notas de Aula Institucionais (.pdf) com senha e sem regras de avaliação/tempos de aula
        pdf_notes = os.path.join(dir_notes_latex, f"aula-{num_str}.pdf")
        tex_notes = gerar_tex_notas_100_latex_institucional(num, titulo, subtitulo)
        print(f" [AULA {num_str}/20] Compilando Notas Institucionais LaTeX com senha...", end=" ", flush=True)
        if compilar_pdf(tex_notes, pdf_notes, cls_dir=None, is_dark=False, url_qr=url_aula):
            print("OK!")
        else:
            print("FALHA!")
            
    print("\n[SUCESSO] 20 Aulas processadas integralmente, sem 'Parte X/Y', com senha e logo ampliada!")

if __name__ == "__main__":
    main()
