---
publish: true
title: Entendendo a Matéria Escura a partir de Choques Extragalácticos
created: 2023-03-01
tags:
  - materia-escura
  - aglomerados-de-galaxias
  - iniciacao-cientifica
---
# 💥 Entendendo a Matéria Escura a partir de Choques Extragalácticos

> [!note] Resumo
> Projeto de Iniciação Científica Júnior (CNPq/PIBIC-EM, Edital 94/2022), orientado pela Prof.ª Ana Cecília Soja no IFF Bom Jesus do Itabapoana. Testei a acurácia do código de Dawson et al. (2013) — que estima o tempo decorrido desde a colisão de dois aglomerados de galáxias via Monte Carlo — contra as simulações dinâmicas de ZuHone et al. (2018), como forma indireta de estudar o comportamento da matéria escura durante colisões extremas.

<div class="media-carousel">
  <a href="/pt-br/research/dark-matter-shocks" class="carousel-slide">
    <img src="/assets/illustrations/cosmologia.svg" alt="Choques de aglomerados de galáxias" />
    <div class="slide-caption">Choques de Aglomerados</div>
  </a>
</div>

## 🌌 O problema: como "ver" a matéria escura?

Aglomerados de galáxias são as maiores estruturas gravitacionalmente ligadas do Universo — e, quando dois deles colidem, o evento é um dos mais energéticos conhecidos. Numa colisão, os três componentes de um aglomerado (galáxias, gás intra-aglomerado e matéria escura) se comportam de formas diferentes: as galáxias, feitas de matéria normal mas muito esparsas entre si, atravessam-se quase sem interagir; o gás, também matéria normal, colide e é freado por atrito; e a matéria escura parece acompanhar as galáxias, mas não exatamente — evidência indireta de que ela interage pouco (ou nada) por vias além da gravidade. O exemplo mais famoso é o **Aglomerado da Bala**, cujas mapas de lentes gravitacionais mostram exatamente essa separação espacial entre os três componentes.

Como não é possível observar diretamente a matéria escura, nem repetir uma colisão de aglomerados em laboratório, a estratégia adotada é indireta: comparar **simulações dinâmicas** com **métodos estatísticos de estimativa de parâmetros observacionais** (massas relativas, redshift, separação projetada) e verificar se eles concordam.

## 🎯 Objetivo

Avaliar a **acurácia** do código de **Dawson (2013)** — que usa o método de Monte Carlo para estimar o tempo decorrido desde a primeira colisão de um par de aglomerados, a partir de parâmetros observacionais relativamente simples de obter — comparando seus resultados com o "gabarito" conhecido das simulações dinâmicas de alta resolução de **ZuHone et al. (2018)**.

## 🔧 Metodologia

O trabalho seguiu quatro etapas:

1. **Familiarização** com conceitos fundamentais de Astronomia (paralaxe, classificação espectral OBAFGKM, evolução estelar, classificação morfológica de galáxias de Hubble — elípticas, espirais, irregulares) e com o problema físico de aglomerados em colisão.
2. **Compilação e entendimento do código de Dawson** — validado primeiro contra o caso de referência do próprio Aglomerado da Bala (massas $1{,}5\times10^{14}$ e $1{,}5\times10^{15}\,M_\odot$, separação projetada de 720 kpc), reproduzindo o resultado original. A função central, `MCEngine`, recebe massas dos dois aglomerados, redshift e distância projetada, e gera $10^4$ amostras via Monte Carlo (convergência já observada a partir de $10^3$ iterações).
3. **Obtenção dos dados de ZuHone et al. (2018)** — o *Galaxy Cluster Merger Catalog*, um repositório de simulações hidrodinâmicas de fusões de aglomerados, organizado por razão de massa (1:1, 1:3, 1:10) e parâmetro de impacto (0, 500, 1000 kpc). O trabalho focou nas 3 simulações com parâmetro de impacto 0 kpc (colisão no plano do céu).
4. **Aplicação do método de Dawson** a cada uma das simulações de ZuHone, comparando o tempo pós-colisão estimado pelo código com o tempo real conhecido da simulação, com incerteza estimada via `np.quantile` sobre as $10^4$ amostras de Monte Carlo.

## 📊 Resultados

A simulação de ZuHone revela um padrão oscilatório: os aglomerados partem de separação máxima, colidem (linha preta, primeira colisão), voltam a se afastar até um novo máximo — menor que o primeiro, por perda de energia na colisão — e assim por diante.

| Razão de massas | Instante da 1ª colisão (Ganos) |
|---|---|
| 1:1 | 1,32 |
| 1:3 | 1,20 |
| 1:10 | 1,04 |

Comparando o código de Dawson com os dados de ZuHone no intervalo entre a primeira colisão e o afastamento máximo seguinte — a única janela em que o método de Dawson é aplicável — os resultados do código **concordam, dentro das incertezas, com a simulação para as três razões de massa testadas (1:1, 1:3 e 1:10)**.

> [!warning] Viés sistemático encontrado
> Apesar da boa concordância geral, os valores centrais estimados pelo código de Dawson mostraram uma **tendência sistemática a subestimar** o tempo real da simulação — um viés que precisa ser investigado com mais profundidade em trabalhos futuros, e que não invalida a viabilidade geral do método.

## 🧾 Conclusão

O método de Dawson (2013) mostrou-se **confiável dentro das incertezas** para estimar o tempo decorrido desde a colisão de aglomerados de galáxias, no intervalo de validade proposto pelo próprio método — mas com uma tendência sistemática de subestimação que merece investigação futura. A perspectiva natural é expandir a análise para os cenários de ZuHone com parâmetro de impacto não-nulo (colisões fora do plano do céu), ainda não testados neste trabalho.

## 🏆 Apresentações e prêmios

Este projeto foi apresentado na **FEBRACE 2023** e na **MOSTRATEC 2023** (Novo Hamburgo, RS) — ver [cobertura da MOSTRATEC](pt-br/media/2023/mostratec-2023).

## 🔗 Referências e correlatos

- Dawson, W. A. (2013) — *The Dynamics of Merging Clusters: A Monte Carlo Solution Applied to the Bullet and Musket Ball Clusters*, ApJ 772, 131. [Código MCMAC](https://github.com/MCTwo/MCMAC).
- ZuHone, J. et al. (2018) — *The Galaxy Cluster Merger Catalog: An Online Repository of Mock Observations from Simulated Galaxy Cluster Mergers*, ApJS 234, 4.
- Clowe, D. et al. — Aglomerado da Bala, evidência clássica de separação espacial entre matéria escura e gás.
- [MOSTRATEC 2023](pt-br/media/2023/mostratec-2023) — cobertura da apresentação deste projeto
- [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection) — outro projeto de pesquisa em Astronomia, também orientado por dinâmica/cinemática de sistemas gravitacionais
- [Simulando o Impacto de Satélites em Observações Astronômicas](pt-br/research/satellite-trail-removal) — projeto seguinte, também com foco computacional aplicado a dados astronômicos
- [Curso ON — Aula 05](pt-br/resource/curso-on/aula-05-avermelhamento-extincao-e-imf) — outro contexto de massa não-luminosa/matéria escura na Galáxia
