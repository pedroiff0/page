---
publish: false
password: escritaiff2026
title: "Aula 15 - Modularização e BibLaTeX"
created: "2026-08-04T14:33:27-03:00"
modified: "2026-08-04T14:33:27-03:00"
tags: ['latex', 'modularizacao', 'biblatex', 'abnt']
---

> **Aviso:** Os recursos adicionais desta aula (listas de exercícios estendidas, gabaritos e templates) são protegidos. Utilize a senha `escritaiff2026` para acessá-los no portal do aluno.

**Carga Horária:** 2h (Aula Diária)


## Objetivos da Aula
Aprender a estruturar projetos longos com `\input` e `\include` e gerenciar bibliografias com `biblatex` e `biber` em conformidade com as normas NBR 6023 e NBR 10520.


## Slide Referente da Aula (PPTX — Modelo Institucional IFF)

Para apresentações em auditórios do IFF ou defesas que utilizam o **Microsoft PowerPoint (.pptx)** (compatível com LibreOffice Impress e Google Slides), disponibilizamos o modelo institucional Widescreen (16:9) pronto para uso e estruturado nas normas canônicas da ABNT/IBGE abordadas nesta aula:

### 1. Especificação Visual e Identidade IFF (Widescreen 16:9)
- **Paleta Institucional:**
  - Verde Oficial IFF: `#2D6238` (`RGB: 45, 98, 56`) — Primária para Títulos e Capa.
  - Vermelho Destaque IFF: `#B3282D` (`RGB: 179, 40, 45`) — Secundária para Alertas e Código.
  - Cinza Chumbo: `#333333` (`RGB: 51, 51, 51`) — Corpo de Texto.
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Silva | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 15`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 15: Modularização do Projeto e BibLaTeX/Biber](/assets/biblioteca/latex-escrita/slides-pptx/aula-15-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-15.md -o aula-15-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```


## Normas ABNT Aplicáveis
As normas NBR 6023:2018 (Referências) e NBR 10520:2023 (Citações) exigem rigor na pontuação e indicação de autoria (e.g., chamada autor-data em caixa alta ou baixa, dependendo da posição). O `biblatex-abnt` no LaTeX automatiza este rigor, controlando o formato da lista de referências e as chamadas (`\cite`, `\textcite`), eliminando erros de consistência manual.

## Estudo de Caso
Durante a produção de uma tese de 300 páginas, a compilação única tornava-se lenta e a organização textual confusa. Ao dividir a tese em capítulos (`\include{capitulos/01-introducao}`), o doutorando pôde trabalhar focadamente. A integração com o Zotero para exportar o `.bib` garantiu que 150 referências fossem citadas perfeitamente via `biblatex-abnt`.

## Diagramas e Ilustrações
```mermaid
graph TD
    A[main.tex] --> B(\include{cap1})
    A --> C(\include{cap2})
    A --> D(\include{cap3})
    E[referencias.bib] -.->|biber| A
    style A fill:#f9f,stroke:#333,stroke-width:4px
```

## Exercício Prático
1. Crie um projeto com um `main.tex` e dois arquivos separados `cap1.tex` e `cap2.tex`.
2. Inclua um arquivo `.bib` contendo a referência de um livro de sua escolha.
3. Cite o livro no `cap1.tex` usando `\textcite` e imprima a bibliografia no final.

## Referências Bibliográficas
ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6023**: Informação e documentação — Referências — Elaboração. Rio de Janeiro: ABNT, 2018.
ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 10520**: Informação e documentação — Citações em documentos — Apresentação. Rio de Janeiro: ABNT, 2023.
