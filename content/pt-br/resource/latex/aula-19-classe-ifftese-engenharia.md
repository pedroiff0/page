---
title: "Aula 19 - Engenharia de Macros e Estrutura Interna da Classe ifftese.cls"
publish: false
password: escritaiff2026
created: "2026-08-04"
modified: "2026-08-04"
tags: [latex, curso, aula-19, ifftese, macros, abnt]
---

# Aula 19 - Engenharia de Macros e Estrutura Interna da Classe ifftese.cls

**Carga horária:** 2h (Aula Diária)

> [!WARNING]
> **Aviso:** Os recursos adicionais desta aula estão protegidos pela senha "escritaiff2026".

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
\titulo{Aula 19: Engenharia de Macros e ifftese.cls}
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
\begin{frame}{Roteiro da Aula 19}
    \tableofcontents
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 3: FUNDAMENTAÇÃO TEÓRICA / NORMATIVA ABNT
% ------------------------------------------------------------------------------
\section{Fundamentação e Normativa}
\begin{frame}{Fundamentação Teórica e Normativa ABNT/IBGE}
    \begin{block}{Diretriz Institucional --- Anatomia Interna da Classe ifftese.cls}
        Como a classe herda de abntex2 e redefine comandos com \makeatletter e \makeatother.
    \end{block}
    \vspace{0.3cm}
    \textbf{Pontos-Chave da Aula 19:}
    \begin{itemize}
        \item \textbf{Alinhamento Normativo:} Obediência estrita aos padrões canônicos da ABNT e IBGE.
        \item \textbf{Rigor Metodológico:} Controle programável de margens, folhas de rosto institucionais e pontilhados dinâmicos no sumário.
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
    \begin{block}{Snippet de Referência --- Aula 19}
\begin{verbatim}
\makeatletter \renewcommand{\folhaderostocontent}{...} \makeatother
\end{verbatim}
    \end{block}
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 6: SÍNTESE E REFERÊNCIAS BIBLIOGRÁFICAS
% ------------------------------------------------------------------------------
\section{Síntese e Referências}
\begin{frame}{Síntese da Aula e Referências Normativas}
    \begin{itemize}
        \item Consolidação dos conhecimentos da Aula 19 no ecossistema IFF.
        \item Próxima etapa: Aplicação no arquivo \texttt{metadados.sty} e validação do build.
    \end{itemize}
    \vspace{0.4cm}
    \footnotesize
    \textbf{Referência Principal:}
    \begin{thebibliography}{10}
        \bibitem{ref1} ReLaTeX. Projeto e documentação da classe ifftese.cls. IFF, 2026.
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
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Silva | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 19`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 19: Engenharia de Macros e ifftese.cls](/assets/biblioteca/latex-escrita/slides-pptx/aula-19-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-19.md -o aula-19-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```


## Detalhamento da Norma ABNT NBR 14724

A NBR 14724 é a principal norma para trabalhos acadêmicos (teses, dissertações e TCCs). O projeto da classe `ifftese.cls` visa automatizar a conformidade com estas regras estritas:
- **Elementos Pré-Textuais:** Capa, Folha de Rosto, Ficha Catalográfica, Errata, Folha de Aprovação, Dedicatória, Agradecimentos, Epígrafe, Resumo, Abstract, Listas e Sumário.
- **Formatação de Páginas:** As macros da classe ajustam margens (3cm superior/esquerda, 2cm inferior/direita) usando o pacote `geometry`.
- **Numeração de Páginas:** Deve constar a partir da primeira folha da parte textual, em algarismos arábicos. O controle interno de contadores em LaTeX é feito com a redefinição de comandos padrão do ambiente de documento.

## Estudo de Caso (Use Case)

**Contexto:** Um aluno de Engenharia precisa gerar automaticamente a folha de aprovação do seu TCC.
**Problema:** A formatação manual usando espaços e quebras de linha gera inconsistências na impressão.
**Solução:** Implementação da macro `\imprimirfolhadeaprovacao` na classe `ifftese.cls` que captura metadados (`\bancaum`, `\bancadois`) e desenha caixas de assinatura padrão utilizando os ambientes `minipage` e `tabular`, garantindo conformidade rigorosa.

## Diagramas e Ilustrações

```mermaid
graph TD
    A[Documento .tex] --> B{Classe ifftese.cls}
    B --> C[Pacotes Base]
    B --> D[Definição de Variáveis]
    B --> E[Macros ABNT]
    D --> F(\autor, \titulo)
    E --> G(\imprimircapa)
    E --> H(\imprimirfolhaderosto)
```

## Exercício Prático

1. Acesse o arquivo interno `ifftese.cls`.
2. Localize a definição do comando `\imprimircapa`.
3. Altere a fonte do título para o tamanho `\Huge` e observe as mudanças ao compilar seu TCC.
4. Crie uma macro `\meunovocomando` que imprima um texto de aviso formatado.

## Referências Bibliográficas

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 14724**: Informação e documentação — Trabalhos acadêmicos — Apresentação. Rio de Janeiro: ABNT, 2011.
