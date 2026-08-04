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


## Slide Referente da Aula (PPTX — Modelo Institucional IFF)

Para apresentações em auditórios do IFF ou defesas que utilizam o **Microsoft PowerPoint (.pptx)** (compatível com LibreOffice Impress e Google Slides), disponibilizamos o modelo institucional Widescreen (16:9) pronto para uso e estruturado nas normas canônicas da ABNT/IBGE abordadas nesta aula:

### 1. Especificação Visual e Identidade IFF (Widescreen 16:9)
- **Paleta Institucional:**
  - Verde Oficial IFF: `#2D6238` (`RGB: 45, 98, 56`) — Primária para Títulos e Capa.
  - Vermelho Destaque IFF: `#B3282D` (`RGB: 179, 40, 45`) — Secundária para Alertas e Código.
  - Cinza Chumbo: `#333333` (`RGB: 51, 51, 51`) — Corpo de Texto.
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Rocha de Andrade | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 24`.

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
