---
title: "Aula 10 - Discussão dos Resultados e Conclusão"
publish: false
password: escritaiff2026
created: "2026-08-04"
modified: "2026-08-04"
tags: [latex, discussao, conclusao, abnt]
---

# Aula 10 - Discussão dos Resultados e Conclusão

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
\subtitle{Aula 10: Discussão e Conclusão}
\author{Prof. Dr. Pedro}
\institute{Instituto Federal Fluminense (IFF)}
\date{\today}

\begin{document}

\begin{frame}
    \titlepage
\end{frame}

\begin{frame}{Discussão dos Resultados}
    \begin{itemize}
        \item O que os dados significam? (Interpretação)
        \item Como os achados dialogam com a literatura revisada?
        \item Ocorreram resultados anômalos? Como explicá-los?
        \item Reconhecimento das \textbf{limitações} da pesquisa.
    \end{itemize}
\end{frame}

\begin{frame}{Conclusão (Considerações Finais)}
    \begin{itemize}
        \item Responde ao problema de pesquisa e aos objetivos.
        \item Não é um mero resumo dos capítulos anteriores.
        \item Não se deve introduzir citações e novos dados na conclusão.
        \item Aponta sugestões para trabalhos futuros.
    \end{itemize}
\end{frame}

\end{document}
```

## 2. Detalhamento Minucioso das Normas ABNT (NBR 14724)
Na **ABNT NBR 14724**, a seção de Conclusão (frequentemente chamada de Considerações Finais) representa a parte final textual do documento, onde se apresentam as conclusões correspondentes aos objetivos ou hipóteses. 
Diferentemente dos Resultados, a **Discussão** exige argumentação e ancoragem teórica (citações que corroborem ou refutem os achados). A **Conclusão**, por sua vez, deve ser sintética, fechando o ciclo lógico do trabalho iniciado na Introdução. É terminantemente proibido incluir novos dados ou novas referências teóricas na Conclusão.

## 3. Estudo de Caso (Use Case) Real
**Contexto:** Discussão de um artigo sobre evasão escolar.
- **Erro (Apenas relatou dados):** "A evasão foi de 30% no curso X e 45% no curso Y." (Isso é resultado, não discussão).
- **Abordagem Correta (Discussão):** "A taxa de evasão de 45% no curso Y corrobora os achados de Silva (2021), que atribui esse fenômeno à carga horária noturna. No entanto, o resultado do curso X (30%) diferiu do esperado, possivelmente devido às políticas de nivelamento implementadas no último ano."
- **Na Conclusão:** O pesquisador amarra o texto informando que o objetivo geral (mapear causas da evasão) foi atingido, limitou-se ao ano de 2025, e sugere que futuros trabalhos analisem outros campi.

## 4. Diagramas e Ilustrações

```mermaid
flowchart LR
    A[Introdução / Problema] --> B[Objetivos]
    B --> C[Resultados]
    C --> D[Discussão / Contrastes]
    D --> E[Conclusão / Resposta ao Problema]
    E -.-> A
```

## 5. Exercício Prático
1. Pegue o objetivo geral do seu projeto. Escreva um parágrafo de Conclusão afirmando categoricamente se ele foi alcançado e as implicações diretas disso.
2. Liste 2 limitações severas do seu trabalho (ex: tamanho da amostra, tempo, acesso a laboratórios) de forma transparente.

## 6. Referências Bibliográficas
- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 14724**: Informação e documentação: trabalhos acadêmicos: apresentação. Rio de Janeiro: ABNT, 2011.
- VOLPATO, G. L. **Bases teóricas para redação científica**. São Paulo: Cultura Acadêmica, 2013.



## Slide Referente da Aula (PPTX — Modelo Institucional IFF)

Para apresentações em auditórios do IFF ou defesas que utilizam o **Microsoft PowerPoint (.pptx)** (compatível com LibreOffice Impress e Google Slides), disponibilizamos o modelo institucional Widescreen (16:9) pronto para uso e estruturado nas normas canônicas da ABNT/IBGE abordadas nesta aula:

### 1. Especificação Visual e Identidade IFF (Widescreen 16:9)
- **Paleta Institucional:**
  - Verde Oficial IFF: `#2D6238` (`RGB: 45, 98, 56`) — Primária para Títulos e Capa.
  - Vermelho Destaque IFF: `#B3282D` (`RGB: 179, 40, 45`) — Secundária para Alertas e Código.
  - Cinza Chumbo: `#333333` (`RGB: 51, 51, 51`) — Corpo de Texto.
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Rocha de Andrade | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 10`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 10: Discussão dos Resultados, Limitações e Conclusão](/assets/biblioteca/latex-escrita/slides-pptx/aula-10-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-10.md -o aula-10-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```
