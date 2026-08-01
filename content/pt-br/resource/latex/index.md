---
publish: true
title: LaTeX e Escrita Acadêmica
created: 2026-07-23
modified: 2026-07-31
published: 2026-07-26T11:10:37.194-03:00
tags:
  - recursos
  - latex
  - escrita
---

> [!note] Resumo
> Um curso completo e gratuito de LaTeX, em português, que vai da instalação até escrever **suas próprias classes** — com dois destinos práticos: documentos acadêmicos no padrão ABNT/IFF (TCC, slides de defesa, pôster) e documentos corporativos com identidade visual (relatórios e apresentações de marca). Tudo construído sobre classes que eu uso de verdade, não sobre exemplos de brochura.

<div class="media-carousel">
  <a href="/pt-br/resource/latex/aula-01-instalacao" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Comece aqui — Aulas 01 a 05" />
    <div class="slide-caption">1. Comece aqui — o essencial em 5 aulas</div>
  </a>
  <a href="/pt-br/resource/latex/aula-06-classe-ifftese" class="carousel-slide">
    <img src="/assets/illustrations/publications.svg" alt="Trilha acadêmica — TCC, slides e pôster" />
    <div class="slide-caption">2. Trilha acadêmica — TCC, defesa e pôster</div>
  </a>
  <a href="/pt-br/resource/latex/aula-11-relatorio-corporativo" class="carousel-slide">
    <img src="/assets/illustrations/informatica.svg" alt="Trilha corporativa — relatórios e slides de marca" />
    <div class="slide-caption">3. Trilha corporativa — relatórios e slides de marca</div>
  </a>
  <a href="/pt-br/research/relatex" class="carousel-slide">
    <img src="/assets/illustrations/research.svg" alt="ReLaTeX — a pesquisa por trás do curso" />
    <div class="slide-caption">4. ReLaTeX — a pesquisa por trás disso tudo</div>
  </a>
</div>

## Por que LaTeX?

Editores visuais funcionam até o dia em que você precisa numerar 40 equações, manter referências cruzadas consistentes e formatar a bibliografia no padrão da revista — aí eles viram inimigos. A dor é sempre a mesma, e você já a conhece: a figura que pula de página e leva a legenda embora, o sumário que desatualiza, a numeração que reinicia sozinha, a formatação que quebra na véspera da entrega.

LaTeX separa **conteúdo** de **formatação**: você escreve texto puro com marcações, e o sistema cuida de numeração, sumário, citações e layout com qualidade tipográfica profissional. O custo é uma curva de aprendizado real nas primeiras semanas. O retorno é que, a partir daí, formatação deixa de ser um problema seu — para sempre, em todos os documentos que você escrever.

Todo artigo que submeto — incluindo o trabalho descrito em [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection) — é escrito em LaTeX.

## O que você leva daqui

- **Um TCC pronto para preencher** — modelo completo em `ifftese.cls`, com capa, ficha catalográfica, banca e bibliografia ABNT já resolvidas.
- **Slides e pôster institucionais** — os mesmos templates usados em bancas e mostras do IFF Campus Bom Jesus do Itabapoana.
- **Um relatório e uma apresentação corporativos** com identidade visual trocável em seis linhas de código.
- **A habilidade de escrever suas próprias classes** — que é o que diferencia quem usa LaTeX de quem _depende_ de um template alheio.

Tudo em português, gratuito, e com o código-fonte explicado linha a linha — inclusive as partes feias.

## Trilha 1 — Fundamentos (comece aqui)

Cinco aulas, do zero. Se você nunca abriu um `.tex`, é por aqui.

1. [Instalação e Ambiente](pt-br/resource/latex/aula-01-instalacao) — TeX Live/MacTeX, VS Code + LaTeX Workshop, Overleaf, uso de IA com cuidado.
2. [Básico](pt-br/resource/latex/aula-02-basico) — estrutura mínima, listas, figuras, tabelas, equações, classes de documento, pacotes essenciais.
3. [Templates e Classes](pt-br/resource/latex/aula-03-modelos) — o que é uma classe vs. um template, onde achar, como adaptar um pronto.
4. [Intermediário](pt-br/resource/latex/aula-04-intermediario) — modularização de projeto, `\input` vs `\include`, metadados centralizados.
5. [Avançado](pt-br/resource/latex/aula-05-avancado) — criar `.sty`/`.cls` próprios, `\makeatletter`, ambientes customizados.

Depois das cinco: [Modelos de Documento](pt-br/resource/latex/modelos-de-documento) — a estrutura mínima de cada tipo (relatório, livro, Beamer, pôster, TCC), para copiar e adaptar.

## Trilha 2 — Acadêmica (ABNT e IFF)

Cinco aulas construídas em cima de classes reais, usadas em trabalhos reais do campus — cada configuração documentada em detalhe, não só o resultado final.

6. [Classe `ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese) — fábrica de macros de metadados, flags comportamentais, floats customizados (quadro/gráfico/fluxograma/algoritmo), recto/verso automático, sumário fluido com dot-leaders medidos dinamicamente.
7. [Pacote `macros.sty`](pt-br/resource/latex/aula-07-pacote-macros) — capa/contracapa/ficha catalográfica com 3 layouts, comandos `\inserirfigura`/`\inserirtabela`/`\inserirgrafico`, ambientes de teorema/exercício com resposta cruzada via hyperref.
8. [Arquivo `metadados.sty`](pt-br/resource/latex/aula-08-pacote-metadados) — o único arquivo que o estudante de fato edita.
9. [Slides de Defesa com o Template Oficial do IFFBJI](pt-br/resource/latex/aula-09-slides-beamer) — o mesmo template usado em bancas reais do campus.
10. [Pôster Científico com `iffposter.cls`](pt-br/resource/latex/aula-10-poster-cientifico) — a classe oficial de pôster do IFFBJI: cabeçalho/rodapé com imagem, sistema de logos, escala de fonte dinâmica.

**[📦 Modelo de TCC completo preenchido (.zip)](assets/biblioteca/latex-escrita/modelo-ifftese-tcc.zip)** — um TCC de exemplo (dados fictícios, tema de sistemas de recomendação) já rodando: capa, ficha catalográfica, banca, dedicatória, epígrafe, resumo/abstract, 4 capítulos, apêndice, anexo e bibliografia, comentado comando a comando. Baixe, abra no Overleaf ou compile local, e vá trocando os dados fictícios pelos seus.

**[📦 Modelo de pôster completo preenchido (.zip)](assets/biblioteca/latex-escrita/modelo-iffposter-banner.zip)** — não é fictício: é o pôster real que apresentei na XIV Mostra do Conhecimento do IFF-BJI, com a mesma pesquisa de [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection), cabeçalho oficial do evento e logos de fomento inclusos.

**[📦 Modelo de slides de defesa (.zip)](assets/biblioteca/latex-escrita/modelo-slide-iffbji.zip)** — o template `slidesiffmodelo.cls` do campus, já preenchido.

## Trilha 3 — Corporativa (relatórios e apresentações de marca)

LaTeX não é só para a universidade. As mesmas ferramentas que fazem um TCC obedecer à ABNT fazem um relatório obedecer ao **manual de marca** de uma empresa — e resolvem, de quebra, o problema que ninguém resolve no Word: manter relatório e apresentação com exatamente a mesma identidade visual, versão após versão.

11. [Relatório Corporativo](pt-br/resource/latex/aula-11-relatorio-corporativo) — a classe `relatoriocorp.cls` do zero: paleta de marca num ponto único, capa com faixa colorida, cabeçalho/rodapé com logo, controle de versões, sumário executivo em destaque, tabelas financeiras alinhadas na vírgula, gráficos na cor da marca, caixas de recomendação/risco, marca d'água de confidencialidade e página de assinaturas.
12. [Slides Corporativos](pt-br/resource/latex/aula-12-slides-corporativos) — o tema `beamerthemecorp.sty`: capa em tela cheia, título com régua, rodapé com seção e paginação, divisória automática de seção, cartões de KPI, roadmap em TikZ e variante de fundo escuro para auditório.

[**Modelos Corporativos**](pt-br/resource/latex/modelos-corporativos) — a página prática da trilha: estrutura de pastas do projeto, o `marca.sty` que faz relatório e slides serem incapazes de divergir de cor, troca de identidade visual em três passos, compilação com `latexmk` e o checklist de conferência antes de entregar.

## A pesquisa por trás do curso

Este material não nasceu de um tutorial: nasceu de um projeto de pesquisa. O **[ReLaTeX](pt-br/research/relatex)** desenvolveu a classe `ifftese.cls` e o pacote `macros.sty` para automatizar o cumprimento das normas ABNT (NBR 14724, NBR 6027) em trabalhos do Instituto Federal Fluminense — atacando exatamente a barreira que faz gente desistir do LaTeX no primeiro dia.

O trabalho será apresentado no **CONEPE 2026** (setembro), em coautoria com [Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja), [Maria Luiza Linhares Dantas](https://www.mlldantas.com) e [Ana Mara Figueiredo de Oliveira](https://integra.iff.edu.br/ecossistema/pessoas/ana-mara-de-oliveira-figueiredo/colaboradora), e segue em desenvolvimento — inclusive uma interface web, no estilo do Overleaf, focada só nessa classe, para quem prefere preencher formulários a editar código.

As aulas 06 a 08 são, literalmente, a documentação interna desse projeto aberta ao público. [Conheça o ReLaTeX →](pt-br/research/relatex)

## 📚 Materiais recomendados

- **[Apostila LaTeX — do básico ao avançado](assets/biblioteca/latex-escrita/apostila-latex-ufes.pdf)** — PET Mecânica/UFES, distribuição gratuita.
- **[Figuras e Diagramas com TikZ](assets/biblioteca/latex-escrita/figuras-diagramas-tikz-ufpb.pdf)** — Prof. Lenimar Andrade/UFPB.
- **[BibLaTeX Cheat Sheet](assets/biblioteca/latex-escrita/biblatex-cheatsheet.pdf)** e **[Manual do biblatex-abnt](assets/biblioteca/latex-escrita/biblatex-abnt-manual.pdf)** — documentação livre ([CTAN](https://ctan.org/pkg/biblatex-abnt)).
- **Guias de normalização ABNT** — [PUC Minas](assets/biblioteca/latex-escrita/guia-abnt-puc-minas.pdf) e [UNIP](assets/biblioteca/latex-escrita/guia-abnt-unip.pdf), gratuitos.

## 🔗 Referências e correlatos

- [ReLaTeX](pt-br/research/relatex) — o projeto de pesquisa que originou as classes deste curso.
- [Overleaf Learn](https://www.overleaf.com/learn) — a melhor documentação introdutória de LaTeX que existe, com exemplos executáveis. Comece por aqui.
- [abnTeX2](https://www.abntex.net.br) — classe LaTeX que implementa as normas ABNT para monografias, teses e artigos. Padrão de fato para TCC no Brasil.
- [CTAN](https://ctan.org) — repositório oficial de pacotes LaTeX; a documentação de qualquer pacote está aqui.
- [Detexify](https://detexify.kirelabs.org/classify.html) — desenhe o símbolo que você quer e ele diz o comando LaTeX. Salva vidas em prova de Cálculo.
- [Tables Generator](https://www.tablesgenerator.com) — gera o código LaTeX de tabelas visualmente, porque tabela em LaTeX na mão é penoso.
- [Expressão Oral e Escrita](pt-br/resource/engenharia-de-computação/1-periodo/expressao-oral-e-escrita) — a base de redação técnica.
- [Metodologia Científica e Tecnológica](pt-br/resource/engenharia-de-computação/8-periodo/metodologia-cientifica-e-tecnologica) — onde as normas ABNT viram obrigação.
- [Projeto Final de Curso I](pt-br/resource/engenharia-de-computação/9-periodo/projeto-final-de-curso-i) e [II](pt-br/resource/engenharia-de-computação/10-periodo/projeto-final-de-curso-ii) — o TCC inteiro em LaTeX + abnTeX2.
