---
publish: true
title: Aula 03 — Templates e Classes
created: 2026-03-16
---

> [!note] Resumo
> A diferença entre classe e template, onde achar templates prontos, e como adaptar um para outro uso.

**Pré-requisito**: [Aula 02](pt-br/resource/latex/aula-02-basico) para entender a estrutura de um `.tex`.

## 1. Conceitos-chave

- **Classe** (`.cls`): define a estrutura principal do documento (tipos de títulos, margens, comportamento de listagens, etc.). Ex: `article`, `report`, `book`, `abntex2`, `beamer`.
- **Template / modelo**: um conjunto de arquivos (`.tex`, `.sty`, `.cls`, `.bib`, imagens) que já vem pré-configurado para um tipo específico de documento (TCC, artigo científico, apresentação).

## 2. Onde encontrar templates

- [Overleaf Templates](https://www.overleaf.com/latex/templates)
- [Modelos UNILA](https://sites.google.com/site/cursolatexunila/home/sobre-o-curso?authuser=0)
- [CTAN](https://ctan.org/) — Comprehensive TeX Archive Network

## 3. Como usar um template (passo a passo)

1. Clone ou baixe o template (zip) para o seu projeto.
2. Abra o projeto no VS Code (ou Overleaf).
3. Identifique os arquivos principais:
   - `main.tex` / `template.tex`
   - `*.cls` (classe)
   - `*.sty` (pacote personalizado)
   - `bibliography.bib`
4. Construa uma cópia de backup antes de fazer mudanças.
5. Personalize o pré-texto (capa, resumo, dados do autor) e a estrutura dos capítulos.

### 3.1 Exemplo rápido (trocar a classe)

No topo do `main.tex`:

```latex
\documentclass[12pt,a4paper]{report} % original
%\documentclass[12pt,a4paper]{abntex2} % para normas ABNT
```

## 4. Como adaptar um template para outro uso

- Substitua o conteúdo dos capítulos mantendo a estrutura de arquivos.
- Remova ou atualize os `\include`/`\input` dos capítulos.
- Ajuste o arquivo de configuração (se existir) para nome, orientador, etc.
- Teste compilando após cada alteração para isolar erros.

## 5. Exemplos de modelos úteis

- TCC/Relatório (ABNT): `abntex2`.
- Artigo científico: `article` com `IEEEtran`, `Elsevier`, `elsarticle`.
- Apresentação: `beamer` ou `powerdot`.
- Pôster acadêmico: `sciposter`, `a0poster`, `tikzposter`.

Ver [Modelos de Documento](pt-br/resource/latex/modelos-de-documento) para exemplos prontos de cada um.

## 🔗 Referências e correlatos

- [Curso — visão geral](pt-br/resource/latex)
- [Aula 02 — Básico](pt-br/resource/latex/aula-02-basico)
- [Aula 04 — Intermediário](pt-br/resource/latex/aula-04-intermediario)
- [Modelos de Documento](pt-br/resource/latex/modelos-de-documento)
