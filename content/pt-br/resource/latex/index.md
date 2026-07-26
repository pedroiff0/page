---
publish: true
title: LaTeX e Escrita Acadêmica
created: 2026-07-23
modified: 2026-07-26T11:10:37.194-03:00
published: 2026-07-26T11:10:37.194-03:00
tags:
  - recursos
  - latex
  - escrita
---

> [!note] Resumo
> Curso próprio de LaTeX (5 aulas), do zero à criação de classes, mais materiais recomendados e o essencial de normalização ABNT.

<div class="media-carousel">
  <a href="/pt-br/resource/latex/aula-01-instalacao" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Aula 01 — Instalação e Ambiente" />
    <div class="slide-caption">Aula 01 — Instalação</div>
  </a>
  <a href="/pt-br/resource/latex/aula-02-basico" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Aula 02 — Básico" />
    <div class="slide-caption">Aula 02 — Básico</div>
  </a>
  <a href="/pt-br/resource/latex/aula-03-modelos" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Aula 03 — Templates e Classes" />
    <div class="slide-caption">Aula 03 — Templates</div>
  </a>
  <a href="/pt-br/resource/latex/aula-04-intermediario" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Aula 04 — Intermediário" />
    <div class="slide-caption">Aula 04 — Intermediário</div>
  </a>
  <a href="/pt-br/resource/latex/aula-05-avancado" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Aula 05 — Avançado" />
    <div class="slide-caption">Aula 05 — Avançado</div>
  </a>
  <a href="/pt-br/resource/latex/modelos-de-documento" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Modelos de Documento" />
    <div class="slide-caption">Modelos de Documento</div>
  </a>
  <a href="/pt-br/resource/latex/aula-06-classe-ifftese" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Aula 06 — Classe ifftese.cls" />
    <div class="slide-caption">Aula 06 — Classe ifftese.cls</div>
  </a>
  <a href="/pt-br/resource/latex/aula-07-pacote-macros" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Aula 07 — Pacote macros.sty" />
    <div class="slide-caption">Aula 07 — macros.sty</div>
  </a>
  <a href="/pt-br/resource/latex/aula-08-pacote-metadados" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Aula 08 — Arquivo metadados.sty" />
    <div class="slide-caption">Aula 08 — metadados.sty</div>
  </a>
  <a href="/pt-br/resource/latex/aula-09-slides-beamer" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Aula 09 — Slides com Beamer" />
    <div class="slide-caption">Aula 09 — Slides (Beamer)</div>
  </a>
  <a href="/pt-br/resource/latex/aula-10-poster-cientifico" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Aula 10 — Pôster Científico" />
    <div class="slide-caption">Aula 10 — Pôster Científico</div>
  </a>
</div>

## Por que LaTeX?

Editores visuais funcionam até o dia em que você precisa numerar 40 equações, manter referências cruzadas consistentes e formatar a bibliografia no padrão da revista — aí eles viram inimigos. LaTeX separa conteúdo de formatação: você escreve texto puro com marcações, e o sistema cuida de numeração, sumário, citações e layout com qualidade tipográfica profissional. Todo artigo que submeto (incluindo o trabalho descrito em [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection)) é escrito em LaTeX.

## Curso — 5 aulas

1. [Instalação e Ambiente](pt-br/resource/latex/aula-01-instalacao) — TeX Live/MacTeX, VS Code + LaTeX Workshop, Overleaf, uso de IA com cuidado.
2. [Básico](pt-br/resource/latex/aula-02-basico) — estrutura mínima, listas, figuras, tabelas, equações, classes de documento, pacotes essenciais.
3. [Templates e Classes](pt-br/resource/latex/aula-03-modelos) — o que é uma classe vs. um template, onde achar, como adaptar um pronto.
4. [Intermediário](pt-br/resource/latex/aula-04-intermediario) — modularização de projeto, `\input` vs `\include`, metadados centralizados.
5. [Avançado](pt-br/resource/latex/aula-05-avancado) — criar `.sty`/`.cls` próprios, `@makeatletter`, ambientes customizados.

Depois das 5 aulas: [Modelos de Documento](pt-br/resource/latex/modelos-de-documento) — checklist prático por tipo (TCC/ABNT, Relatório, Livro, Beamer, Pôster científico).

## 🎓 Aprofundamento — estudo de caso real

Três aulas extras, construídas em cima de uma classe LaTeX que uso de verdade no meu próprio TCC (`ifftese.cls`, para o IFF Campus Bom Jesus do Itabapoana) — cada configuração documentada em detalhe, não só o resultado final:

6. [Classe `ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese) — fábrica de macros de metadados, flags comportamentais, floats customizados (quadro/gráfico/fluxograma/algoritmo), recto/verso automático, sumário fluido com dot-leaders medidos dinamicamente.
7. [Pacote `macros.sty`](pt-br/resource/latex/aula-07-pacote-macros) — capa/contracapa/ficha catalográfica com 3 layouts, comandos `\inserirfigura`/`\inserirtabela`/`\inserirgrafico` e variantes de subfigura, ambientes de teorema/exercício com sistema de resposta cruzada via hyperref.
8. [Arquivo `metadados.sty`](pt-br/resource/latex/aula-08-pacote-metadados) — o único arquivo que o estudante de fato edita: preenchimento de flags e dados reais do trabalho.
9. [Slides de Defesa com Beamer](pt-br/resource/latex/aula-09-slides-beamer) — `\documentclass{beamer}` num arquivo à parte, temas, blocos, revelação incremental, roteiro típico de banca.
10. [Pôster Científico (Banner)](pt-br/resource/latex/aula-10-poster-cientifico) — `tikzposter`, blocos e colunas, paleta reaproveitada da classe, boas práticas de pôster A0.

**[📦 Baixar o modelo completo preenchido (.zip)](assets/biblioteca/latex-escrita/modelo-ifftese-tcc.zip)** — um TCC de exemplo (dados fictícios, tema de sistemas de recomendação) já rodando: capa, ficha catalográfica, banca, dedicatória, epígrafe, resumo/abstract, 4 capítulos, apêndice, anexo e bibliografia — mais os slides de defesa (`slides.tex`) e o pôster científico (`banner.tex`) do mesmo trabalho fictício, todos comentados comando a comando. Baixe, abra no Overleaf ou compile local, e vá trocando os dados fictícios pelos seus.

## 📚 Materiais recomendados

- **[Apostila LaTeX — do básico ao avançado](assets/biblioteca/latex-escrita/apostila-latex-ufes.pdf)** — PET Mecânica/UFES, distribuição gratuita.
- **[Figuras e Diagramas com TikZ](assets/biblioteca/latex-escrita/figuras-diagramas-tikz-ufpb.pdf)** — Prof. Lenimar Andrade/UFPB.
- **[BibLaTeX Cheat Sheet](assets/biblioteca/latex-escrita/biblatex-cheatsheet.pdf)** e **[Manual do biblatex-abnt](assets/biblioteca/latex-escrita/biblatex-abnt-manual.pdf)** — documentação livre ([CTAN](https://ctan.org/pkg/biblatex-abnt)).
- **Guias de normalização ABNT** — [PUC Minas](assets/biblioteca/latex-escrita/guia-abnt-puc-minas.pdf) e [UNIP](assets/biblioteca/latex-escrita/guia-abnt-unip.pdf), gratuitos.

## 🔗 Referências e correlatos

- [Overleaf Learn](https://www.overleaf.com/learn) — a melhor documentação introdutória de LaTeX que existe, com exemplos executáveis. Comece por aqui.
- [abnTeX2](https://www.abntex.net.br) — classe LaTeX que implementa as normas ABNT para monografias, teses e artigos. Padrão de fato para TCC no Brasil.
- [CTAN](https://ctan.org) — repositório oficial de pacotes LaTeX; a documentação de qualquer pacote está aqui.
- [Detexify](https://detexify.kirelabs.org/classify.html) — desenhe o símbolo que você quer e ele diz o comando LaTeX. Salva vidas em prova de Cálculo.
- [Tables Generator](https://www.tablesgenerator.com) — gera o código LaTeX de tabelas visualmente, porque tabela em LaTeX na mão é penoso.
- [Expressão Oral e Escrita](pt-br/resource/engenharia-de-computação/1-periodo/expressao-oral-e-escrita) — a base de redação técnica.
- [Metodologia Científica e Tecnológica](pt-br/resource/engenharia-de-computação/8-periodo/metodologia-cientifica-e-tecnologica) — onde as normas ABNT viram obrigação.
- [Projeto Final de Curso I](pt-br/resource/engenharia-de-computação/9-periodo/projeto-final-de-curso-i) e [II](pt-br/resource/engenharia-de-computação/10-periodo/projeto-final-de-curso-ii) — o TCC inteiro em LaTeX + abnTeX2.
