# 🏛️ Template Oficial para Novos Cursos e Disciplinas (IFF Campus Bom Jesus)

Este diretório (`content/templates/ModeloCurso/`) é o **modelo padrão automatizado** desenvolvido para a criação ágil de novas disciplinas e formações ministradas pelo **Prof. Dr. Pedro Henrique Rocha de Andrade** no Instituto Federal Fluminense.

---

## 🚀 Como Criar um Novo Curso em 3 Passos

### 1. Clonar ou Copiar a Pasta do Modelo
Copie esta pasta para o local desejado dentro de `content/pt-br/resource/` (ou em `content/pt-br/resource/Engenharia de Computação/...`).

Exemplo:
```bash
cp -r content/templates/ModeloCurso content/pt-br/resource/novo-curso-exemplo
```

---

### 2. Adicionar as Aulas (`aula-XX-titulo.md`)
Dentro da nova pasta do curso, crie seus arquivos markdown de aula seguindo o padrão de nomenclatura:
- `aula-01-minha-primeira-aula.md`
- `aula-02-segunda-aula.md`
- `aula-03-terceira-aula.md`
- ...

> [!TIP] Estrutura do Arquivo de Aula
> Cada arquivo deve conter no frontmatter YAML `title: "Aula XX: Título da Lição"` e `publish: true`. O sistema reconhece automaticamente o número da aula e suas normas mencionadas.

---

### 3. Atualizar a Tabela (Base de Dados) Automática
Sempre que você adicionar ou renomear uma aula na pasta do curso, **você não precisa editar a tabela manualmente no `index.md`**!  
Basta executar o script de automação:

```bash
# Para atualizar apenas o seu novo curso (indicando a pasta do curso):
python3 scripts/generate_course_table.py --dir content/pt-br/resource/novo-curso-exemplo

# OU para atualizar todos os cursos de uma só vez:
npm run update-courses
```

#### O que o Script Automático Faz?
1. Lê todos os arquivos `aula-*.md` na pasta do curso.
2. Identifica o número da aula, o título limpo e as normas ABNT / IBGE mencionadas no texto.
3. Checa automaticamente na pasta `/assets/biblioteca/<nome-do-curso>/` se existem:
   - Slides em formato LaTeX (`slides-latex/aula-XX.pdf`)
   - Slides em formato PowerPoint (`slides-pptx/aula-XX.pdf`)
   - Imagens de capa (`thumbs/aula-XX.png`)
4. **Preenche sozinho a Tabela de Aulas** no bloco marcado por `<!-- COURSE_TABLE_START -->` ... `<!-- COURSE_TABLE_END -->`.
5. **Atualiza sozinho o Carrossel Ilustrado** no bloco marcado por `<!-- COURSE_CAROUSEL_START -->` ... `<!-- COURSE_CAROUSEL_END -->`.

---

## 🔒 Compilação Automática de LaTeX (.tex) já com Senha Padrão

Para que os arquivos `.tex` gerados ou compilados já gerem os arquivos **PDF protegidos automaticamente pela senha padrão** (`escritaiff2026`), você tem três métodos prontos neste modelo:

### Método 1: Script Gerador Oficial do Curso (`scripts/gerar_slides_aulas.py`)
Sempre que você quiser gerar ou recompilar os slides de um curso inteiro a partir dos arquivos markdown (`aula-*.md`):
```bash
python3 scripts/gerar_slides_aulas.py --dir content/pt-br/resource/latex --slug latex-escrita --senha escritaiff2026
```
> [!NOTE]
> O script compila os códigos LaTeX com `pdflatex`, aplica a criptografia automaticamente com a senha padrão no arquivo PDF final, gera a versão Widescreen PPTX (também com senha) e as imagens de capa em `thumbs/`.

### Método 2: Script de Compilação Avulsa (`compilar_pdf_protegido.py`)
Se você tiver um único arquivo `meu_slide.tex` e quiser compilar já saindo protegido:
```bash
python3 compilar_pdf_protegido.py meu_slide.tex --senha escritaiff2026
```

### Método 3: Via `latexmk` no VS Code ou Terminal (Arquivo `.latexmkrc`)
O modelo já vem com o arquivo `.latexmkrc` na raiz da pasta. Ao compilar com `latexmk -pdf arquivo.tex` (ou clicando no botão **Build LaTeX Project** do VS Code), o pós-processamento de criptografia executa automaticamente ao fim do build e sela o PDF com a senha padrão!

---

## 🏛️ Garantia Institucional
Todos os arquivos PDF de slides e ementas devem ser protegidos pela senha institucional padrão (`escritaiff2026` ou a senha definida para a disciplina) para manter a conformidade de segurança acadêmica do IFF.
