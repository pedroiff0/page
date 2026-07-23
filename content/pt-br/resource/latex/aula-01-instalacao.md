---
publish: true
title: "Aula 01 — Instalação e Ambiente"
created: 2026-03-16
---

> [!note] Resumo
> Instalação do TeX Live/MacTeX, editor (VS Code + LaTeX Workshop), fluxo de compilação, Overleaf, e como usar IA com cuidado.

## Objetivo

Nesta primeira aula configuramos o ambiente: instalamos o TeX, definimos um editor, aprendemos o fluxo de compilação e vemos opções on-line (Overleaf) + como aproveitar IA para acelerar a escrita.

## 1. Instalação local (TeX Live)

### 1.1 O que é TeX Live?

É a distribuição de LaTeX mais usada. Inclui o compilador (pdfTeX, XeTeX, LuaTeX), pacotes e utilitários (bibtex, makeindex, latexmk).

### 1.2 Mac (recomendado)

1. Instale via Homebrew (mais simples):

```bash
brew install --cask mactex
```

2. Verifique a instalação:

```bash
pdflatex --version
latexmk --version
```

> [!warning] Espaço em disco
> O TeX Live (MacTeX) ocupa 4-5 GB. Se precisar de uma versão menor, use `basictex`.

### 1.3 Windows (opções)

- **TeX Live**: instalador completo (recomendado para quem precisa de muitos pacotes).
- **MiKTeX**: instala pacotes sob demanda.

### 1.4 Linux

Use o gerenciador de pacotes da sua distribuição (ex: `sudo apt install texlive-full` no Ubuntu) ou baixe o instalador oficial.

## 2. Editor recomendado: Visual Studio Code

### 2.1 Por que usar VS Code

- Suporte a múltiplas linguagens.
- Extensões de edição + integração com Git.
- LaTeX Workshop adiciona recursos (compilação automática, visualização, snippets).

### 2.2 Extensão: LaTeX Workshop

Instale a extensão "LaTeX Workshop" e confirme que:

- Compila com `latexmk`.
- Mostra visualização em PDF integrada.
- Detecta erros e avisos.

### 2.3 Configurações recomendadas

No `settings.json` do VS Code:

```json
{
  "latex-workshop.latex.autoBuild.run": "onSave",
  "latex-workshop.latex.outDir": "%DIR%/build",
  "latex-workshop.view.pdf.viewer": "tab"
}
```

## 3. Workflow básico de compilação

1. Escrever o `.tex`.
2. Compilar (via `latexmk`, via VS Code, ou Overleaf).
3. Revisar o PDF.

Exemplo de compilação manual:

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

> [!tip] Dica
> Usar `-interaction=nonstopmode` ajuda a não travar em erros, mas sempre verifique o log.

## 4. Overleaf (ambiente online)

### 4.1 Vantagens

- Não precisa instalar nada.
- Colaboração em tempo real.
- Histórico de versões automático.

### 4.2 Limitações

- Limite de compilação em planos grátis.
- Dependência de conexão.

### 4.3 Começando

1. Crie conta (Google, GitHub, e-mail).
2. Crie um projeto usando um template (article, report, ABNT, etc.).
3. Faça upload de arquivos (`.tex`, `.bib`, imagens).
4. Compile e veja o PDF na lateral.

## 5. Usando IA com LaTeX (com cuidado)

- Peça sempre para gerar saída em `.tex` ou "LaTeX code".
- Revise o resultado: IA pode errar comandos ou sintaxe.
- Melhore o texto passo a passo e mantenha o arquivo original em backup.

### Ferramentas úteis

- [Overleaf](https://www.overleaf.com/project)
- [Perplexity](https://www.perplexity.ai)
- [Gemini](https://gemini.google.com/app)

## 🔗 Referências e correlatos

- [Curso — visão geral](pt-br/resource/latex) — as 5 aulas e os materiais recomendados.
- [Aula 02 — Básico](pt-br/resource/latex/aula-02-basico) — próxima aula: estrutura do documento, tabelas, figuras, equações.
- [TeX Live](https://tug.org/texlive/)
- [Tutorial Overleaf (30 min)](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)
