---
title: "Aula 20 - Customização Avançada de Floats, Listas e Sumário Dinâmico"
publish: false
password: escritaiff2026
created: "2026-08-04"
modified: "2026-08-04"
tags: [latex, curso, aula-20, floats, nbr6027, abnt]
---

# Aula 20 - Customização Avançada de Floats, Listas e Sumário Dinâmico (ABNT NBR 6027)

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
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Rocha de Andrade | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 20`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 20: Floats Customizados e Sumário Dinâmico](/assets/biblioteca/latex-escrita/slides-pptx/aula-20-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-20.md -o aula-20-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```


## Detalhamento da Norma ABNT NBR 6027:2012

A **NBR 6027** regulamenta a elaboração do sumário. As regras estritas incluem:
- **Localização:** O sumário é o último elemento pré-textual.
- **Tipografia:** Os indicativos das seções (1, 1.1, 1.1.1) devem estar alinhados à esquerda. O título das seções pode ter destaque tipográfico hierárquico (negrito, maiúsculas, etc.), mas este destaque deve ser idêntico ao utilizado no corpo do texto.
- No LaTeX, pacotes como `tocloft` permitem redefinir macros internas como `\cftsecfont` e `\cftsecpagefont` para manter a coerência exigida pela norma entre o sumário e as seções reais do documento.

## Estudo de Caso (Use Case)

**Contexto:** Um pesquisador nota que as seções terciárias no sumário não estão recebendo a formatação itálico que ele aplicou no corpo do texto.
**Problema:** A classe padrão de LaTeX não sincroniza estilos tipográficos entre o título da seção no texto e no `.toc` (Table of Contents).
**Solução:** Configuração do pacote `tocloft` para injetar comandos de estilo diretamente na entrada do sumário. Exemplo de solução implementada: `\renewcommand{\cftsubsubsectionfont}{\itshape}`.

## Diagramas e Ilustrações

```mermaid
sequenceDiagram
    participant TEX as Arquivo .tex
    participant Compiler as LaTeX Compiler
    participant TOC as Arquivo .toc
    TEX->>Compiler: \tableofcontents
    Compiler->>TOC: Lê as entradas (Capítulos, Seções)
    TOC-->>Compiler: Formata segundo tocloft
    Compiler-->>TEX: Renderiza o Sumário (NBR 6027)
```

## Exercício Prático

1. Inclua uma figura no seu documento usando o ambiente `figure`.
2. Assegure-se de que a figura está ancorada corretamente com o parâmetro `[htpb]`.
3. Configure o sumário para não apresentar as linhas pontilhadas (dots) para capítulos, seguindo as variações da NBR 6027, usando `\renewcommand{\cftchapdotsep}{\cftnodots}`.

## Referências Bibliográficas

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6027**: Informação e documentação — Sumário — Apresentação. Rio de Janeiro: ABNT, 2012.
