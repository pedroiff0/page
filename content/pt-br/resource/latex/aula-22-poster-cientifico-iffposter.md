---
title: "Aula 22 - Pôster Científico em LaTeX com a Classe iffposter.cls"
publish: false
password: escritaiff2026
created: "2026-08-04"
modified: "2026-08-04"
tags: [latex, curso, aula-22, poster, tikz]
---

# Aula 22 - Pôster Científico em LaTeX com a Classe iffposter.cls

**Carga horária:** 2h (Aula Diária)

> [!WARNING]
> **Aviso:** Os recursos adicionais desta aula estão protegidos pela senha "escritaiff2026".


## Slide Referente da Aula (PPTX — Modelo Institucional IFF)

Para apresentações em auditórios do IFF ou defesas que utilizam o **Microsoft PowerPoint (.pptx)** (compatível com LibreOffice Impress e Google Slides), disponibilizamos o modelo institucional Widescreen (16:9) pronto para uso e estruturado nas normas canônicas da ABNT/IBGE abordadas nesta aula:

### 1. Especificação Visual e Identidade IFF (Widescreen 16:9)
- **Paleta Institucional:**
  - Verde Oficial IFF: `#2D6238` (`RGB: 45, 98, 56`) — Primária para Títulos e Capa.
  - Vermelho Destaque IFF: `#B3282D` (`RGB: 179, 40, 45`) — Secundária para Alertas e Código.
  - Cinza Chumbo: `#333333` (`RGB: 51, 51, 51`) — Corpo de Texto.
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Silva | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 22`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 22: Pôster Científico em LaTeX (iffposter.cls)](/assets/biblioteca/latex-escrita/slides-pptx/aula-22-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-22.md -o aula-22-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```


## Detalhamento da Norma ABNT e Uso em Pôsteres

Embora pôsteres tenham regras frequentemente ditadas por congressos específicos, a apresentação de referências bibliográficas dentro deles deve seguir a **NBR 6023:2018/2020**. Devido à restrição de espaço, os pôsteres frequentemente utilizam citações no formato numérico (NBR 10520) para economizar espaço nos blocos de texto. O tamanho comum de impressão é o A0 (841 x 1189 mm).

## Estudo de Caso (Use Case)

**Contexto:** Um grupo de pesquisa da instituição foi aprovado para apresentar os resultados de um projeto de extensão num congresso nacional.
**Problema:** Desenvolver um pôster colaborativamente onde os gráficos gerados no Python (matplotlib) e tabelas (pandas) se encaixem perfeitamente nas colunas sem perder qualidade visual.
**Solução:** Utilizando a classe `iffposter.cls`, o layout é dividido em 3 colunas baseadas no `tcolorbox`. Gráficos são exportados como PGF/TikZ ou PDF do Python, mantendo consistência de fonte e resolução infinita ao serem injetados nos blocos do pôster.

## Diagramas e Ilustrações

```tikz
\begin{tikzpicture}
  % Simple representation of a poster layout
  \draw[thick] (0,0) rectangle (6,8);
  \draw[fill=blue!20] (0.2,6.5) rectangle (5.8,7.8); % Header
  \node at (3, 7.15) {Título do Pôster};
  
  \draw[fill=gray!10] (0.2,4) rectangle (2.8,6.3); % Col 1
  \node at (1.5, 5.15) {Intro};
  
  \draw[fill=gray!10] (3.2,4) rectangle (5.8,6.3); % Col 2
  \node at (4.5, 5.15) {Metodologia};
  
  \draw[fill=gray!10] (0.2,1) rectangle (5.8,3.8); % Bottom Col
  \node at (3, 2.4) {Resultados e Gráficos};
\end{tikzpicture}
```

## Exercício Prático

1. Inicie um arquivo com `\documentclass[a0paper]{iffposter}`.
2. Defina os autores e filiações.
3. Crie blocos de conteúdo usando os ambientes predefinidos (ex: `\begin{posterbox}{Introdução}`).
4. Adicione uma imagem vetorial no bloco de resultados.

## Referências Bibliográficas

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6023**: Informação e documentação — Referências — Elaboração. Rio de Janeiro: ABNT, 2018. (Atualizada em 2020).
