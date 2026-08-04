---
title: "Aula 09 - Resultados e Apresentação Visual de Dados"
publish: false
password: escritaiff2026
created: "2026-08-04"
modified: "2026-08-04"
tags: [latex, resultados, ibge, abnt, quadros, tabelas]
---

# Aula 09 - Resultados e Apresentação Visual de Dados

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
\subtitle{Aula 09: Resultados e Dados}
\author{Prof. Dr. Pedro}
\institute{Instituto Federal Fluminense (IFF)}
\date{\today}

\begin{document}

\begin{frame}
    \titlepage
\end{frame}

\begin{frame}{Apresentação de Dados}
    \begin{itemize}
        \item Os Resultados devem ser objetivos e sem julgamentos precipitados.
        \item Uso estratégico de recursos visuais (Tabelas, Quadros, Gráficos).
        \item No LaTeX: ambientes \texttt{table}, \texttt{tabular} e \texttt{figure}.
    \end{itemize}
\end{frame}

\begin{frame}{Tabela (IBGE) vs Quadro (ABNT)}
    \begin{block}{Tabela (Norma IBGE 1993)}
        \begin{itemize}
            \item Contém dados \textbf{numéricos/estatísticos}.
            \item Bordas laterais ABERTAS. 
            \item Linhas horizontais apenas no cabeçalho e fechamento.
        \end{itemize}
    \end{block}
    
    \begin{block}{Quadro (ABNT NBR 14724)}
        \begin{itemize}
            \item Contém dados \textbf{textuais/teóricos}.
            \item Bordas laterais e internas FECHADAS.
        \end{itemize}
    \end{block}
\end{frame}

\end{document}
```

## 2. Detalhamento Minucioso das Normas ABNT (IBGE 1993 vs NBR 14724)
A diferenciação mais crítica na escrita acadêmica brasileira envolve as Tabelas e Quadros.
A **ABNT NBR 14724** diz que as ilustrações (quadros, figuras) devem ter identificação na parte superior e fonte na parte inferior.
Para as **Tabelas**, aplica-se as **Normas de Apresentação Tabular do IBGE (1993)**:
- **Tabelas:** Representam dados quantitativos rigorosos. Não possuem linhas verticais nas bordas laterais. As linhas horizontais são usadas apenas para separar o cabeçalho do conteúdo e fechar a tabela embaixo.
- **Quadros:** Representam dados qualitativos (textos, comparações de autores). Possuem bordas fechadas em todos os lados e grades internas (grid).

## 3. Estudo de Caso (Use Case) Real
**Contexto:** Um aluno de Engenharia está relatando as propriedades mecânicas de 5 compósitos diferentes na sua dissertação.
- **Erro de Formatação:** O aluno insere os valores de Resistência à Tração e Módulo de Elasticidade em um "Quadro", totalmente fechado com linhas, contrariando o IBGE.
- **Solução Correta:** O aluno cria uma **Tabela**, sem bordas externas laterais. Em LaTeX, ele utiliza o pacote `booktabs` (comandos `\toprule`, `\midrule`, `\bottomrule`) para criar uma tabela impecável, esteticamente profissional e dentro das normas do IBGE.

## 4. Diagramas e Ilustrações (LaTeX / TikZ conceptual)

```latex
% Exemplo de Tabela no padrão IBGE usando booktabs
\begin{table}[h]
\centering
\caption{Resultados dos Ensaios de Tração}
\label{tab:tracao}
\begin{tabular}{lcc}
\toprule
\textbf{Amostra} & \textbf{Resistência (MPa)} & \textbf{Módulo (GPa)} \\
\midrule
Compósito A & 45.2 & 2.1 \\
Compósito B & 52.8 & 2.4 \\
\bottomrule
\end{tabular}
\source{Elaborado pelo autor (2026).}
\end{table}
```

## 5. Exercício Prático
1. Diferencie no seu próprio texto acadêmico onde você deve usar Tabelas e onde deve usar Quadros.
2. Crie uma tabela básica no padrão IBGE usando LaTeX com o pacote `booktabs`.

## 6. Referências Bibliográficas
- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 14724**: Informação e documentação: trabalhos acadêmicos: apresentação. Rio de Janeiro: ABNT, 2011.
- IBGE. **Normas de apresentação tabular**. 3. ed. Rio de Janeiro: IBGE, 1993.



## Slide Referente da Aula (PPTX — Modelo Institucional IFF)

Para apresentações em auditórios do IFF ou defesas que utilizam o **Microsoft PowerPoint (.pptx)** (compatível com LibreOffice Impress e Google Slides), disponibilizamos o modelo institucional Widescreen (16:9) pronto para uso e estruturado nas normas canônicas da ABNT/IBGE abordadas nesta aula:

### 1. Especificação Visual e Identidade IFF (Widescreen 16:9)
- **Paleta Institucional:**
  - Verde Oficial IFF: `#2D6238` (`RGB: 45, 98, 56`) — Primária para Títulos e Capa.
  - Vermelho Destaque IFF: `#B3282D` (`RGB: 179, 40, 45`) — Secundária para Alertas e Código.
  - Cinza Chumbo: `#333333` (`RGB: 51, 51, 51`) — Corpo de Texto.
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Silva | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 09`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 09: Resultados e Apresentação Visual de Dados (IBGE)](/assets/biblioteca/latex-escrita/slides-pptx/aula-09-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-09.md -o aula-09-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```
