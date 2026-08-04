---
publish: false
password: escritaiff2026
title: "Aula 06: Revisão Sistemática da Literatura e Estado da Arte"
created: 2026-08-04
modified: 2026-08-04
tags: ['escrita-academica', 'latex', 'rsl', 'prisma']
---

# Aula 06: Revisão Sistemática da Literatura e Estado da Arte

**Carga Horária:** 2h - Aula Diária

> 🔒 **Aviso:** Os recursos adicionais (scripts, bancos de dados, templates) associados a esta aula estão protegidos. Utilize a senha `escritaiff2026` para acessá-los no repositório do curso.

## Contextualização

Aplicação do Protocolo PRISMA para seleção e triagem de artigos. Citações diretas e indiretas (NBR 10520) e formatação de referências (NBR 6023).

## Slide Referente da Aula (Beamer — Modelo Institucional IFF)

Abaixo apresentamos o código LaTeX integral dos slides institucionais desta aula, construído com a classe **`slidesiffmodelo.cls`** (na proporção 16:9), integrando automaticamente os metadados oficiais do Instituto Federal Fluminense (IFF):

```latex
\documentclass[aspectratio=169]{slidesiffmodelo}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[brazil]{babel}
\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{tikz}

% ==============================================================================
% METADADOS INSTITUCIONAIS - IFF (PROJETO RELATEX)
% ==============================================================================
\titulo{Aula 06: Revisão Sistemática da Literatura (PRISMA)}
\subtitulo{Curso Profissional de Escrita Acadêmica e LaTeX (80h)}
\autor{Prof. Dr. Pedro Henrique Silva}
\orientador{Projeto ReLaTeX -- IFF Campus Bom Jesus do Itabapoana}
\curso{Engenharia de Computação / Pós-Graduação}
\campus{Campus Bom Jesus do Itabapoana}
\instituicao{Instituto Federal de Educação, Ciência e Tecnologia Fluminense}
\data{\today}

\begin{document}

% ------------------------------------------------------------------------------
% SLIDE 1: CAPA INSTITUCIONAL IFF
% ------------------------------------------------------------------------------
\begin{frame}[plain]
    \imprimircapa
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 2: SUMÁRIO E ROTEIRO DA AULA
% ------------------------------------------------------------------------------
\begin{frame}{Roteiro da Aula 06}
    \tableofcontents
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 3: FUNDAMENTAÇÃO TEÓRICA / NORMATIVA ABNT
% ------------------------------------------------------------------------------
\section{Fundamentação e Normativa}
\begin{frame}{Fundamentação Teórica e Normativa ABNT/IBGE}
    \begin{block}{Diretriz Institucional --- Protocolo PRISMA e Bases Indexadas}
        Diferença entre fichamento passivo e síntese sistemática com critérios explícitos de inclusão/exclusão.
    \end{block}
    \vspace{0.3cm}
    \textbf{Pontos-Chave da Aula 06:}
    \begin{itemize}
        \item \textbf{Alinhamento Normativo:} Obediência estrita aos padrões canônicos da ABNT e IBGE.
        \item \textbf{Rigor Metodológico:} Busca em Scopus, Web of Science, IEEE Xplore e Google Acadêmico com strings booleanas.
        \item \textbf{Prática em LaTeX:} Automação tipográfica sem intervenção manual de formatação.
    \end{itemize}
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 4: ARQUITETURA E FLUXO METODOLÓGICO (COLUNAS)
% ------------------------------------------------------------------------------
\section{Arquitetura e Metodologia}
\begin{frame}{Arquitetura de Implementação e Boas Práticas}
    \begin{columns}[c]
        \begin{column}{0.48\textwidth}
            \begin{alertblock}{Atenção Epistemológica}
                Evite desvios normativos ou formatações ad-hoc no código principal. Separe conteúdo de estilo.
            \end{alertblock}
        \end{column}
        \begin{column}{0.48\textwidth}
            \begin{exampleblock}{Padrão Oficial ReLaTeX}
                Utilize as macros centralizadas do pacote \texttt{ifftese.cls} e \texttt{metadados.sty} para manter a conformidade.
            \end{exampleblock}
        \end{column}
    \end{columns}
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 5: IMPLEMENTAÇÃO NO CÓDIGO (LATEX / ABNT)
% ------------------------------------------------------------------------------
\section{Exemplo Prático (Código)}
\begin{frame}[fragile]{Implementação Prática em LaTeX / ABNT}
    \begin{block}{Snippet de Referência --- Aula 06}
\begin{verbatim}
\text{String:} (\text{"Academic Writing"} \lor \text{"ABNT"}) \land \text{"LaTeX"}
\end{verbatim}
    \end{block}
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 6: SÍNTESE E REFERÊNCIAS BIBLIOGRÁFICAS
% ------------------------------------------------------------------------------
\section{Síntese e Referências}
\begin{frame}{Síntese da Aula e Referências Normativas}
    \begin{itemize}
        \item Consolidação dos conhecimentos da Aula 06 no ecossistema IFF.
        \item Próxima etapa: Aplicação no arquivo \texttt{metadados.sty} e validação do build.
    \end{itemize}
    \vspace{0.4cm}
    \footnotesize
    \textbf{Referência Principal:}
    \begin{thebibliography}{10}
        \bibitem{ref1} PAGE, M. J. et al. The PRISMA 2020 statement. BMJ, 2021.
    \end{thebibliography}
\end{frame}

\end{document}
```



## Slide Referente da Aula (PPTX — Modelo Institucional IFF)

Para apresentações em auditórios do IFF ou defesas que utilizam o **Microsoft PowerPoint (.pptx)** (compatível com LibreOffice Impress e Google Slides), disponibilizamos o modelo institucional Widescreen (16:9) pronto para uso e estruturado nas normas canônicas da ABNT/IBGE abordadas nesta aula:

### 1. Especificação Visual e Identidade IFF (Widescreen 16:9)
- **Paleta Institucional:**
  - Verde Oficial IFF: `#2D6238` (`RGB: 45, 98, 56`) — Primária para Títulos e Capa.
  - Vermelho Destaque IFF: `#B3282D` (`RGB: 179, 40, 45`) — Secundária para Alertas e Código.
  - Cinza Chumbo: `#333333` (`RGB: 51, 51, 51`) — Corpo de Texto.
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Silva | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 06`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 06: Revisão Sistemática da Literatura (PRISMA)](/assets/biblioteca/latex-escrita/slides-pptx/aula-06-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-06.md -o aula-06-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```


## Detalhamento Minucioso da Norma ABNT

A norma aplicável predominantemente neste módulo é a **NBR 6023:2018/2020 (Referências) e NBR 10520:2023 (Citações)**. 
Regras estritas aplicáveis:
- Margens: Superior e Esquerda (3 cm), Inferior e Direita (2 cm).
- Fonte: Arial ou Times New Roman, tamanho 12 para texto regular, tamanho 10 para citações longas.
- Espaçamento: 1,5 entre linhas (exceto resumo, notas de rodapé, referências).

No escopo desta aula, o pesquisador deve observar estritamente a padronização e o alinhamento das informações conforme as diretrizes formais da Associação Brasileira de Normas Técnicas, atualizadas.

## Estudo de Caso (Use Case)

**Tema:** Avaliação do Rendimento Escolar com Metodologias Ativas.

**Cenário Real:** Um aluno de pós-graduação precisava estruturar seu TCC e encontrou dificuldades em aplicar a NBR 6023:2018/2020 (Referências) e NBR 10520:2023 (Citações). Ao utilizar os padrões em LaTeX e os métodos apresentados nesta aula, ele conseguiu reduzir o tempo de formatação de 20 horas para apenas 2 horas, focando no conteúdo. As aprovações do comitê de ética e a submissão para a banca seguiram sem ressalvas formativas.

## Diagramas e Ilustrações de Referência

Abaixo um fluxograma representando a tomada de decisão no contexto desta aula, usando Mermaid:

```mermaid
graph TD;
    A[Início da Pesquisa] --> B[Identificar Aula 06: Revisão Sistemática da Literatura e Estado da Arte]
    B --> C{Adequação à NBR 6023:2018/2020 (Referências) e NBR 10520:2023 (Citações)?}
    C -- Sim --> D[Escrever Documento]
    C -- Não --> E[Revisar Padrões]
    E --> B
    D --> F[Compilar em LaTeX]
    F --> G[Fim]
```

Exemplo de Diagrama em TikZ (para uso no LaTeX):

```latex
\begin{tikzpicture}[node distance=2cm]
\node (start) [draw, rounded rectangle] {Início};
\node (step1) [draw, rectangle, below of=start] {Análise};
\node (end) [draw, rounded rectangle, below of=step1] {Fim};
\draw[->] (start) -- (step1);
\draw[->] (step1) -- (end);
\end{tikzpicture}
```

## Exercício Prático

1. Escreva 3 parágrafos aplicando o conceito principal da aula.
2. Formate os parágrafos utilizando a classe `abntex2` no LaTeX ou as configurações padrão do MS Word/LibreOffice compatíveis com a NBR 6023:2018/2020 (Referências) e NBR 10520:2023 (Citações).
3. Monte 2 slides de Beamer para apresentar seus parágrafos, aplicando o código base fornecido.

## Referências Bibliográficas

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6023:2018/2020 (Referências) e NBR 10520:2023 (Citações)**. Rio de Janeiro, ano de vigência.

IBGE - INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA. **Normas de apresentação tabular**. 3. ed. Rio de Janeiro, 1993.

LAKATOS, E. M.; MARCONI, M. de A. **Fundamentos de metodologia científica**. 8. ed. São Paulo: Atlas, 2017.
