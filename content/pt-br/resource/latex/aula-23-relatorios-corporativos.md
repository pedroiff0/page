---
title: "Aula 23 - Relatórios Corporativos e Documentação Técnica"
publish: false
password: escritaiff2026
created: "2026-08-04"
modified: "2026-08-04"
tags: [latex, curso, aula-23, relatorio, documentacao]
---

# Aula 23 - Relatórios Corporativos e Documentação Técnica (relatoriocorp.cls)

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
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Rocha de Andrade | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 23`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 23: Relatórios Corporativos (relatoriocorp.cls)](/assets/biblioteca/latex-escrita/slides-pptx/aula-23-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-23.md -o aula-23-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```


## Detalhamento da Norma ABNT NBR 10719

A **NBR 10719** especifica os princípios e estrutura para relatórios técnico-científicos.
- **Elementos Obrigatórios:** Capa, Folha de rosto, Resumo, Sumário, Introdução, Desenvolvimento, Conclusão, Referências (NBR 6023).
- **Estruturação:** Diferente das teses, o relatório foca na concisão. A classe `relatoriocorp.cls` implementa a folha de rosto com espaços para classificações de segurança (Confidencial, Restrito, Público) e registro de número de controle documental.

## Estudo de Caso (Use Case)

**Contexto:** Um engenheiro de uma empresa do polo industrial precisa emitir um relatório mensal de falhas em maquinário.
**Problema:** O uso de processadores de texto convencionais desformata relatórios extensos contendo centenas de imagens de sensores e diagramas elétricos gerados por loggers.
**Solução:** O engenheiro usa um script Python que consome os dados e gera um arquivo `.tex` automaticamente usando a classe `relatoriocorp.cls`. O LaTeX compila dezenas de tabelas de falhas com perfeição, mantendo o cabeçalho e rodapé corporativos inalterados.

## Diagramas e Ilustrações

```mermaid
graph TD
    A[Dados do Sensor (CSV)] --> B[Script de Automação Python]
    B --> C[Geração de relatorio_mensal.tex]
    C --> D[Compilação (pdflatex/xelatex)]
    D --> E[Relatório Técnico (PDF) Padronizado]
```

## Exercício Prático

1. Compile o modelo básico da classe `relatoriocorp.cls`.
2. Adicione um "Resumo Executivo" utilizando o ambiente apropriado.
3. Insira uma tabela de listagem de componentes e utilize o comando `\label{}` e `\ref{}` para referenciá-la no texto do relatório.

## Referências Bibliográficas

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 10719**: Informação e documentação — Relatório técnico e/ou científico — Apresentação. Rio de Janeiro: ABNT, 2015.
