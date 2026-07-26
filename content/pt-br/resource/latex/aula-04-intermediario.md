---
publish: true
title: Aula 04 — Intermediário
created: 2026-03-16
---

> [!note] Resumo
> Por que e como modularizar um projeto LaTeX: estrutura de pastas, `\input` vs `\include`, e centralização de metadados.

**Pré-requisito**: [Aulas 01–03](pt-br/resource/latex) (instalação, básico e modelos).

## Por que modularizar?

- Facilita a manutenção de documentos longos.
- Permite reaproveitar conteúdo/estilos em outros projetos.
- Ajuda a isolar erros e a compilar partes específicas.

## Estrutura de projeto recomendada

```
projeto/
├── build/          # saída (PDF, logs, auxiliares)
├── bib/            # bibliografia (.bib)
├── img/            # figuras e imagens
├── tex/            # capítulos e preâmbulo
│   ├── metadata.tex
│   ├── preambulo.tex
│   ├── cap1.tex
│   └── cap2.tex
├── main.tex        # arquivo principal
└── Makefile        # (opcional) scripts de compilação
```

## `\input` vs `\include`

- `\input{arquivo}` insere o conteúdo como se estivesse no mesmo arquivo.
- `\include{arquivo}` cria arquivos auxiliares (`.aux`) e é ótimo para capítulos.

```latex
% main.tex
\documentclass{report}
\begin{document}
\include{tex/cap1}
\include{tex/cap2}
\end{document}
```

## Metadados (centralizar informações do trabalho)

Crie um arquivo como `tex/metadata.tex` com título, autor, orientador, curso, etc., e use esses comandos no preâmbulo para evitar repetição.

```latex
% tex/metadata.tex
\def\titulo{Título do Trabalho}
\def\autor{Nome Completo}
\def\orientador{Prof. Dr. Fulano}
\def\ano{2026}
```

```latex
% main.tex
\input{tex/metadata}
\title{\titulo}
\author{\autor}
\date{\ano}
```

## 🔗 Referências e correlatos

- [Curso — visão geral](pt-br/resource/latex)
- [Aula 03 — Templates e Classes](pt-br/resource/latex/aula-03-modelos)
- [Aula 05 — Avançado](pt-br/resource/latex/aula-05-avancado)
