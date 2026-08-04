---
publish: true
title: "Aula 06: Revisão Sistemática da Literatura e Protocolo PRISMA 2020"
created: '2026-08-04'
modified: '2026-08-04'
tags: [latex, escrita-academica, abnt, ifftese, prisma, rsl]
---

# Aula 06: Revisão Sistemática da Literatura e Protocolo PRISMA 2020

**Carga Horária Equivalente:** 4 tempos de 50 minutos (3h20m / 4 horas-aula diárias)
**Professor Responsável:** Prof. Dr. Pedro Henrique Rocha de Andrade

---

> [!WARNING] AVISO INSTITUCIONAL
> Os materiais associados a esta disciplina, incluindo links de acesso, bibliografia suplementar e recursos audiovisuais, são protegidos por senha. Em caso de solicitação, utilize a credencial: `escritaiff2026`.

| Material Didático | Link Institucional (Acesso Restrito / Senha Protegida) |
| :--- | :--- |
| 📄 **Slides LaTeX (.pdf)** | [Acessar Slide LaTeX](/assets/biblioteca/latex-escrita/slides-latex/aula-06.pdf) |
| 📊 **Slides PPTX (.pdf)** | [Acessar Slide PPTX](/assets/biblioteca/latex-escrita/slides-pptx/aula-06.pdf) |

---

## 1. Introdução à Revisão Sistemática da Literatura (RSL)

A Revisão Sistemática da Literatura (RSL) é uma abordagem metodológica rigorosa, cujo objetivo central é mapear, avaliar, sintetizar e sumarizar as evidências científicas disponíveis sobre um tema específico. Diferente da revisão narrativa (tradicional), que frequentemente apresenta um viés de seleção por parte do autor, a RSL busca a máxima isenção, replicabilidade e transparência. 

No contexto da escrita acadêmica de alto nível, estruturar um capítulo de estado da arte ou de revisão de literatura através de métodos sistemáticos confere enorme peso à tese ou dissertação. A ABNT NBR 14724 recomenda que a fundamentação teórica seja consistente, atualizada e metodologicamente embasada. A RSL atende perfeitamente a esse requisito.

### 1.1 Revisão Narrativa vs. Revisão Sistemática vs. Mapeamento Sistemático

É crucial distinguir entre as principais formas de revisão bibliográfica:

*   **Revisão Narrativa:** Típica de TCCs introdutórios. O autor escolhe as fontes segundo sua conveniência ou conhecimento prévio. Não há critério explícito de busca ou seleção. Alta suscetibilidade ao viés de confirmação.
*   **Mapeamento Sistemático:** Foca em obter uma visão ampla de um campo de pesquisa, identificar lacunas e tendências de publicação (ex: evolução cronológica, principais autores, veículos de publicação). Menor ênfase na análise profunda do conteúdo de cada estudo.
*   **Revisão Sistemática:** Parte de uma Questão de Pesquisa (Research Question) muito bem delineada. O objetivo é responder a essa pergunta extraindo e sintetizando dados qualitativos ou quantitativos dos estudos primários.

## 2. Bases Indexadas e Motores de Busca Científica

Para garantir a validade de uma RSL, as buscas devem ser realizadas em bases de dados eletrônicas reconhecidas e de alto impacto na área do conhecimento da pesquisa.

### 2.1 Principais Bases Multidisciplinares e Específicas

1.  **Scopus (Elsevier):** Atualmente a maior base de dados de resumos e citações de literatura revisada por pares. Essencial para praticamente todas as áreas da engenharia e tecnologia.
2.  **Web of Science (WoS - Clarivate):** Conhecida pelo rigor em sua Coleção Principal. O índice h e o Fator de Impacto (JCR) são métricas consagradas vinculadas a esta base.
3.  **IEEE Xplore:** Base de dados fundamental e compulsória para pesquisadores de Engenharia Elétrica, Computação, Eletrônica e Telecomunicações.
4.  **ACM Digital Library:** Crucial para pesquisa em Ciência da Computação pura, Interação Humano-Computador, etc.
5.  **PubMed/MEDLINE:** Obrigatória para a área da saúde e bioengenharia.

### 2.2 Estratégia de Busca (String de Busca)

A estratégia de busca é o "coração" da fase de planejamento da RSL. Ela deve ser traduzida em uma string booleana que combine palavras-chave. Utiliza-se a lógica de conjuntos com os operadores **AND** (interseção), **OR** (união) e **NOT** (exclusão).

**Exemplo de estruturação (PICOC - Population, Intervention, Comparison, Outcomes, Context):**
*   **População:** "IoT" OR "Internet of Things"
*   **Intervenção:** "Security" OR "Cryptography" OR "Authentication"
*   **Contexto:** "Smart Home" OR "Domotics"

*String resultante:* `("IoT" OR "Internet of Things") AND ("Security" OR "Cryptography" OR "Authentication") AND ("Smart Home" OR "Domotics")`

> [!TIP] Dica de Pesquisa
> Lembre-se de adaptar a string de busca para a sintaxe específica de cada base de dados. O Scopus, por exemplo, aceita chaves `{ }` para busca exata e `*` como curinga.

## 3. O Protocolo PRISMA 2020

O **PRISMA** (Preferred Reporting Items for Systematic reviews and Meta-Analyses) é um conjunto de diretrizes baseadas em evidências para relatar revisões sistemáticas e meta-análises. A versão atualizada (PRISMA 2020) consiste em um checklist de 27 itens e um fluxograma detalhado.

Embora o PRISMA seja essencialmente um guia de **relato** (como escrever o artigo/capítulo), ele também impulsiona a qualidade da **condução** da pesquisa, pois obriga o pesquisador a registrar dados métricos desde o início.

### 3.1 O Fluxograma PRISMA (Flow Diagram)

O fluxograma mapeia o fluxo de informação ao longo das quatro fases essenciais da RSL. É mandatório em dissertações e teses que aleguem conduzir uma revisão sistemática.

1.  **Identificação (Identification):** Número total de registros encontrados nas bases de dados.
2.  **Triagem (Screening):** Remoção de duplicatas (via software como Mendeley, Zotero, ou Rayyan) e leitura de títulos e resumos.
3.  **Elegibilidade (Eligibility):** Leitura na íntegra dos artigos pré-selecionados e aplicação rigorosa dos Critérios de Inclusão e Exclusão (CI/CE).
4.  **Inclusão (Included):** Número final de artigos primários que comporão a síntese qualitativa e/ou meta-análise quantitativa.

### 3.2 Critérios de Inclusão e Exclusão (CI e CE)

Os critérios devem ser definidos *a priori* no protocolo da pesquisa, antes da execução das buscas, para evitar que o pesquisador manipule os resultados para adequar às suas hipóteses.

**Exemplos de CE (Critérios de Exclusão):**
*   CE1: O artigo não está escrito em inglês, português ou espanhol.
*   CE2: O estudo é apenas um resumo expandido (short paper) de menos de 4 páginas.
*   CE3: O trabalho foca em hardware, não no software/algoritmo (dependendo do escopo da tese).

## 4. Diagrama do Processo (Mermaid)

Abaixo apresentamos uma simplificação do Fluxograma PRISMA estruturado em Mermaid:

```mermaid
flowchart TD
    A[Registros identificados nas bases: \n Scopus=150, WoS=120, IEEE=80 \n Total = 350] --> B(Remoção de Duplicatas);
    B --> |90 duplicatas removidas| C[Registros para Triagem de Título/Resumo \n Total = 260];
    C --> D{Aplicação de Critérios};
    D -->|Excluídos após leitura de resumo: 200| E[Artigos para Leitura na Íntegra \n Total = 60];
    E --> F{Leitura Completa};
    F -->|Excluídos (Falta de detalhe metodológico, \n foco diferente): 35| G[Estudos Incluídos na Revisão \n Total = 25];
    
    style A fill:#e1f5fe,stroke:#01579b
    style G fill:#c8e6c9,stroke:#1b5e20
```

## 5. Estudo de Caso

**O Cenário:** A doutoranda Juliana está conduzindo sua tese sobre "Uso de Inteligência Artificial para Previsão de Falhas em Motores de Indução". Ela precisa escrever o Capítulo 2 (Fundamentação Teórica e Trabalhos Relacionados).

**A Prática Incorreta (Narrativa):** Juliana vai no Google Scholar, digita "IA motores indução", escolhe os 10 primeiros artigos em português que parecem interessantes e escreve um texto resumindo cada um. Seu orientador recusa, apontando viés e falta de profundidade.

**A Prática Correta (Sistemática com PRISMA):**
1.  Juliana elabora uma string em inglês: `("Artificial Intelligence" OR "Machine Learning" OR "Deep Learning") AND ("Induction Motor" OR "Electric Motor") AND ("Fault Diagnosis" OR "Predictive Maintenance")`.
2.  Executa a string no IEEE Xplore, Scopus e Web of Science, restringindo para os últimos 5 anos (2021-2026).
3.  Retorna 450 artigos. Ela importa todos para o Rayyan (software de triagem web). Remove 150 duplicatas.
4.  Lê os 300 abstracts e aplica seus CE (ex: exclui artigos que simulam apenas em ambiente virtual sem bancada de testes). Restam 50 artigos.
5.  Lê os 50 na íntegra. Exclui mais 20 por não apresentarem as métricas de acurácia ou matriz de confusão dos modelos.
6.  Sobra um portfólio de 30 artigos primários de altíssima qualidade. Ela cria tabelas de extração de dados e escreve um capítulo comparando os métodos, descobrindo exatamente qual a lacuna (gap) que sua tese irá preencher (ex: modelos de Deep Learning em motores sob falha incipiente do estator).
7.  Juliana gera o Fluxograma PRISMA no LaTeX (usando TikZ ou inserindo uma figura exportada) e documenta todo o processo, garantindo reprodutibilidade.

## 6. Exercício Prático

**Objetivo:** Estruturar a base de uma RSL.

1.  Defina uma Questão de Pesquisa (RQ) principal alinhada ao tema do seu projeto (TCC, Dissertação ou Tese).
2.  Utilizando a estrutura PICOC (ou PICO), defina as palavras-chave principais e secundárias.
3.  Construa a String de Busca Boolean em inglês.
4.  Liste pelo menos 3 Critérios de Inclusão e 3 Critérios de Exclusão objetivos e inquestionáveis.
5.  Desenhe um esboço do Fluxograma PRISMA (em papel ou usando ferramenta diagramadora) com números hipotéticos de artigos em cada fase para visualizar a estrutura.

## 7. Referências Bibliográficas (ABNT NBR 6023:2018)

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6023**: Informação e documentação: referências: elaboração. Rio de Janeiro: ABNT, 2018.

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 14724**: Informação e documentação: trabalhos acadêmicos: apresentação. Rio de Janeiro: ABNT, 2011.

KITCHENHAM, B. Procedures for performing systematic reviews. **Keele, UK, Keele University**, v. 33, n. 2004, p. 1-26, 2004.

PAGE, M. J. et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. **Systematic reviews**, v. 10, n. 1, p. 1-11, 2021. Disponível em: https://systematicreviewsjournal.biomedcentral.com/articles/10.1186/s13643-021-01539-5. Acesso em: 04 ago. 2026.
