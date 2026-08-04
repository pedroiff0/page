---
publish: false
password: escritaiff2026
title: "Aula 17 - Arquivo de Metadados (.sty)"
created: "2026-08-04T14:33:27-03:00"
modified: "2026-08-04T14:33:27-03:00"
tags: ['latex', 'metadados', 'sty', 'arquitetura', 'abnt']
---

> **Aviso:** Os recursos adicionais desta aula (listas de exercícios estendidas, gabaritos e templates) são protegidos. Utilize a senha `escritaiff2026` para acessá-los no portal do aluno.

**Carga Horária:** 2h (Aula Diária)


## Objetivos da Aula
Aprender a estruturar dados variáveis do documento (autor, título, orientador, banca) através de um arquivo `metadados.sty` para separar a lógica e o conteúdo do documento (Ecossistema ReLaTeX).


## Slide Referente da Aula (PPTX — Modelo Institucional IFF)

Para apresentações em auditórios do IFF ou defesas que utilizam o **Microsoft PowerPoint (.pptx)** (compatível com LibreOffice Impress e Google Slides), disponibilizamos o modelo institucional Widescreen (16:9) pronto para uso e estruturado nas normas canônicas da ABNT/IBGE abordadas nesta aula:

### 1. Especificação Visual e Identidade IFF (Widescreen 16:9)
- **Paleta Institucional:**
  - Verde Oficial IFF: `#2D6238` (`RGB: 45, 98, 56`) — Primária para Títulos e Capa.
  - Vermelho Destaque IFF: `#B3282D` (`RGB: 179, 40, 45`) — Secundária para Alertas e Código.
  - Cinza Chumbo: `#333333` (`RGB: 51, 51, 51`) — Corpo de Texto.
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Rocha de Andrade | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 17`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 17: Arquivo de Metadados (metadados.sty)](/assets/biblioteca/latex-escrita/slides-pptx/aula-17-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-17.md -o aula-17-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```


## Normas ABNT Aplicáveis
A NBR 14724 regulamenta a estrutura pré-textual (Capa, Folha de Rosto, Folha de Aprovação). Esses elementos repetem os mesmos dados: Título, Autor, Instituição. A centralização dessas informações em um arquivo de metadados garante a consistência entre todos os elementos pré-textuais exigidos pela norma, evitando discrepâncias caso o título seja alterado de última hora.

## Estudo de Caso
A coordenadoria de TCC de uma universidade criou um template central (ReLaTeX). Os alunos precisam apenas preencher o arquivo `metadados.sty` com seus dados, sem jamais tocar no arquivo `capa.tex` ou `folha_de_rosto.tex`. Isso reduziu em 90% as devoluções de trabalhos por erros nas páginas iniciais.

## Diagramas e Ilustrações
```mermaid
graph TD
    A[metadados.sty] -->|Injeta dados| B(capa.tex)
    A -->|Injeta dados| C(folha_rosto.tex)
    A -->|Injeta dados| D(aprovacao.tex)
    B --> E[main.tex]
    C --> E
    D --> E
```

## Exercício Prático
1. Crie um arquivo `metadados.sty`.
2. Defina nele três comandos: `\imprimirautor`, `\imprimirtitulo`, e `\imprimirdata`.
3. No seu arquivo `.tex` principal, faça `\usepackage{metadados}` e crie uma capa simples chamando esses comandos.

## Referências Bibliográficas
ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 14724**: Informação e documentação — Trabalhos acadêmicos — Apresentação. Rio de Janeiro: ABNT, 2011.
