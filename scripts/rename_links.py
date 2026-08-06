import glob, os

files = glob.glob('content/pt-br/resource/latex/aula-*.md')
for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    if '.pptx)' in content:
        content = content.replace('.pptx)', '.zip)')
        with open(filepath, 'w') as f:
            f.write(content)
        print(f'Updated {filepath}')
