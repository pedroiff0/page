import os
import re
import yaml

SOURCE_DIR = "/home/cinzento/webpage"
DEST_DIR = "/home/cinzento/quartz-site/content"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def split_content(content):
    en_match = re.search(r'<div class="lang-en"[^>]*>(.*?)</div>', content, re.DOTALL)
    pt_match = re.search(r'<div class="lang-pt"[^>]*>(.*?)</div>', content, re.DOTALL)
    
    en_text = en_match.group(1).strip() if en_match else ""
    pt_text = pt_match.group(1).strip() if pt_match else ""
    
    # If no tags, assume both are the same (like blog posts maybe?)
    if not en_text and not pt_text:
        en_text = content.strip()
        pt_text = content.strip()
        
    return en_text, pt_text

def parse_frontmatter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1])
                return fm, parts[2]
            except Exception as e:
                pass
    return {}, content

def process_file(src_path, dest_rel_en, dest_rel_pt):
    with open(src_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()
    
    fm, body = parse_frontmatter(raw_content)
    en_body, pt_body = split_content(body)
    
    # Titles
    title_en = fm.get('title', {}).get('en', fm.get('title', '')) if isinstance(fm.get('title'), dict) else fm.get('title', '')
    title_pt = fm.get('title', {}).get('pt', fm.get('title', '')) if isinstance(fm.get('title'), dict) else fm.get('title', '')
    
    date = fm.get('date', '')
    
    def write_file(path, title, content):
        ensure_dir(os.path.dirname(path))
        with open(path, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(f'title: "{title}"\n')
            if date:
                f.write(f'date: {date}\n')
            f.write("---\n\n")
            f.write(content)

    en_path = os.path.join(DEST_DIR, "en", dest_rel_en)
    pt_path = os.path.join(DEST_DIR, "pt-br", dest_rel_pt)
    
    write_file(en_path, title_en, en_body)
    write_file(pt_path, title_pt, pt_body)

# Clean existing
import shutil
if os.path.exists(os.path.join(DEST_DIR, 'en')):
    shutil.rmtree(os.path.join(DEST_DIR, 'en'))
if os.path.exists(os.path.join(DEST_DIR, 'pt-br')):
    shutil.rmtree(os.path.join(DEST_DIR, 'pt-br'))

# 1. Pages
pages_map = {
    "about.md": ("index.md", "index.md"),
    "research.md": ("research/index.md", "pesquisa/index.md"),
    "publications.md": ("publications/index.md", "publicacoes/index.md"),
    "resources.md": ("resources/index.md", "recursos/index.md"),
    "media.md": ("media/index.md", "midia/index.md")
}

for src, (den, dpt) in pages_map.items():
    src_file = os.path.join(SOURCE_DIR, "_pages", src)
    if os.path.exists(src_file):
        process_file(src_file, den, dpt)

# 2. Research
res_dir = os.path.join(SOURCE_DIR, "_research")
if os.path.exists(res_dir):
    for f in os.listdir(res_dir):
        if f.endswith(".md"):
            name = f.split('-', 3)[-1] if re.match(r'\d{4}-\d{2}-\d{2}-', f) else f
            process_file(os.path.join(res_dir, f), f"research/{name}", f"pesquisa/{name}")

# 3. Publications
pub_dir = os.path.join(SOURCE_DIR, "_publications")
if os.path.exists(pub_dir):
    for f in os.listdir(pub_dir):
        if f.endswith(".md"):
            process_file(os.path.join(pub_dir, f), f"publications/{f}", f"publicacoes/{f}")

print("Migration completed.")
