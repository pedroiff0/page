import re

with open('scripts/gerar_slides_e_notas.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update signature of gerar_tex_slides_52_frames to receive url_qr
code = code.replace(
    'def gerar_tex_slides_52_frames(num, titulo, subtitulo, is_dark=False):',
    'def gerar_tex_slides_52_frames(num, titulo, subtitulo, is_dark=False, url_qr=""): '
)

# 2. Add QR Code Caption and Starry Night to Title Slide
old_title_slide = r"""    # Slide 1: Capa
    lines.append(r"\begin{frame}[t]")
    lines.append(r"    \titlepage")
    lines.append(r"    \begin{tikzpicture}[remember picture, overlay]")
    lines.append(r"      \node[anchor=east, xshift=-1cm, yshift=1.5cm] at (current page.east) {\includegraphics[width=2.5cm]{img/qrcode_transparente.png}};")
    lines.append(r"    \end{tikzpicture}")
    lines.append(r"\end{frame}")"""

new_title_slide = r"""    # Slide 1: Capa
    lines.append(r"\begin{frame}[t]")
    lines.append(r"    \begin{tikzpicture}[remember picture, overlay]")
    lines.append(r"      \node[opacity=0.15, at=(current page.center)] {\includegraphics[width=\paperwidth,height=\paperheight]{img/noite_estrelada.jpg}};")
    lines.append(r"    \end{tikzpicture}")
    lines.append(r"    \titlepage")
    lines.append(r"    \begin{tikzpicture}[remember picture, overlay]")
    lines.append(r"      \node[anchor=east, xshift=-1cm, yshift=1.5cm] (qr) at (current page.east) {\includegraphics[width=2.5cm]{img/qrcode_transparente.png}};")
    if url_qr:
        # Escape the URL for LaTeX display safely
        safe_url = url_qr.replace('%', '\\%').replace('#', '\\#').replace('_', '\\_')
        lines.append(f"      \\node[anchor=north, yshift=-0.1cm, font=\\tiny, color=gray] at (qr.south) {{{safe_url}}};")
    lines.append(r"    \end{tikzpicture}")
    lines.append(r"\end{frame}")"""
code = code.replace(old_title_slide, new_title_slide)

# 3. Add Starry Night to Final Slide
old_final_slide = r"""    # Slide 52: Encerramento
    lines.append(r"\begin{frame}[c]")
    lines.append(r"    \begin{center}")
    lines.append(r"        {\Huge \color{iffgold} \textbf{Obrigado!}} \\ \vspace{1cm}")
    lines.append(r"        {\large \color{iffgreen} \textbf{Prof. Dr. Pedro Henrique Rocha de Andrade}} \\ \vspace{0.5cm}")
    lines.append(r"        {\normalsize Instituto Federal Fluminense (IFF) --- \textit{Campus} Bom Jesus do Itabapoana}")
    lines.append(r"    \end{center}")
    lines.append(r"\end{frame}")"""

new_final_slide = r"""    # Slide 52: Encerramento
    lines.append(r"\begin{frame}[c]")
    lines.append(r"    \begin{tikzpicture}[remember picture, overlay]")
    lines.append(r"      \node[opacity=0.15, at=(current page.center)] {\includegraphics[width=\paperwidth,height=\paperheight]{img/noite_estrelada.jpg}};")
    lines.append(r"    \end{tikzpicture}")
    lines.append(r"    \begin{center}")
    lines.append(r"        {\Huge \color{iffgold} \textbf{Obrigado!}} \\ \vspace{1cm}")
    lines.append(r"        {\large \color{iffgreen} \textbf{Prof. Dr. Pedro Henrique Rocha de Andrade}} \\ \vspace{0.5cm}")
    lines.append(r"        {\normalsize Instituto Federal Fluminense (IFF) --- \textit{Campus} Bom Jesus do Itabapoana}")
    lines.append(r"    \end{center}")
    lines.append(r"\end{frame}")"""
code = code.replace(old_final_slide, new_final_slide)

# 4. Fix Logo IFF in header macro
old_logo = r'lines.append(r"    \includegraphics[height=0.65cm]{img/logoiff.png}%")'
new_logo = r'lines.append(r"    \includegraphics[trim=0 30 0 30, clip, height=0.85cm]{img/logoiff.png}%")'
code = code.replace(old_logo, new_logo)

# 5. Fix TikZ colors
old_tikz = r"""    lines.append(r"    \begin{tikzpicture}[node distance=1.6cm, auto,")
    lines.append(r"        boxpre/.style={rectangle, draw=iffgreen, thick, fill=iffgreen!12!white, text width=3.3cm, align=center, rounded corners, minimum height=0.9cm, font=\scriptsize},")
    lines.append(r"        boxtex/.style={rectangle, draw=iffgold, thick, fill=iffgold!12!white, text width=3.3cm, align=center, rounded corners, minimum height=0.9cm, font=\scriptsize},")
    lines.append(r"        boxpos/.style={rectangle, draw=iffviolet, thick, fill=iffviolet!12!white, text width=3.3cm, align=center, rounded corners, minimum height=0.9cm, font=\scriptsize},")
    lines.append(r"        arrow/.style={->, >=stealth, thick, color=iffred}")
    lines.append(r"    ]")"""

new_tikz = r"""    fill_shade = "!20!black" if is_dark else "!12!white"
    text_color = "white" if is_dark else "black"
    lines.append(r"    \begin{tikzpicture}[node distance=1.6cm, auto,")
    lines.append(f"        boxpre/.style={{rectangle, draw=iffgreen, thick, fill=iffgreen{fill_shade}, text={text_color}, text width=3.3cm, align=center, rounded corners, minimum height=0.9cm, font=\\scriptsize}},")
    lines.append(f"        boxtex/.style={{rectangle, draw=iffgold, thick, fill=iffgold{fill_shade}, text={text_color}, text width=3.3cm, align=center, rounded corners, minimum height=0.9cm, font=\\scriptsize}},")
    lines.append(f"        boxpos/.style={{rectangle, draw=iffviolet, thick, fill=iffviolet{fill_shade}, text={text_color}, text width=3.3cm, align=center, rounded corners, minimum height=0.9cm, font=\\scriptsize}},")
    lines.append(r"        arrow/.style={->, >=stealth, thick, color=iffred}")
    lines.append(r"    ]")"""
code = code.replace(old_tikz, new_tikz)

# 6. Copy Noite Estrelada inside compilar_pdf
old_copy = r"""        logo_src = logo_dark if is_dark else logo_light
        if os.path.exists(logo_src):
            shutil.copy2(logo_src, os.path.join(img_dir, "logoiff.png"))
        elif os.path.exists("/home/pedro/Downloads/_cosmic_assets/iff/iffbomjesusvert-1.png"):
            shutil.copy2("/home/pedro/Downloads/_cosmic_assets/iff/iffbomjesusvert-1.png", os.path.join(img_dir, "logoiff.png"))"""

new_copy = r"""        logo_src = logo_dark if is_dark else logo_light
        if os.path.exists(logo_src):
            shutil.copy2(logo_src, os.path.join(img_dir, "logoiff.png"))
        elif os.path.exists("/home/pedro/Downloads/_cosmic_assets/iff/iffbomjesusvert-1.png"):
            shutil.copy2("/home/pedro/Downloads/_cosmic_assets/iff/iffbomjesusvert-1.png", os.path.join(img_dir, "logoiff.png"))
            
        noite_src = "/home/pedro/Documentos/pesquisa/midias/noite_estrelada_original.jpg"
        if os.path.exists(noite_src):
            shutil.copy2(noite_src, os.path.join(img_dir, "noite_estrelada.jpg"))
        else:
            # Fallback mock file to avoid pdflatex error if missing
            with open(os.path.join(img_dir, "noite_estrelada.jpg"), "w") as f:
                f.write("")"""
code = code.replace(old_copy, new_copy)

with open('scripts/gerar_slides_e_notas.py', 'w', encoding='utf-8') as f:
    f.write(code)

