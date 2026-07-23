---
publish: true
title: "Aula 02"
titulo: Computacao-Aula02
disciplina: Computação Científica de Alto Desempenho
conteudo: Desempenho e arquitetura em MPI, e introdução a dados e aprendizado de máquina em astronomia
professor: Fernando Roig e Lilianne Nakazono
criado: quarta-feira 22/07/2026 14:00
modificado: 22/07/2026
tags:
  - escola-de-inverno-on
  - hpc
  - computacao-paralela
  - aprendizado-de-maquina
  - dados-astronomicos
cssclasses:
  - page-grid
  - center-images
---
# Notas de Aula — Computação de Alto Desempenho (Aula 02)

> [!info] Informações da aula
> **Tema:** Duas partes — desempenho e arquitetura de MPI (continuação da [[260721-Computacao-Aula01|Aula 01]]) e introdução a dados e aprendizado de máquina em astronomia.
> **Professores:** Prof. Dr. Fernando Roig (parte 1) e Prof.ª Dr.ª Lilianne Nakazono (parte 2)

---

## 🎯 Visão geral

Esta aula tem duas partes bem distintas. Na primeira, o Prof. Roig aprofunda o **MPI** apresentado na Aula 01 — indo do "como programar" para o "como isso se comporta na prática": latência de comunicação, arquitetura cliente-servidor e onde o desempenho realmente se perde. Na segunda, a Prof.ª Lilianne Nakazono muda de assunto: como os dados chegam até nós em astronomia, e como o **aprendizado de máquina** processa esses dados para encontrar padrões — uma ponte direta entre HPC (que fornece a capacidade computacional) e ciência de dados (que a usa).

### 📑 Tópicos abordados
1. Desempenho e latência em MPI
2. Arquitetura cliente-servidor
3. OpenMP vs. MPI: comparação direta
4. Como os dados chegam em astronomia
5. Aprendizado de máquina: tipos e fluxo de trabalho

---

## Parte 1 — Desempenho e arquitetura em MPI

### Latência e por que MPI é "mais difícil"

Em comparação com o OpenMP (Aula 01), programar em MPI é reconhecidamente mais trabalhoso: como cada processo tem seu próprio espaço de memória isolado, **toda** comunicação precisa ser explicitada pelo programador (quem envia, quem recebe, o quê, quando) — não existe o "atalho" implícito de ler/escrever uma variável compartilhada. Essa comunicação tem um custo real, a **latência**: o tempo entre o início do envio de uma mensagem e sua chegada ao destino, que não cai a zero mesmo para mensagens pequenas — existe sempre um custo fixo de "estabelecer a conversa" entre dois processos, antes mesmo de considerar o tempo de transmitir os dados em si.

### Arquitetura cliente-servidor

Um padrão comum de organização de processos MPI é o modelo **cliente-servidor**: um processo (ou pequeno grupo) atua como coordenador — distribuindo trabalho, agregando resultados — enquanto os demais processos ("clientes") executam tarefas e devolvem resultados ao coordenador. É uma alternativa ao modelo SPMD "simétrico" da Aula 01 (todos os processos rodando o mesmo código de forma equivalente), mais adequada quando o trabalho não se divide em partes de tamanho previsível — por exemplo, quando um processo central precisa distribuir dinamicamente blocos de tarefas conforme os clientes ficam livres.

### OpenMP vs. MPI: tabela comparativa

| Critério | OpenMP | MPI |
|---|---|---|
| **Unidade de execução** | Thread | Processo |
| **Memória** | Compartilhada (mesmo espaço de endereçamento) | Distribuída (cada processo com memória própria) |
| **Comunicação** | Implícita (leitura/escrita de variáveis) | Explícita (troca de mensagens) |
| **Escopo típico** | Um único nó (multi-core) | Múltiplos nós (cluster inteiro) |
| **Complexidade de programação** | Menor — diretivas sobre código sequencial existente | Maior — é preciso projetar toda a comunicação |
| **Escalabilidade** | Limitada ao número de núcleos de um nó | Escala para milhares de processos/nós |

Na prática, os dois não são mutuamente exclusivos: é comum combinar **MPI entre nós** (memória distribuída) com **OpenMP dentro de cada nó** (memória compartilhada) — o chamado modelo **híbrido MPI+OpenMP**, que aproveita o melhor dos dois paradigmas em clusters modernos com nós multi-core.

---

## Parte 2 — Dados e aprendizado de máquina em astronomia

### Como os dados chegam em astronomia

Fundamentalmente, um telescópio mede quatro coisas sobre a luz que chega: **quanta luz** (fluxo), **de onde** (posição), **quando** e **em que contexto** (comprimento de onda, polarização). Instrumentos diferentes observam em diferentes comprimentos de onda e resoluções, o que diversifica enormemente os formatos de dado disponíveis:

- **Imagens brutas** — dados em 2D (posição no céu).
- **Espectroscopia** — decompõe a luz por comprimento de onda (usada extensivamente em Arqueologia Galáctica, ver GALAH/APOGEE).
- **Fotometria e curvas de luz** — brilho medido ao longo do tempo.
- **Cubos de dados** — combinações 2D (espaço) + 1D (comprimento de onda ou tempo), comuns em espectroscopia de campo integral.

Esses dados são organizados em **catálogos (surveys)** — como o GCNS e o GALAH DR4 já usados na minha própria pesquisa (ver [[MinhaPesquisa-VizinhancaSolar-tSNE|Apresentação de Pesquisa]]). Vale notar que nem todo dado vem de observação direta: **simulações numéricas** (ver Aula 01) e até textos da literatura científica também são fontes de dado tratáveis computacionalmente.

### Aprendizado de máquina: os três tipos

Aprendizado de máquina é, em essência, um algoritmo que ajusta seus próprios parâmetros a partir de dados de treino (e valida esse ajuste em dados de validação) para atingir um objetivo específico. Existem três grandes categorias:

| Tipo | Como aprende | Exemplo de uso |
|---|---|---|
| **Supervisionado** | A partir de exemplos **já rotulados/classificados** | Classificação e regressão (ex.: prever [Fe/H] de uma estrela a partir do espectro) |
| **Não supervisionado** | Encontra estrutura nos dados **sem rótulos** | Agrupamento por características em comum (ex.: o próprio t-SNE usado na minha pesquisa) |
| **Por reforço** | Aprende por tentativa, recompensa e erro | Otimização de estratégias/políticas a partir de um objetivo já definido |

> [!tip] Conexão direta com a minha pesquisa
> O algoritmo **t-SNE** usado no meu trabalho (ver [[MinhaPesquisa-VizinhancaSolar-tSNE|Apresentação de Pesquisa]]) é um exemplo direto de aprendizado **não supervisionado**: ele encontra agrupamentos no espectro estelar sem que eu tenha rotulado previamente nenhuma estrela — os rótulos físicos (Teff, log g, [Fe/H]) só entram *depois*, como validação.

### Fluxo de trabalho de aprendizado de máquina

O processo típico segue uma sequência bem definida:

$$\text{Dados} \rightarrow \text{Atributos} \rightarrow \text{Modelo} \rightarrow \text{Treino do Modelo} \rightarrow \text{Avaliação} \rightarrow \text{Predição}$$

Isto é: primeiro os dados brutos são reduzidos a **atributos** (as variáveis relevantes que o modelo de fato vai usar — ex.: o fluxo espectral normalizado, no caso do t-SNE), depois um **modelo** é escolhido e **treinado** sobre esses atributos, **avaliado** por alguma métrica de qualidade (ver as métricas de confiabilidade discutidas na minha pesquisa) e, só então, usado para **predizer** sobre dados novos.

---

## 📌 Conceitos-chave

- **Latência (MPI):** custo de tempo fixo para estabelecer comunicação entre processos, independente do tamanho da mensagem.
- **Arquitetura cliente-servidor:** um processo coordenador distribui trabalho e agrega resultados de processos "clientes".
- **MPI+OpenMP híbrido:** combina memória distribuída entre nós (MPI) com memória compartilhada dentro de cada nó (OpenMP).
- **Catálogo (survey):** conjunto organizado de dados observacionais ou simulados de múltiplos objetos astronômicos.
- **Aprendizado supervisionado / não supervisionado / por reforço:** as três grandes famílias de aprendizado de máquina, diferenciadas pelo tipo de sinal de treino disponível.
- **Fluxo de ML:** Dados → Atributos → Modelo → Treino → Avaliação → Predição.

---

## ❓ Perguntas e discussões da aula

> [!question] Perguntas (Aula 2)
> *(nenhuma pergunta registrada ainda)*

---

## 🔗 Referências e correlatos
- [Aula 01](pt-br/resource/escolainverno/computação/260721-computacao-aula01)
- [Aula 03](pt-br/resource/escolainverno/computação/computacao-aula03)
- [Recursos — Machine Learning](pt-br/resource/computacao/machine-learning)
- [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection) — a pesquisa citada nesta aula como exemplo de ML não supervisionado
- [Apresentação de Pesquisa](pt-br/resource/escolainverno/apresentacao)
