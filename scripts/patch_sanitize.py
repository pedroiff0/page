import re

with open('scripts/gerar_slides_e_notas.py', 'r', encoding='utf-8') as f:
    code = f.read()

funcs = """def latex_escape(text):
    math_blocks = re.findall(r'\\$.*?\\$', text)
    for i, m in enumerate(math_blocks): text = text.replace(m, f"@@MATH{i}@@")
    text = text.replace('%', r'\\%').replace('&', r'\\&').replace('#', r'\\#').replace('_', r'\\_')
    text = re.sub(r'\\*\\*(.*?)\\*\\*', r'\\\\textbf{\\1}', text)
    text = re.sub(r'\\*(.*?)\\*', r'\\\\textit{\\1}', text)
    text = re.sub(r'`(.*?)`', r'\\\\texttt{\\1}', text)
    for i, m in enumerate(math_blocks): text = text.replace(f"@@MATH{i}@@", m)
    return text

def pptx_clean(text):
    text = re.sub(r'\\*\\*(.*?)\\*\\*', r'\\1', text)
    text = re.sub(r'\\*(.*?)\\*', r'\\1', text)
    text = re.sub(r'`(.*?)`', r'\\1', text)
    return text

def extract_slides_from_md"""
code = code.replace("def extract_slides_from_md", funcs)

old_tex_item = """        for j, item in enumerate(sdata['items']):
            if '[AZUL]' in item:
                item_text = item.replace('[AZUL]', '').strip()
                lines.append(f"        \\\\item \\\\textcolor{{iffblue}}{{\\\\textbf{{[Vale Lembrar]}} {item_text}}}")
            elif j % 3 == 0:
                lines.append(f"        \\\\item \\\\textcolor{{iffgreen}}{{\\\\textbf{{[Importante]}} {item}}}")
            elif j % 3 == 1:
                lines.append(f"        \\\\item \\\\textcolor{{iffviolet}}{{\\\\textbf{{[Para a Prova]}} {item}}}")
            else:
                lines.append(f"        \\\\item {item}")"""
new_tex_item = """        for j, item in enumerate(sdata['items']):
            item_clean = latex_escape(item)
            if '[AZUL]' in item_clean:
                item_text = item_clean.replace('[AZUL]', '').strip()
                lines.append(f"        \\\\item \\\\textcolor{{iffblue}}{{\\\\textbf{{[Vale Lembrar]}} {item_text}}}")
            elif j % 3 == 0:
                lines.append(f"        \\\\item \\\\textcolor{{iffgreen}}{{\\\\textbf{{[Importante]}} {item_clean}}}")
            elif j % 3 == 1:
                lines.append(f"        \\\\item \\\\textcolor{{iffviolet}}{{\\\\textbf{{[Para a Prova]}} {item_clean}}}")
            else:
                lines.append(f"        \\\\item {item_clean}")"""
code = code.replace(old_tex_item, new_tex_item)

old_pptx_item = """            for j, item in enumerate(sdata['items']):
                p = tf.add_paragraph()
                if '[AZUL]' in item:
                    item_text = item.replace('[AZUL]', '').strip()
                    p.text = f"[Vale Lembrar] {item_text}"
                    p.font.color.rgb = RGBColor(96, 165, 250) if is_dark else RGBColor(37, 99, 235)
                elif j % 3 == 0:
                    p.text = f"[Importante] {item}"
                    p.font.color.rgb = RGBColor(34, 197, 94) if is_dark else RGBColor(21, 128, 61)
                elif j % 3 == 1:
                    p.text = f"[Prova/Trabalho] {item}"
                    p.font.color.rgb = RGBColor(167, 139, 250) if is_dark else RGBColor(109, 40, 217)
                else:
                    p.text = item"""
new_pptx_item = """            for j, item in enumerate(sdata['items']):
                p = tf.add_paragraph()
                item_clean = pptx_clean(item)
                if '[AZUL]' in item_clean:
                    item_text = item_clean.replace('[AZUL]', '').strip()
                    p.text = f"[Vale Lembrar] {item_text}"
                    p.font.color.rgb = RGBColor(96, 165, 250) if is_dark else RGBColor(37, 99, 235)
                elif j % 3 == 0:
                    p.text = f"[Importante] {item_clean}"
                    p.font.color.rgb = RGBColor(34, 197, 94) if is_dark else RGBColor(21, 128, 61)
                elif j % 3 == 1:
                    p.text = f"[Prova/Trabalho] {item_clean}"
                    p.font.color.rgb = RGBColor(167, 139, 250) if is_dark else RGBColor(109, 40, 217)
                else:
                    p.text = item_clean"""
code = code.replace(old_pptx_item, new_pptx_item)

# ALSO add SENHA to PPTX?? Pedro said "O arquivo pptx tbm deve ter senha para baixar."
# But wait, python-pptx CANNOT encrypt PPTX files! We need a third-party tool like `msoffcrypto-tool`!
# Or we just use `zip` to zip it with a password? Pedro said "O arquivo pptx tbm deve ter senha para baixar." (Password to download, or password to open?). If he means password to open PPTX, `msoffcrypto` encrypts. But maybe we can just zip them with a password?
# Wait, I don't have python-msoffcrypto installed. Let's install it if we need it, or wait and see!
# We can use LibreOffice in headless mode: `libreoffice --headless --convert-to pptx:"Impress MS PowerPoint 2007 XML" --outdir . file.pptx` - wait, LibreOffice does not easily add password via CLI.
# The easiest is msoffcrypto-tool: `msoffcrypto-tool in.pptx out.pptx -p password`. Is it installed? Let's check!

with open('scripts/gerar_slides_e_notas.py', 'w', encoding='utf-8') as f:
    f.write(code)
