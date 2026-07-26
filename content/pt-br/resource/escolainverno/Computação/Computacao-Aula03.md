---
publish: false
created: 2026-07-22
title: "Aula 03"
titulo: Computacao-Aula03
disciplina: Computação Científica de Alto Desempenho
conteudo: Algoritmos clássicos de aprendizado de máquina (supervisionado e não supervisionado) aplicados a dados astronômicos
professor: Fernando Roig
tags:
  - escola-de-inverno-on
  - hpc
  - computacao-paralela
  - aprendizado-de-maquina
cssclasses:
  - page-grid
  - center-images
---
# 💻 Notas de Aula — Computação de Alto Desempenho (Aula 03)

> [!warning] Nota provisória
> Esta nota ainda não reflete o conteúdo real da aula — o professor não disponibilizou slides/PDF até o momento. O texto abaixo é um resumo mínimo dos algoritmos listados nas minhas anotações rápidas da aula, sem o desenvolvimento/contexto que o professor de fato apresentou; será substituído por notas fiéis assim que o material oficial chegar.

> [!note] Resumo
> Continuação da Aula 02: um giro por alguns dos algoritmos clássicos de aprendizado de máquina — supervisionados (regressão linear, árvores de decisão, random forest, k-NN) e não supervisionados (PCA, t-SNE, UMAP) — que implementam, na prática, a taxonomia introduzida na Aula 02.

> [!info] Informações da aula
> **Tema:** Algoritmos de aprendizado de máquina, supervisionado e não supervisionado — continuação de [[Computacao-Aula02|Aula 02]]
> **Professores:** Prof. Dr. Fernando Roig e Prof.ª Dr.ª Lilianne Nakazono

---

## 🎯 Visão geral (resumo mínimo, a expandir)

Esta aula parece ter percorrido, na prática, os dois lados da taxonomia supervisionado/não-supervisionado já apresentada na Aula 02, usando alguns dos algoritmos mais tradicionais de cada família.

### 📑 Tópicos prováveis (a confirmar com o material oficial)
1. Algoritmos supervisionados: regressão linear, árvores de decisão, random forest, k-NN
2. Algoritmos não supervisionados: PCA, t-SNE, UMAP

---

## 📚 Algoritmos supervisionados

- **Regressão linear:** ajusta uma relação linear entre variáveis de entrada e uma saída contínua — o algoritmo supervisionado mais simples, base conceitual para métodos mais complexos.
- **Árvore de decisão:** divide os dados sucessivamente por perguntas binárias sobre os atributos, até chegar a uma predição — fácil de interpretar, mas propensa a *overfitting* isoladamente.
- **Random forest:** combina muitas árvores de decisão treinadas em subamostras diferentes dos dados (*bagging*), reduzindo o overfitting de uma árvore individual e geralmente melhorando a precisão.
- **k-Nearest Neighbours (k-NN):** classifica (ou prevê) um ponto novo com base nos $k$ pontos mais próximos no conjunto de treino, tipicamente por distância euclidiana — simples, mas custoso para bases muito grandes.

## 🧭 Algoritmos não supervisionados (redução de dimensionalidade)

- **PCA (Análise de Componentes Principais):** projeta os dados nas direções de maior variância, uma técnica linear de redução de dimensionalidade — o ponto de partida clássico antes de métodos não lineares.
- **t-SNE:** técnica não linear de redução de dimensionalidade que preserva relações de vizinhança local, muito usada para visualizar dados de alta dimensão em 2D (ver a página de [Machine Learning](pt-br/resource/computacao/machine-learning) e minha própria pesquisa, que usa exatamente esse algoritmo).
- **UMAP:** alternativa mais recente ao t-SNE, também não linear, geralmente mais rápida e melhor em preservar tanto estrutura local quanto global dos dados.

---

## ⚠️ Pontos de atenção

> [!important] Atenção
> *(nenhuma anotação registrada ainda — a preencher a partir do material oficial da aula)*

---

## 📌 Conceitos-chave

- **Regressão linear / árvore de decisão / random forest / k-NN:** algoritmos supervisionados clássicos, do mais simples (regressão) ao mais robusto contra overfitting (random forest, via *bagging* de árvores).
- **PCA:** redução de dimensionalidade linear, pelas direções de maior variância dos dados.
- **t-SNE / UMAP:** redução de dimensionalidade não linear, focada em preservar vizinhança — a base do tipo de análise usada na minha própria pesquisa.

---

## ❓ Perguntas e discussões da aula

> [!question] Perguntas (Aula 3)
> *(nenhuma pergunta registrada ainda)*

---

## 🔗 Referências e correlatos
- [Aula 01](pt-br/resource/escolainverno/computação/computacao-aula01)
- [Aula 02](pt-br/resource/escolainverno/computação/computacao-aula02) — a taxonomia supervisionado/não-supervisionado que esta aula coloca em prática
- [Recursos — Machine Learning](pt-br/resource/computacao/machine-learning) — PCA, t-SNE e os demais algoritmos aqui, explicados em mais profundidade
- [Apresentação de Pesquisa — Vizinhança Solar com t-SNE](pt-br/resource/escolainverno/apresentacao/minhapesquisa-vizinhancasolar-tsne) — uso real do t-SNE citado aqui, aplicado a espectros estelares
