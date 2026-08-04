---
publish: false
password: escritaiff2026
title: "Aula 16 - Gráficos com TikZ e PGFPlots"
created: "2026-08-04T14:33:27-03:00"
modified: "2026-08-04T14:33:27-03:00"
tags: ['latex', 'tikz', 'pgfplots', 'graficos']
---

> **Aviso:** Os recursos adicionais desta aula (listas de exercícios estendidas, gabaritos e templates) são protegidos. Utilize a senha `escritaiff2026` para acessá-los no portal do aluno.

**Carga Horária:** 2h (Aula Diária)


## Objetivos da Aula
Produzir ilustrações vetoriais e gráficos de alta qualidade nativamente no LaTeX usando os pacotes TikZ e PGFPlots.


## Slide Referente da Aula (PPTX — Modelo Institucional IFF)

Para apresentações em auditórios do IFF ou defesas que utilizam o **Microsoft PowerPoint (.pptx)** (compatível com LibreOffice Impress e Google Slides), disponibilizamos o modelo institucional Widescreen (16:9) pronto para uso e estruturado nas normas canônicas da ABNT/IBGE abordadas nesta aula:

### 1. Especificação Visual e Identidade IFF (Widescreen 16:9)
- **Paleta Institucional:**
  - Verde Oficial IFF: `#2D6238` (`RGB: 45, 98, 56`) — Primária para Títulos e Capa.
  - Vermelho Destaque IFF: `#B3282D` (`RGB: 179, 40, 45`) — Secundária para Alertas e Código.
  - Cinza Chumbo: `#333333` (`RGB: 51, 51, 51`) — Corpo de Texto.
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Rocha de Andrade | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 16`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 16: Gráficos Vetoriais com TikZ e PGFPlots](/assets/biblioteca/latex-escrita/slides-pptx/aula-16-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-16.md -o aula-16-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```


## Normas ABNT Aplicáveis
Para ilustrações (gráficos, diagramas, esquemas), a ABNT estipula (frequentemente com base na NBR 14724) que sua identificação aparece na parte superior (e.g., "Figura 1 - Parábola") e a fonte na parte inferior. O ambiente `figure` no LaTeX com `\caption` no topo e comandos customizados ou `\source{}` na base garantem a conformidade visual e vetorial, não perdendo resolução ao dar zoom.

## Estudo de Caso
Um pesquisador de Ciência da Computação precisava apresentar a arquitetura de uma rede neural e um gráfico de performance de erro ao longo das épocas (loss). O uso de imagens PNG ficava pixelado. Ao adotar o TikZ para desenhar a rede e o PGFPlots alimentado por um CSV de dados de treino, o PDF final manteve 100% de precisão gráfica, com a mesma fonte do texto.

## Diagramas e Ilustrações
```tikz
\begin{tikzpicture}[node distance=2cm]
    \node[draw, circle] (A) {Início};
    \node[draw, rectangle, right of=A, node distance=3cm] (B) {Processamento};
    \node[draw, circle, right of=B, node distance=3cm] (C) {Fim};
    \draw[->] (A) -- (B);
    \draw[->] (B) -- (C);
\end{tikzpicture}
```

## Exercício Prático
1. Desenhe um fluxograma de 3 nós interligados utilizando TikZ.
2. Utilize o pacote `pgfplots` para plotar a função seno entre $-2\pi$ e $2\pi$.

## Referências Bibliográficas
ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 14724**: Informação e documentação — Trabalhos acadêmicos — Apresentação. Rio de Janeiro: ABNT, 2011.
TANTau, T. **The TikZ and PGF Packages**. Manual for version 3.1.5B, 2020.
