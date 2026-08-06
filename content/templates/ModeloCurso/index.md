---
publish: true
title: "[NOME DO CURSO OU DISCIPLINE]"
created: '2026-08-06'
modified: '2026-08-06'
tags:
  - nome-do-curso
  - iff
---

Bem-vindo ao repositório oficial da disciplina **[NOME DO CURSO]** do **Instituto Federal Fluminense (IFF) — Campus Bom Jesus do Itabapoana**, ministrada pelo **Prof. Pedro Henrique Rocha de Andrade**.

---

## 🎨 Carrossel de Aulas (Acesso Rápido Interativo)

<!-- O carrossel horizontal interativo pode ser colado aqui com os cards das aulas -->

---

## 📚 Material Suplementar e Documentos Oficiais

> [!note] Guia Rápido e Documentos Institucionais
> - **[📅 Ementa e Cronograma da Disciplina (PDF)](/assets/biblioteca/seu-curso/documentos/cronograma.pdf)** — *Planejamento analítico das aulas e matriz de competências.*
> - **[📜 Código de Conduta e Diretrizes](/assets/biblioteca/seu-curso/documentos/diretrizes.pdf)** — *Diretrizes éticas e conduta discente.*

---

## 📊 Sistema Resumido de Avaliação e Cronograma

> [!tip] Distribuição de Pesos nos Bimestres
> - **📅 Período Letivo:** [DATA INÍCIO] a [DATA FIM] | **⏰ [DIA E HORÁRIO DA AULA]**
> - **🔹 1º Bimestre:** 60% Trabalho Prático / Projeto + 40% Avaliação em Sala.
> - **🔹 2º Bimestre:** 80% Projeto Final + 20% Avaliação em Sala.

---

## 🗺️ Tabela Dinâmica de Aulas

```base
filters:
  and:
    - 'file.folder.startsWith("CAMINHO/DA/PASTA/DO/CURSO")'
    - 'note.publish'
    - 'note.notas'
formulas:
  aula: 'link(file.path, note.title)'
properties:
  formula.aula:
    displayName: Aula & Título da Aula
  note.notas:
    displayName: Notas de Aula (PDF)
  note.slide:
    displayName: Slide Institucional (PDF)
views:
  - type: table
    name: Aulas da Disciplina
    order:
      - formula.aula
      - note.notas
      - note.slide
    sort:
      - property: file.name
        direction: ASC
```

---

## 🏛️ Material de Referência Externa

> [!important] Fontes Canônicas e Portais Oficiais
> - **[Portal IFF](https://www.iff.edu.br/)** — Instituto Federal Fluminense.
