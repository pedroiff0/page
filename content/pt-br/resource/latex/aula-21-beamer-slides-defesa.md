---
title: "Aula 21 - Slides de Defesa Institucionais em Beamer"
publish: false
password: escritaiff2026
created: "2026-08-04"
modified: "2026-08-04"
tags: [latex, curso, aula-21, beamer, apresentacao]
---

# Aula 21 - Slides de Defesa Institucionais em Beamer com Integração aos Metadados

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
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Rocha de Andrade | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 21`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 21: Slides de Defesa Institucionais (Beamer)](/assets/biblioteca/latex-escrita/slides-pptx/aula-21-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-21.md -o aula-21-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```


## Detalhamento da Norma ABNT NBR aplicáveis

Embora não exista uma norma estrita da ABNT especificamente para *slides* de apresentação, aplicam-se as normas de citações e referências (NBR 10520:2023 e NBR 6023:2018/2020) quando dados, trechos ou figuras de outros autores são utilizados durante a defesa institucional.
- **Citações (NBR 10520:2023):** Devem ser feitas nas caixas de texto ou rodapés dos slides, sempre vinculadas às referências completas.
- **Referências (NBR 6023):** É altamente recomendado o uso de um frame final contendo as referências principais abordadas na apresentação, formatadas de forma legível.

## Estudo de Caso (Use Case)

**Contexto:** Um candidato a mestrado precisa apresentar sua dissertação, que contém inúmeras equações complexas e diagramas em TikZ.
**Problema:** Copiar as equações como imagens para softwares de apresentação convencionais (como PowerPoint) resulta em perda de resolução e dificuldade de edição de última hora.
**Solução:** O candidato utiliza a classe `beamer` com o tema institucional. Ele copia o código LaTeX diretamente do seu arquivo `dissertacao.tex` para os *frames* da apresentação, garantindo renderização vetorial e consistência visual imediata.

## Diagramas e Ilustrações

```mermaid
graph LR
    A[Arquivo tese.tex] --> B(Macros de Dados: \titulo, \autor)
    B --> C[Arquivo apresentacao.tex (Beamer)]
    C --> D[Geração do PDF]
    D --> E[Projeção na Defesa]
```

## Exercício Prático

1. Crie um arquivo `apresentacao.tex` utilizando `\documentclass{beamer}`.
2. Defina o tema como `\usetheme{CambridgeUS}`.
3. Crie 3 frames: Um de título, um de introdução com uma lista (`itemize`), e um contendo uma equação matemática referente ao seu trabalho.
4. Compile e observe o resultado em PDF.

## Referências Bibliográficas

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 10520**: Informação e documentação — Citações em documentos — Apresentação. Rio de Janeiro: ABNT, 2023.
