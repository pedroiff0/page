---
publish: true
title: Aula 02
created: 2026-07-22T11:00:00-03:00
modified: 2026-07-26T10:51:54.084-03:00
published: 2026-07-26T10:51:54.084-03:00
tags:
  - escola-de-inverno-on
  - astrofisica-extragalactica
  - aglomerados-de-galaxias
  - evolucao-galactica
cssclasses:
  - page-grid
  - center-images
titulo: Aglomerados-Aula02
disciplina: Astrofísica Extragaláctica
conteudo: Formação hierárquica de estruturas e evolução de galáxias em ambientes de aglomerado
professor: Rogério Monteiro-Oliveira
---

# 🌌 Notas de Aula — Aglomerados de Galáxias (Aula 02)

> [!note] Resumo
> Como aglomerados colapsam hierarquicamente a partir de flutuações de densidade primordiais, e o catálogo de mecanismos físicos que "matam" a formação estelar de uma galáxia ao cair nesse ambiente — terminando na BCG, a galáxia mais extrema desse processo.

> [!info] Informações da aula
> **Tema:** Formação hierárquica de estruturas e como o ambiente de um aglomerado transforma as galáxias que caem nele — continuação de [[Aglomerados-Aula01|Aula 01]]
> **Professor:** Prof. Dr. Rogério Monteiro-Oliveira

---

## 🎯 Visão geral

A Aula 01 tratou o aglomerado como um objeto já formado, em equilíbrio. Esta aula olha para dois pontos que faltavam: **como** essas estruturas colapsam hierarquicamente a partir de pequenas flutuações de densidade do Universo primordial, e **o que acontece** com uma galáxia individual quando ela cai nesse ambiente denso e hostil. A segunda metade da aula — a mais longa — é essencialmente um catálogo de mecanismos físicos que "matam" a formação estelar de uma galáxia ao longo de sua queda em direção ao centro do aglomerado, terminando na galáxia mais extrema desse processo: a **BCG** (Brightest Cluster Galaxy) no fundo do poço de potencial.

### 📑 Tópicos abordados

1. Contraste de densidade e formação hierárquica de estruturas
2. Classificação morfológica e populações de galáxias
3. Mecanismos de transformação ambiental (o que "mata" uma galáxia)
4. O centro do aglomerado: BCG, cooling flows e feedback de AGN

---

## 1. Contraste de densidade e formação hierárquica

A formação de estruturas em grande escala é descrita pelo **parâmetro de contraste de densidade**:

$\delta(\mathbf{x}, t) = \frac{\rho(\mathbf{x}, t) - \bar\rho(t)}{\bar\rho(t)}$

que compara a densidade local $\rho(\mathbf{x},t)$ com a densidade média do Universo $\bar\rho(t)$ naquele instante. Por definição, **sobredensidades** têm $\delta > 0$ (regiões que vão colapsar) e **subdensidades** têm $\delta < 0$ (os _voids_ da teia cósmica — ver Aula 01; como $\delta$ é limitado inferiormente em $-1$, regiões subdensas nunca "esvaziam" completamente, apenas se expandem mais rápido que a média e ficam cada vez mais rarefeitas em relação ao resto do Universo).

O colapso é **hierárquico**: estruturas menores colapsam primeiro (porque suas flutuações de densidade atingem o limiar não linear mais cedo) e depois se agregam em estruturas maiores. Isso aparece no valor de $\delta$ necessário para cada escala descolar do fundo:

| Escala | Contraste de densidade típico para colapso |
|---|---|
| Galáxia | $\delta \sim 10^5\text{–}10^6$ |
| Aglomerado de galáxias | $\delta \sim 100$ |
| Superaglomerado | $\delta \sim 1$ |

Ou seja: quanto maior a escala, menor o contraste de densidade necessário para começar a colapsar — o que explica por que galáxias individuais já estão totalmente formadas e virializadas enquanto superaglomerados ainda estão em processo de colapso hoje.

> [!tip] Por que a matéria escura fria (CDM) importa aqui?
> A **matéria escura fria** (_Cold Dark Matter_) não sente pressão de radiação nem colide eletromagneticamente — ela só interage gravitacionalmente. Isso permite que pequenas flutuações de densidade cresçam livremente desde cedo, sem serem "apagadas" por pressão, e é exatamente o que possibilita esse cenário de **colapso hierárquico bottom-up** (pequeno → grande). Sem CDM, seria muito mais difícil formar estrutura em tempo hábil no Universo.

---

## 2. Classificação morfológica e populações de galáxias

### A sequência de Hubble não é evolutiva

O **esquema de classificação de Hubble** (o "diapasão" morfológico — elípticas, lenticulares, espirais, irregulares) organiza galáxias por _forma_, não por _idade_ ou _estágio evolutivo_. É um erro comum (e importante de evitar) interpretar a sequência de Hubble como uma linha do tempo — uma galáxia não "nasce" elíptica e "vira" espiral, nem o contrário, em uma progressão simples.

### Cor × massa: Blue Cloud, Green Valley, Red Sequence

Uma forma mais robusta de descrever a _evolução_ de uma população de galáxias é o diagrama **cor × massa estelar** (o análogo, em galáxias, do diagrama cor-magnitude estelar visto na nota de Arqueologia Galáctica). Nele, aparecem três regiões bem definidas:

- **Blue Cloud (nuvem azul):** galáxias azuis, com gás e formação estelar ativa — tipicamente espirais.
- **Red Sequence (sequência vermelha):** galáxias vermelhas, sem gás frio, população estelar velha — tipicamente elípticas (mesma sequência vermelha já vista na Aula 01 como técnica de _detecção_ de aglomerados).
- **Green Valley (vale verde):** a região de transição, pouco povoada porque a travessia entre as duas é relativamente rápida — é justamente aí que vivem as galáxias "pegas no ato" de serem transformadas pelos mecanismos da próxima seção.

---

## 3. Mecanismos de transformação ambiental

O deslocamento **Blue Cloud → Green Valley → Red Sequence** é causado, em grande parte, pelo próprio ambiente do aglomerado. À medida que uma galáxia rica em gás cai em direção ao centro (movimento chamado **infall**, dentro de **grupos de infall** que se aglutinam ao aglomerado maior), ela é submetida a diversos mecanismos físicos que removem seu gás e desligam a formação estelar:

### Pressão de arraste (Ram Pressure Stripping)

Ao atravessar o **meio intra-aglomerado (ICM)** — o gás quente descrito na Aula 01 — a galáxia sente uma pressão de arraste análoga ao vento sentido por quem corre contra o ar:

$P_{\text{ram}} = \rho_{\text{ICM}}\, v^2$

onde $\rho_{\text{ICM}}$ é a densidade do gás do ICM e $v$ a velocidade da galáxia em relação a ele. Quando essa pressão supera a força gravitacional que prende o gás frio ao disco da galáxia, o gás é literalmente "arrancado" — processo descrito originalmente por **Gunn & Gott (1972)**. O desligamento (_quenching_) da formação estelar por esse mecanismo é rápido, em escalas de tempo de $\sim 100$ Myr.

> [!tip] Galáxias "água-viva" (Jellyfish Galaxies)
> Quando o arraste é forte o suficiente, o gás estripado forma longos rastros atrás da galáxia — visualmente parecidos com os tentáculos de uma água-viva, daí o apelido **jellyfish galaxies** (ou galáxias medusa). Dentro desses rastros, o gás comprimido durante o processo pode disparar surtos localizados de formação estelar (os chamados _**fireballs**_, nós compactos e brilhantes de formação estelar dentro da cauda estripada, que depois se apagam por erosão), e o próprio gás quente estripado emite em raio-X ao ser chocado e aquecido pelo ICM.

### Starvation (inanição)

Um mecanismo mais lento: mesmo sem arrancar o gás frio já presente no disco, o ICM pode impedir que o **halo quente** da galáxia continue resfriando e realimentando o disco com gás novo. Sem reposição, a galáxia consome seu estoque de gás remanescente e a formação estelar se apaga gradualmente, em escalas de $\sim 1$–$3$ Gyr — um caminho mais lento (mas igualmente eficaz) rumo à sequência vermelha.

### Harassment (assédio galáctico)

Encontros gravitacionais rápidos e próximos ("rasantes") entre galáxias dentro do aglomerado, repetidos ao longo de muitas órbitas. Cada encontro é breve, mas o efeito de maré cumulativo perturba a estrutura da galáxia, contribuindo para a alta dispersão de velocidades observada em aglomerados (ver teorema do virial, Aula 01) e arrancando gravitacionalmente estrelas das bordas dos discos — material que passa a compor a **luz intra-aglomerado (ICL)**, um "brilho difuso" de estrelas soltas que não pertencem a nenhuma galáxia individual.

### Fricção dinâmica

Diferente dos mecanismos acima (que agem sobre o _gás_), a fricção dinâmica desacelera a **galáxia como um todo**, sem qualquer contato físico: o movimento da galáxia pelo meio de matéria escura e outras galáxias cria uma esteira gravitacional (_wake_) que puxa a galáxia para trás, fazendo-a perder momento angular e espiralar lentamente em direção ao centro do aglomerado.

O resultado líquido de todos esses processos é a transformação sistemática **espiral azul (rica em gás, formando estrelas) → elíptica vermelha (sem gás, população estelar velha)** à medida que uma galáxia migra da periferia para o centro do aglomerado — a mesma relação morfologia-densidade introduzida na Aula 01, agora explicada em termos dos mecanismos físicos que a produzem.

---

## 4. O centro do aglomerado: BCG, cooling flows e feedback de AGN

No fundo do poço de potencial do aglomerado mora a **BCG** (_Brightest Cluster Galaxy_), tipicamente a galáxia mais massiva e luminosa do sistema. Ela cresce por **canibalismo galáctico**: fusões maiores (_major mergers_) e menores (_minor mergers_) sucessivas com galáxias que espiralam até o centro por fricção dinâmica, acumulando o "entulho" estelar de todo o aglomerado. Em casos extremos, esse crescimento produz uma **galáxia cD** — uma elíptica supermassiva com um envelope estelar difuso e extenso, misturado com a própria luz intra-aglomerado.

### O paradoxo dos cooling flows

O gás do ICM no núcleo do aglomerado é denso o suficiente para que seu **tempo de resfriamento radiativo** seja _menor_ que a idade do Universo (tempo de Hubble) — em princípio, isso deveria gerar um fluxo constante de gás esfriando e caindo no centro (um _cooling flow_), alimentando enormes taxas de formação estelar na BCG. Só que, na prática, observamos taxas de resfriamento e formação estelar muito **menores** do que essa previsão simples — o chamado **paradoxo observacional dos cooling flows**.

> [!tip] A resolução: feedback de AGN
> A solução aceita hoje é o **feedback do núcleo galáctico ativo (AGN)**: o **buraco negro supermassivo (SMBH)** na BCG, ao acretar matéria, libera jatos e energia que reaquecem o gás do núcleo do aglomerado, contrabalançando o resfriamento radiativo e suprimindo o _cooling flow_ previsto — um mecanismo de autorregulação que conecta a física de escala de um único buraco negro à evolução de todo o aglomerado.

---

## 📌 Conceitos-chave

- **Contraste de densidade ($\delta$):** mede o quanto uma região se desvia da densidade média do Universo; $\delta>0$ colapsa, $\delta<0$ é um _void_.
- **Formação hierárquica:** estruturas menores colapsam primeiro e se agregam em estruturas maiores — viabilizada pela matéria escura fria (CDM).
- **Ram pressure stripping:** remoção do gás frio de uma galáxia pelo arraste do ICM ($P_{\text{ram}} = \rho_{\text{ICM}} v^2$), gerando galáxias "água-viva".
- **Starvation:** desligamento lento da formação estelar por corte do resfriamento do halo de gás quente.
- **Harassment:** perturbação cumulativa por encontros gravitacionais rápidos e repetidos, alimentando a luz intra-aglomerado (ICL).
- **Fricção dinâmica:** desaceleração gravitacional de uma galáxia pelo meio ao redor, sem contato físico.
- **BCG / galáxia cD:** galáxia central do aglomerado, formada por canibalismo galáctico sucessivo.
- **Feedback de AGN:** mecanismo que resolve o paradoxo dos _cooling flows_, reaquecendo o ICM central.

---

## ❓ Perguntas e discussões da aula

> [!question] Perguntas (Aula 2)
>
> 1. **O que são subdensidades?** R.: Regiões onde o contraste de densidade é negativo ($\delta < 0$), ou seja, menos densas que a média do Universo — correspondem aos _voids_ da teia cósmica (Aula 01). Como $\delta \geq -1$ por definição, elas nunca "esvaziam" totalmente: apenas se expandem mais rápido que a média cósmica.

---

## 🔗 Referências e correlatos

- [Slides oficiais da Aula 02 (PDF)](assets/escolainverno/aulas/mc4/L02.pdf)
- [Aula 01](pt-br/resource/escolainverno/aglomerados/aglomerados-aula01) — teorema do virial, ICM e detecção de aglomerados
- [Aula 03](pt-br/resource/escolainverno/aglomerados/aglomerados-aula03)
- [Cosmologia — Aula 03](pt-br/resource/escolainverno/cosmologia/cosmologia-aula03) — teia cósmica e estrutura em grande escala
- [Arqueologia Galáctica — Aula 01](pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula01) — diagrama cor-magnitude estelar, análogo ao diagrama cor × massa de galáxias visto aqui
