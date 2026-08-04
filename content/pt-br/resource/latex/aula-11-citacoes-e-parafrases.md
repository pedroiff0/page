---
title: "Aula 11 - Citações e Paráfrases"
publish: false
password: escritaiff2026
created: "2026-08-04"
modified: "2026-08-04"
tags: [latex, citacoes, abnt, nbr10520]
---

# Aula 11 - Citações e Paráfrases

**Carga Horária:** 2h - Aula Diária

> **Aviso:** Os materiais complementares e templates estão protegidos. Utilize a senha `escritaiff2026` para acessá-los.

## 1. Slide Referente da Aula (Beamer)

```latex
\documentclass[aspectratio=169]{beamer}
\usetheme{Madrid}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[brazil]{babel}

\title{Escrita Acadêmica e LaTeX}
\subtitle{Aula 11: Citações (ABNT NBR 10520:2023)}
\author{Prof. Dr. Pedro}
\institute{Instituto Federal Fluminense (IFF)}
\date{\today}

\begin{document}

\begin{frame}
    \titlepage
\end{frame}

\begin{frame}{Atualizações da NBR 10520:2023}
    \begin{itemize}
        \item Fim da caixa alta obrigatória nos parênteses: (Silva, 2023) ao invés de (SILVA, 2023).
        \item Citação Indireta: Livre (paráfrase) do autor, sem aspas. Página é opcional.
        \item Citação Direta Curta (até 3 linhas): com aspas duplas e indicação de página obrigatória.
        \item Citação Direta Longa (+ de 3 linhas): recuo de 4cm, sem aspas, fonte menor e indicação de página obrigatória.
    \end{itemize}
\end{frame}

\begin{frame}{LaTeX: pacote \texttt{abntex2cite}}
    \begin{itemize}
        \item \texttt{\textbackslash cite\{chave\}} $\rightarrow$ (Silva, 2023)
        \item \texttt{\textbackslash citeonline\{chave\}} $\rightarrow$ Silva (2023)
        \item \texttt{\textbackslash cite[p.~10]\{chave\}} $\rightarrow$ (Silva, 2023, p. 10)
    \end{itemize}
\end{frame}

\end{document}
```

## 2. Detalhamento Minucioso das Normas ABNT (NBR 10520:2023)
A **ABNT NBR 10520:2023** mudou drasticamente as citações no Brasil. A mudança mais sensível é a **padronização das chamadas em maiúsculas e minúsculas**, extinguindo o uso do ALL CAPS dentro dos parênteses para autores institucionais ou pessoais. 
- **Citação Direta Curta:** Textualmente igual, aspas, inserida no texto. Obrigatório Autor, Ano, Página.
- **Citação Direta Longa:** Mais de 3 linhas, recuo padrão de 4 cm da margem esquerda, fonte menor que o texto (geralmente tam 10), espaçamento simples, sem aspas.
- **Citação Indireta (Paráfrase):** Interpretação com as próprias palavras. Autor e Ano obrigatórios.

## 3. Estudo de Caso (Use Case) Real
**Contexto:** Um artigo da área de Educação citando Freire (1996) e a nova regra de 2023.
- **Forma Antiga (Antes de 2023):** "Educar é impregnar de sentido o que fazemos" (FREIRE, 1996, p. 32).
- **Nova Norma (2023):** "Educar é impregnar de sentido o que fazemos" (Freire, 1996, p. 32).
- No LaTeX, se o usuário ainda usa versões antigas do pacote `abntex2cite`, a compilação gerará a chamada em ALL CAPS. É crucial ajustar as opções do pacote ou migrar para configurações atualizadas do `biblatex-abnt`.

## 4. Diagramas e Ilustrações (LaTeX Code Snippet)

```latex
% Exemplo de Citação Direta Longa em LaTeX
Segundo Freire (1996), a pedagogia é...
\begin{citacao}
Ensinar não é transferir conhecimento, mas criar as 
possibilidades para a sua própria produção ou a sua construção. 
Quando entro em uma sala de aula devo estar sendo um ser aberto
a indagações. (Freire, 1996, p. 47).
\end{citacao}
```

## 5. Exercício Prático
1. Escreva um parágrafo combinando uma citação indireta de dois autores (usando `\citeonline` ou sistema autor-data no texto) e uma citação direta curta de outro autor.
2. Configure o seu ambiente LaTeX com o `abntex2cite` ou `biblatex` para garantir que o formato (Autor, Ano) saia sem Caixa Alta.

## 6. Referências Bibliográficas
- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 10520**: Informação e documentação: citações em documentos: apresentação. Rio de Janeiro: ABNT, 2023.
- FRANÇA, J. L. et al. **Manual para normalização de publicações técnico-científicas**. 9. ed. Belo Horizonte: UFMG, 2013.


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
\titulo{Aula 11: Citações e Paráfrases (NBR 10520:2023)}
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
\begin{frame}{Roteiro da Aula 11}
    \tableofcontents
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 3: FUNDAMENTAÇÃO TEÓRICA / NORMATIVA ABNT
% ------------------------------------------------------------------------------
\section{Fundamentação e Normativa}
\begin{frame}{Fundamentação Teórica e Normativa ABNT/IBGE}
    \begin{block}{Diretriz Institucional --- Normativa Atualizada ABNT NBR 10520:2023}
        Adoção do formato Caixa Baixa em chamadas no texto (Silva, 2026) e regras para citações diretas > 3 linhas.
    \end{block}
    \vspace{0.3cm}
    \textbf{Pontos-Chave da Aula 11:}
    \begin{itemize}
        \item \textbf{Alinhamento Normativo:} Obediência estrita aos padrões canônicos da ABNT e IBGE.
        \item \textbf{Rigor Metodológico:} Como evitar o plágio por paráfrase imprópria e gerenciar chamadas autor-data ou numéricas.
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
    \begin{block}{Snippet de Referência --- Aula 11}
\begin{verbatim}
\cite{silva2026} \quad \text{vs.} \quad \begin{citacao} ... \end{citacao}
\end{verbatim}
    \end{block}
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 6: SÍNTESE E REFERÊNCIAS BIBLIOGRÁFICAS
% ------------------------------------------------------------------------------
\section{Síntese e Referências}
\begin{frame}{Síntese da Aula e Referências Normativas}
    \begin{itemize}
        \item Consolidação dos conhecimentos da Aula 11 no ecossistema IFF.
        \item Próxima etapa: Aplicação no arquivo \texttt{metadados.sty} e validação do build.
    \end{itemize}
    \vspace{0.4cm}
    \footnotesize
    \textbf{Referência Principal:}
    \begin{thebibliography}{10}
        \bibitem{ref1} ABNT. NBR 10520: Informação e documentação - Citações em documentos. 2023.
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
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Silva | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 11`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 11: Citações e Paráfrases (NBR 10520:2023)](/assets/biblioteca/latex-escrita/slides-pptx/aula-11-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-11.md -o aula-11-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```

