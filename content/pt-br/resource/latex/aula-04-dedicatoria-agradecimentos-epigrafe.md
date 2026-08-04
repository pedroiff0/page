---
publish: false
password: escritaiff2026
title: "Aula 04: Dedicatória, Agradecimentos e Epígrafe"
created: 2026-08-04
modified: 2026-08-04
tags: ['escrita-academica', 'latex', 'pre-textuais', 'epigrafe']
---

# Aula 04: Dedicatória, Agradecimentos e Epígrafe

**Carga Horária:** 2h - Aula Diária

> 🔒 **Aviso:** Os recursos adicionais (scripts, bancos de dados, templates) associados a esta aula estão protegidos. Utilize a senha `escritaiff2026` para acessá-los no repositório do curso.

## Contextualização

Elementos pré-textuais opcionais. Epígrafe deve seguir NBR 10520 para citações, não aparecendo nas referências a menos que citada no texto principal.


## Slide Referente da Aula (PPTX — Modelo Institucional IFF)

Para apresentações em auditórios do IFF ou defesas que utilizam o **Microsoft PowerPoint (.pptx)** (compatível com LibreOffice Impress e Google Slides), disponibilizamos o modelo institucional Widescreen (16:9) pronto para uso e estruturado nas normas canônicas da ABNT/IBGE abordadas nesta aula:

### 1. Especificação Visual e Identidade IFF (Widescreen 16:9)
- **Paleta Institucional:**
  - Verde Oficial IFF: `#2D6238` (`RGB: 45, 98, 56`) — Primária para Títulos e Capa.
  - Vermelho Destaque IFF: `#B3282D` (`RGB: 179, 40, 45`) — Secundária para Alertas e Código.
  - Cinza Chumbo: `#333333` (`RGB: 51, 51, 51`) — Corpo de Texto.
- **Rodapé Institucional Padronizado:** `Prof. Dr. Pedro Henrique Rocha de Andrade | IFF Campus Bom Jesus do Itabapoana | Curso de Escrita Acadêmica e LaTeX (80h) | Aula 04`.

### 2. Download do Arquivo PPTX Institucional
O arquivo `.pptx` institucional desta aula encontra-se gerado no repositório com todos os 4 slides (Capa, Roteiro, Fundamentação Teórica e Exemplo Prático/Referências):

> [!TIP] **Download da Apresentação**
> **[📥 Baixar Apresentação Institucional em PPTX — Aula 04: Dedicatória, Agradecimentos e Epígrafe](/assets/biblioteca/latex-escrita/slides-pptx/aula-04-iff-institucional.pptx)**

### 3. Conversão Direta via Terminal (Pandoc)
Caso prefira compilar seus próprios slides localmente a partir deste texto Markdown utilizando o template mestre institucional:
```bash
pandoc aula-04.md -o aula-04-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```


## Detalhamento Minucioso da Norma ABNT

A norma aplicável predominantemente neste módulo é a **NBR 14724:2011 e NBR 10520:2023 (Citações na Epígrafe)**. 
Regras estritas aplicáveis:
- Margens: Superior e Esquerda (3 cm), Inferior e Direita (2 cm).
- Fonte: Arial ou Times New Roman, tamanho 12 para texto regular, tamanho 10 para citações longas.
- Espaçamento: 1,5 entre linhas (exceto resumo, notas de rodapé, referências).

No escopo desta aula, o pesquisador deve observar estritamente a padronização e o alinhamento das informações conforme as diretrizes formais da Associação Brasileira de Normas Técnicas, atualizadas.

## Estudo de Caso (Use Case)

**Tema:** Avaliação do Rendimento Escolar com Metodologias Ativas.

**Cenário Real:** Um aluno de pós-graduação precisava estruturar seu TCC e encontrou dificuldades em aplicar a NBR 14724:2011 e NBR 10520:2023 (Citações na Epígrafe). Ao utilizar os padrões em LaTeX e os métodos apresentados nesta aula, ele conseguiu reduzir o tempo de formatação de 20 horas para apenas 2 horas, focando no conteúdo. As aprovações do comitê de ética e a submissão para a banca seguiram sem ressalvas formativas.

## Diagramas e Ilustrações de Referência

Abaixo um fluxograma representando a tomada de decisão no contexto desta aula, usando Mermaid:

```mermaid
graph TD;
    A[Início da Pesquisa] --> B[Identificar Aula 04: Dedicatória, Agradecimentos e Epígrafe]
    B --> C{Adequação à NBR 14724:2011 e NBR 10520:2023 (Citações na Epígrafe)?}
    C -- Sim --> D[Escrever Documento]
    C -- Não --> E[Revisar Padrões]
    E --> B
    D --> F[Compilar em LaTeX]
    F --> G[Fim]
```

Exemplo de Diagrama em TikZ (para uso no LaTeX):

```latex
\begin{tikzpicture}[node distance=2cm]
\node (start) [draw, rounded rectangle] {Início};
\node (step1) [draw, rectangle, below of=start] {Análise};
\node (end) [draw, rounded rectangle, below of=step1] {Fim};
\draw[->] (start) -- (step1);
\draw[->] (step1) -- (end);
\end{tikzpicture}
```

## Exercício Prático

1. Escreva 3 parágrafos aplicando o conceito principal da aula.
2. Formate os parágrafos utilizando a classe `abntex2` no LaTeX ou as configurações padrão do MS Word/LibreOffice compatíveis com a NBR 14724:2011 e NBR 10520:2023 (Citações na Epígrafe).
3. Monte 2 slides de Beamer para apresentar seus parágrafos, aplicando o código base fornecido.

## Referências Bibliográficas

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 14724:2011 e NBR 10520:2023 (Citações na Epígrafe)**. Rio de Janeiro, ano de vigência.

IBGE - INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA. **Normas de apresentação tabular**. 3. ed. Rio de Janeiro, 1993.

LAKATOS, E. M.; MARCONI, M. de A. **Fundamentos de metodologia científica**. 8. ed. São Paulo: Atlas, 2017.
