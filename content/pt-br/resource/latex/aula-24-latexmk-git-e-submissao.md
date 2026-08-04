---
title: "Aula 24 - Automação com latexmk, Versionamento Git e Checklist"
publish: false
password: escritaiff2026
created: "2026-08-04"
modified: "2026-08-04"
tags: [latex, curso, aula-24, git, latexmk, automacao]
---

# Aula 24 - Automação com latexmk, Versionamento Git e Checklist de Submissão

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
\titulo{Aula 24: Automação (latexmk), Git e Checklist de Submissão}
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
\begin{frame}{Roteiro da Aula 24}
    \tableofcontents
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 3: FUNDAMENTAÇÃO TEÓRICA / NORMATIVA ABNT
% ------------------------------------------------------------------------------
\section{Fundamentação e Normativa}
\begin{frame}{Fundamentação Teórica e Normativa ABNT/IBGE}
    \begin{block}{Diretriz Institucional --- CI/CD e Versionamento de Documentos TeX}
        Automação da compilação em múltiplos passos (PDFLaTeX -> Biber -> PDFLaTeX) via latexmkrc.
    \end{block}
    \vspace{0.3cm}
    \textbf{Pontos-Chave da Aula 24:}
    \begin{itemize}
        \item \textbf{Alinhamento Normativo:} Obediência estrita aos padrões canônicos da ABNT e IBGE.
        \item \textbf{Rigor Metodológico:} Boas práticas com Git/GitHub (.gitignore para LaTeX) e checklist de submissão na biblioteca.
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
    \begin{block}{Snippet de Referência --- Aula 24}
\begin{verbatim}
\texttt{git add . && git commit -m "Versao final TCC" && latexmk -c}
\end{verbatim}
    \end{block}
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 6: SÍNTESE E REFERÊNCIAS BIBLIOGRÁFICAS
% ------------------------------------------------------------------------------
\section{Síntese e Referências}
\begin{frame}{Síntese da Aula e Referências Normativas}
    \begin{itemize}
        \item Consolidação dos conhecimentos da Aula 24 no ecossistema IFF.
        \item Próxima etapa: Aplicação no arquivo \texttt{metadados.sty} e validação do build.
    \end{itemize}
    \vspace{0.4cm}
    \footnotesize
    \textbf{Referência Principal:}
    \begin{thebibliography}{10}
        \bibitem{ref1} CHACON, S.; STRAUB, B. Pro Git. Apress, 2014.
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
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Silva | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 24`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 24: Automação (latexmk), Git e Checklist de Submissão](/assets/biblioteca/latex-escrita/slides-pptx/aula-24-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-24.md -o aula-24-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```


## Detalhamento das Normas ABNT aplicáveis

Antes da submissão final de um trabalho (verificação final), é crucial aplicar a revisão das normas NBR 12225:2023 (Lombada) e NBR 6028:2021 (Resumo). A automação via script garante que o arquivo final compilado reflita a última versão rastreável e que todos os índices remissivos e bibliográficos sejam gerados corretamente sem pular nenhuma etapa de compilação.

- **NBR 6028:2021 (Resumos):** Verifica-se a extensão (150 a 500 palavras para trabalhos acadêmicos) e a formatação sem parágrafos (texto em bloco único), o que deve ser conferido na versão compilada final.
- **NBR 12225:2023 (Lombadas):** Se houver versão impressa, a capa final exportada pelo LaTeX deve gerar a dimensão correta.

## Estudo de Caso (Use Case)

**Contexto:** Um autor principal e seu orientador estão escrevendo uma tese.
**Problema:** O processo de compilação exige rodar `pdflatex`, depois `biber`, e depois `pdflatex` duas vezes. Além disso, as modificações conflitavam quando trocadas por e-mail.
**Solução:** O ambiente do projeto foi configurado com um repositório Git. Um arquivo `.gitignore` foi adicionado para ignorar arquivos `.aux`, `.log`, `.bbl`. A compilação passou a ser feita via terminal com o comando único `$ latexmk -pdf -interaction=nonstopmode tese.tex`, que detecta as mudanças e automatiza o número correto de passagens.

## Diagramas e Ilustrações

```mermaid
graph LR
    A[Edição de Texto (.tex)] --> B[Git Commit]
    B --> C[Push para Repositório Remoto]
    C --> D[Automação Local (latexmk)]
    D --> E[PDF Finalizado]
    D --> F[Limpeza (latexmk -c)]
```

## Exercício Prático

1. Crie um arquivo `.gitignore` no diretório do seu projeto LaTeX e adicione as extensões: `*.aux`, `*.log`, `*.out`, `*.toc`, `*.bbl`, `*.blg`, `*.fls`, `*.fdb_latexmk`.
2. Inicialize o repositório (`git init`), adicione seus arquivos (`git add .`) e faça o primeiro commit (`git commit -m "Commit inicial"`).
3. Execute o comando `latexmk -pdf seu_arquivo.tex` para compilar o projeto em um único passo.

## Referências Bibliográficas

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6028**: Informação e documentação — Resumo, resenha e recensão — Apresentação. Rio de Janeiro: ABNT, 2021.

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 12225**: Informação e documentação — Lombada — Apresentação. Rio de Janeiro: ABNT, 2023.
