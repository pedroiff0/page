import re

with open('scripts/gerar_slides_e_notas.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update the QR code location in LaTeX Beamer Capa
qr_old = r"\begin{tikzpicture}[remember picture, overlay]\n  \node[anchor=south east, xshift=-0.5cm, yshift=0.5cm] at (current page.south east) {\includegraphics[width=2.5cm]{img/qrcode_transparente.png}};\n\end{tikzpicture}"
qr_new = r"\begin{tikzpicture}[remember picture, overlay]\n  \node[anchor=east, xshift=-1cm, yshift=1.5cm] at (current page.east) {\includegraphics[width=2.5cm]{img/qrcode_transparente.png}};\n\end{tikzpicture}"
code = code.replace(qr_old, qr_new)

# 2. Add iffblue color definition
code = code.replace(r"\definecolor{iffgreen}{RGB}{21, 128, 61}", r"\definecolor{iffgreen}{RGB}{21, 128, 61}\n        \definecolor{iffblue}{RGB}{37, 99, 235}")
code = code.replace(r"\definecolor{iffgreen}{RGB}{34, 197, 94}", r"\definecolor{iffgreen}{RGB}{34, 197, 94}\n        \definecolor{iffblue}{RGB}{96, 165, 250}")

# 3. Replace the SLIDE_TOPICS[:47] static loop with dynamic slides_data loop
tex_slides_loop_old = r"""    lines.append(r"\\section{Desenvolvimento Teórico e Metodológico}")
    for idx_topic, topic in enumerate(SLIDE_TOPICS\[:47\]):
        lines.append(r"\\begin{frame}\[t\]")
        lines.append(f"    \\\\frametitle{{{topic}}}")
        lines.append(r"    \\begin{itemize}")
        lines.append(f"        \\\\item \\\\textbf{{Análise Normativa e Escopo:}} Abordagem sistemática segundo as diretrizes de metodologia científica do IFF;")
        lines.append(f"        \\\\item \\\\textbf{{Fundamentação Prática:}} Aplicação no desenvolvimento documental em LaTeX (classe \\\\texttt{{ifftese.cls}});")
        lines.append(f"        \\\\item \\\\textbf{{Rigidez Técnica:}} Conformidade integral à ABNT NBR 14724, NBR 10520:2023 e NBR 6023:2018;")
        lines.append(f"        \\\\item \\\\textbf{{Exemplo de Aplicação:}} Integração de dados em projetos e trabalhos de conclusão de curso.")
        lines.append(r"    \\end{itemize}")
        lines.append(r"\\end{frame}")
        lines.append("")"""

tex_slides_loop_new = r"""    lines.append(r"\section{Desenvolvimento Teórico e Metodológico}")
    slides_data = extract_slides_from_md(num_str)
    for idx_topic, sdata in enumerate(slides_data):
        lines.append(r"\begin{frame}[t]")
        lines.append(f"    \\frametitle{{\\color{{iffgold}}{sdata['title']}}}")
        lines.append(r"    \begin{itemize}")
        for j, item in enumerate(sdata['items']):
            if '[AZUL]' in item:
                item_text = item.replace('[AZUL]', '').strip()
                lines.append(f"        \\item \\textcolor{{iffblue}}{{\\textbf{{[Vale Lembrar]}} {item_text}}}")
            elif j % 3 == 0:
                lines.append(f"        \\item \\textcolor{{iffgreen}}{{\\textbf{{[Importante]}} {item}}}")
            elif j % 3 == 1:
                lines.append(f"        \\item \\textcolor{{iffviolet}}{{\\textbf{{[Para a Prova]}} {item}}}")
            else:
                lines.append(f"        \\item {item}")
        lines.append(r"    \end{itemize}")
        lines.append(r"\end{frame}")
        lines.append("")"""

code = re.sub(tex_slides_loop_old, tex_slides_loop_new, code, flags=re.DOTALL)

with open('scripts/gerar_slides_e_notas.py', 'w', encoding='utf-8') as f:
    f.write(code)
