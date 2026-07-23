---
publish: true
title: "LaTeX e Escrita Acadêmica"
tags:
 - recursos
 - latex
 - escrita
---

> [!info] LaTeX é o sistema de preparação de documentos padrão da comunidade científica — artigos, monografias, pôsteres e apresentações. Aqui estão os materiais que uso e recomendo, mais o essencial de normalização ABNT.

## Por que LaTeX?

Editores visuais funcionam até o dia em que você precisa numerar 40 equações, manter referências cruzadas consistentes e formatar a bibliografia no padrão da revista — aí eles viram inimigos. LaTeX separa conteúdo de formatação: você escreve texto puro com marcações, e o sistema cuida de numeração, sumário, citações e layout com qualidade tipográfica profissional. Todo artigo que submeto (incluindo o trabalho descrito em [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection)) é escrito em LaTeX.

## Trilha de estudo

### 1. Primeiros documentos
Crie uma conta no [Overleaf](https://www.overleaf.com) (editor online, zero instalação) e reproduza um documento simples: seções, listas, negrito/itálico, uma equação. O [tutorial oficial de 30 minutos do Overleaf](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) cobre exatamente isso.

### 2. Matemática e estrutura
Equações em display, ambientes `align`, matrizes, teoremas. Depois: figuras com `\includegraphics`, tabelas com `booktabs`, referências cruzadas com `\label`/`\ref`. É o dia a dia de qualquer relatório de disciplina.

### 3. Bibliografia e ABNT
Aprenda BibTeX/BibLaTeX: um arquivo `.bib` com as referências e o estilo cuida do resto. Para trabalhos no Brasil, o pacote [abnTeX2](https://www.abntex.net.br) e o `biblatex-abnt` formatam tudo conforme as normas ABNT automaticamente — a alternativa manual é sofrimento.

### 4. Figuras programáticas e apresentações
TikZ para diagramas vetoriais direto no documento, e Beamer para slides. É o nível em que seus diagramas de arquitetura e pôsteres de congresso ficam com cara de publicação.

## 📚 Materiais recomendados

- **[Apostila LaTeX — do básico ao avançado](assets/biblioteca/latex-escrita/apostila-latex-ufes.pdf)** — PET Mecânica/UFES, distribuição gratuita.
- **[Figuras e Diagramas com TikZ](assets/biblioteca/latex-escrita/figuras-diagramas-tikz-ufpb.pdf)** — Prof. Lenimar Andrade/UFPB.
- **[BibLaTeX Cheat Sheet](assets/biblioteca/latex-escrita/biblatex-cheatsheet.pdf)** e **[Manual do biblatex-abnt](assets/biblioteca/latex-escrita/biblatex-abnt-manual.pdf)** — documentação livre ([CTAN](https://ctan.org/pkg/biblatex-abnt)).
- **Guias de normalização ABNT** — [PUC Minas](assets/biblioteca/latex-escrita/guia-abnt-puc-minas.pdf) e [UNIP](assets/biblioteca/latex-escrita/guia-abnt-unip.pdf), gratuitos.

## 🔗 Referências externas

- [Overleaf Learn](https://www.overleaf.com/learn) — a melhor documentação introdutória de LaTeX que existe, com exemplos executáveis. Comece por aqui.
- [abnTeX2](https://www.abntex.net.br) — classe LaTeX que implementa as normas ABNT para monografias, teses e artigos. Padrão de fato para TCC no Brasil.
- [CTAN](https://ctan.org) — repositório oficial de pacotes LaTeX; a documentação de qualquer pacote está aqui.
- [Detexify](https://detexify.kirelabs.org/classify.html) — desenhe o símbolo que você quer e ele diz o comando LaTeX. Salva vidas em prova de Cálculo.
- [Tables Generator](https://www.tablesgenerator.com) — gera o código LaTeX de tabelas visualmente, porque tabela em LaTeX na mão é penoso.

## Conexão com as disciplinas do curso

- [Expressão Oral e Escrita](expressao-oral-e-escrita.md) — a base de redação técnica.
- [Metodologia Científica e Tecnológica](metodologia-cientifica-e-tecnologica.md) — onde as normas ABNT viram obrigação.
- [Projeto Final de Curso I](projeto-final-de-curso-i.md) e [II](projeto-final-de-curso-ii.md) — o TCC inteiro em LaTeX + abnTeX2.
