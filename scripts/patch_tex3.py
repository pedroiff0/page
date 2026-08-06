import re

with open('scripts/gerar_slides_e_notas.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Add QR to LaTeX Slide 1: Capa
old_capa = """    # Slide 1: Capa
    lines.append(r"\\begin{frame}[t]")
    lines.append(r"    \\titlepage")
    lines.append(r"\\end{frame}")"""
new_capa = """    # Slide 1: Capa
    lines.append(r"\\begin{frame}[t]")
    lines.append(r"    \\titlepage")
    lines.append(r"    \\begin{tikzpicture}[remember picture, overlay]")
    lines.append(r"      \\node[anchor=east, xshift=-1cm, yshift=1.5cm] at (current page.east) {\\includegraphics[width=2.5cm]{img/qrcode_transparente.png}};")
    lines.append(r"    \\end{tikzpicture}")
    lines.append(r"\\end{frame}")"""
code = code.replace(old_capa, new_capa)

# Add QR to LaTeX final slide
old_fim = """    # Slide 50: Obrigado
    lines.append(r"\\begin{frame}[t]")
    lines.append(r"    \\frametitle{\\color{iffgold}Obrigado!}")
    lines.append(r"    \\vspace{1cm}")
    lines.append(r"    \\centering")
    lines.append(r"    \\LARGE\\textbf{Dúvidas?}\\\\")
    lines.append(r"    \\vspace{0.5cm}")
    lines.append(r"    \\large Pedro Henrique Rocha de Andrade\\\\")
    lines.append(r"    \\normalsize E-mail: pedroiff0@gmail.com\\\\")
    lines.append(r"    \\normalsize \\url{https://www.phrandrade.com}")
    lines.append(r"\\end{frame}")"""
new_fim = """    # Slide Final: Obrigado
    lines.append(r"\\begin{frame}[t]")
    lines.append(r"    \\frametitle{\\color{iffgold}Obrigado!}")
    lines.append(r"    \\vspace{1cm}")
    lines.append(r"    \\centering")
    lines.append(r"    \\LARGE\\textbf{Dúvidas?}\\\\")
    lines.append(r"    \\vspace{0.5cm}")
    lines.append(r"    \\large Pedro Henrique Rocha de Andrade\\\\")
    lines.append(r"    \\normalsize E-mail: pedroiff0@gmail.com\\\\")
    lines.append(r"    \\normalsize \\url{https://www.phrandrade.com}")
    lines.append(r"    \\begin{tikzpicture}[remember picture, overlay]")
    lines.append(r"      \\node[anchor=south east, xshift=-1cm, yshift=1cm] at (current page.south east) {\\includegraphics[width=3.5cm]{img/qrcode_transparente.png}};")
    lines.append(r"    \\end{tikzpicture}")
    lines.append(r"\\end{frame}")"""
code = code.replace(old_fim, new_fim)

with open('scripts/gerar_slides_e_notas.py', 'w', encoding='utf-8') as f:
    f.write(code)
