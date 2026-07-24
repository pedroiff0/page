---
publish: true
title: "Aula 03"
titulo: Aglomerados-Aula03
disciplina: Astrofísica Extragaláctica
conteudo: O Universo Através das Lentes Gravitacionais — formalismo de lentes fracas e aglomerados em fusão como laboratórios de matéria escura autointeragente
professor: Rogério Monteiro-Oliveira
created: 2026-07-24T09:15:00-03:00
tags:
  - escola-de-inverno-on
  - astrofisica-extragalactica
  - aglomerados-de-galaxias
  - lentes-gravitacionais
  - materia-escura
cssclasses:
  - page-grid
  - center-images
---
# 🌌 Notas de Aula — Aglomerados de Galáxias (Aula 03)

> [!note] Resumo
> O formalismo matemático das lentes gravitacionais fracas — de como Newton nunca previu a deflexão da luz até o mapa de massa reconstruído hoje — e como aglomerados em colisão (como o Aglomerado Bala) funcionam como os únicos laboratórios astrofísicos capazes de testar se a matéria escura interage consigo mesma.

> [!info] Informações da aula
> **Tema:** O Universo Através das Lentes Gravitacionais (continuação de [[Aglomerados-Aula02|Aula 02]])
> **Professor:** Prof. Dr. Rogério Monteiro-Oliveira

---

## 🎯 Visão geral

A aula tem duas partes. Na primeira, o formalismo matemático das **lentes gravitacionais fracas** é construído passo a passo: partindo do ângulo de deflexão previsto pela Relatividade Geral (o dobro do valor newtoniano), até a **equação de lentes** $\beta(\theta) = \theta - \alpha(\theta)$ que relaciona a posição real de uma fonte de fundo à sua posição observada (distorcida). No regime fraco, essa distorção é tratada como uma transformação linear local, descrita pela convergência $\kappa$ (densidade de massa projetada) e o cisalhamento $\gamma$ (distorção da forma) — e o resultado prático é um mapa da distribuição de massa do aglomerado que revela, de forma independente de luz ou gás, que **~80% da massa é matéria escura**.

Na segunda parte, a aula muda de escala: aglomerados **em fusão** (como o famoso Aglomerado Bala) são apresentados como os únicos "laboratórios" astrofísicos capazes de testar se a matéria escura interage consigo mesma além da gravidade — um teste motivado por falhas conhecidas do modelo $\Lambda$CDM em pequena escala (problema núcleo-cúspide, problema da diversidade, "grande demais para falhar"). A ideia central: comparar o deslocamento pós-colisão entre os três componentes de um aglomerado (matéria escura via lentes, gás via raio-X, galáxias no óptico) permite estimar a seção de choque de autointeração da matéria escura, $\sigma/m$.

### 📑 Tópicos abordados
1. Breve contexto histórico das lentes gravitacionais (de Newton a Zwicky)
2. O ângulo de deflexão e a equação de lentes
3. Convergência, cisalhamento e o regime de lentes fracas
4. Aglomerados em fusão como laboratórios astrofísicos
5. Os problemas do $\Lambda$CDM em pequena escala e a matéria escura autointeragente (SIDM)
6. O Aglomerado Bala e a busca pela seção de choque de autointeração

---

## 1. Breve contexto histórico das lentes gravitacionais

Ao contrário da crença popular, **Newton não previu a deflexão gravitacional da luz** — a famosa pergunta em seu livro *Opticks* (1704) ("Não agem os corpos sobre a luz à distância, e por sua ação curvam seus raios...?") tratava, na verdade, de difração, não do efeito gravitacional que hoje conhecemos.

- **1804 — Soldner**: primeiro cálculo quantitativo, usando física newtoniana — previu um desvio de $0{,}84''$ (arcsegundos) para um raio de luz rasante ao Sol.
- **Einstein (Relatividade Geral)**: recalcula o ângulo de deflexão como $1{,}75''$ — exatamente o **dobro** do valor newtoniano.
- **1919 — Eclipse solar de Sobral (CE)**: a expedição liderada por Eddington mediu um desvio de $1{,}98 \pm 0{,}18''$, validando a Relatividade Geral contra a previsão newtoniana. No mesmo ano, **Oliver Lodge** cunhou o termo "lente" para o efeito.
- **Anos 1920–30 — Chwolson e Link**: sugeriram que alinhamentos perfeitos criariam "anéis" ou galáxias duplicadas (Link publicou 9 meses antes de Einstein). **Einstein (1936)** publicou o formalismo matemático completo, mas era pessimista: achava que o efeito nunca seria observável, por depender de alinhamentos raros entre estrelas individuais.
- **Fritz Zwicky** propõe usar **galáxias inteiras** como lentes, em vez de estrelas individuais — o que tornava o efeito observável (separações visíveis ao telescópio) e serviria como "balança" para medir a massa da própria galáxia-lente.
- **Walsh (1979)**: após o avanço de CCDs e radioastronomia, detecta o primeiro sistema de imagens múltiplas — um par de quasares idênticos criados pela deflexão de uma galáxia no caminho.

## 2. O ângulo de deflexão e a equação de lentes

O ângulo de deflexão previsto pela mecânica newtoniana é:

$$\hat\alpha_N = \frac{2GM}{c^2\xi}$$

enquanto a Relatividade Geral prevê o dobro:

$$\hat\alpha = \frac{4GM}{c^2\xi} = 2\,\hat\alpha_N$$

(essa diferença de fator 2 é exatamente o que a expedição de Sobral testou em 1919). A partir da geometria de lentes — envolvendo as distâncias-diâmetro-angular entre observador e lente ($D_d$), observador e fonte ($D_s$), e lente e fonte ($D_{ds}$) — chega-se à **equação de lentes**:

$$\beta(\theta) = \theta - \alpha(\theta)$$

que relaciona a posição real da fonte de fundo ($\beta$) à posição observada/distorcida da imagem ($\theta$), através do ângulo de deflexão $\alpha(\theta)$. O deflexão pode ser escrita como o gradiente de um **potencial gravitacional projetado** $\psi$ (a projeção 2D do potencial 3D da lente): $\nabla\psi = \alpha$, e o laplaciano desse potencial equivale ao dobro da convergência: $\nabla^2\psi = 2\kappa$.

## 3. Convergência, cisalhamento e o regime de lentes fracas

No **regime de lentes fracas**, a distorção morfológica das fontes de fundo é tratada como uma **transformação linear local**, descrita pela matriz Jacobiana $\mathcal{A} = \partial\beta/\partial\theta$, decomposta em dois ingredientes:

- **Convergência** $\kappa \equiv \Sigma/\Sigma_{cr}$ — a densidade de massa projetada da lente, em unidades da densidade crítica $\Sigma_{cr}$ (que faz a lente ser "forte" o suficiente pra formar múltiplas imagens quando $\kappa > 1$).
- **Cisalhamento (shear)** $\gamma \equiv \gamma_1 + i\gamma_2 = |\gamma|e^{2i\phi}$ — a distorção na forma (elipticidade) da fonte.

Como convergência e cisalhamento aparecem misturados no efeito observado, define-se o **cisalhamento reduzido** $g = \gamma/(1-\kappa)$, que é o que de fato se mede a partir da elipticidade observada das galáxias de fundo: na ausência de lentes, o valor esperado da elipticidade é zero, $E(e^{(s)}) = 0$; com lentes fracas, $E(e) \approx g \approx \gamma$. Na prática, a medida da forma das galáxias é feita em imagens monocromáticas profundas, com correção cuidadosa da **função de espalhamento de ponto (PSF)** do instrumento. O resultado final é um **mapa da distribuição de massa** do aglomerado — e, tipicamente, esse mapa revela que **~80% da massa é matéria escura**.

## 4. Aglomerados em fusão como laboratórios astrofísicos

Segundo o **cenário hierárquico** (já visto na [[Aglomerados-Aula02|Aula 02]]), aglomerados se formam a partir da fusão de estruturas menores — o que torna **aglomerados em processo de fusão** laboratórios particularmente ricos para: entender os detalhes desse cenário hierárquico, estudar os componentes do aglomerado separadamente, estudar o próprio ambiente de evolução das galáxias, e — o foco desta aula — investigar a **natureza da matéria escura**. Apenas sistemas astrofísicos desse tipo conseguem, hoje, investigar a **autointeração** da matéria escura.

## 5. Os problemas do $\Lambda$CDM em pequena escala e a matéria escura autointeragente (SIDM)

Apesar do sucesso do modelo padrão $\Lambda$CDM em grande escala, ele **falha em explicar algumas inconsistências em escala de galáxias**:

- **Problema núcleo-cúspide (core-cusp problem)**: simulações de CDM previm um perfil de densidade "pontudo" (cúspide) no centro de galáxias, mas observações mostram um núcleo mais "achatado" (*core*).
- **Problema da diversidade**: a diversidade observada nas curvas de rotação de galáxias de massa similar é maior do que a prevista pelas simulações de CDM puro.
- **Problema "grande demais para falhar" (too-big-to-fail)**: simulações preveem sub-halos massivos demais para não terem formado galáxias visíveis — mas essas galáxias não são observadas.

Há duas classes de solução: (a) específicas para cada problema, atribuindo-os a efeitos **bariônicos** (ex.: *feedback* de AGN redistribuindo matéria); ou (b) uma solução mais geral, alterando o próprio paradigma CDM para permitir que a matéria escura interaja consigo mesma **além da gravidade** — a chamada **SIDM (Self-Interacting Dark Matter)**, matéria escura autointeragente.

O desafio: como testar a SIDM se não temos matéria escura acessível em nosso ambiente local (laboratório)? A resposta: aglomerados em fusão.

## 6. O Aglomerado Bala e a busca pela seção de choque de autointeração

O **Aglomerado Bala** (1E 0657-56) é o exemplo clássico: nas imagens da colisão, a matéria escura (mapeada por lentes gravitacionais, em azul) aparece claramente separada do gás do ICM (visto em raio-X, em magenta) e das galáxias (vistas no óptico) — a evidência visual mais direta de que a maior parte da massa do aglomerado não acompanha o gás, que é freado pelo atrito durante a colisão.

Aglomerados em fusão funcionam como **grandes colisores de partículas**: a desvantagem é a baixa energia por partícula, mas a vantagem é o número descomunal de partículas de matéria escura envolvidas ($\sim 10^{70}$) — tornando-os o melhor lugar para testar a SIDM. A lógica da estimativa: comparando o quanto cada componente (matéria escura, gás, galáxias) se desloca após a colisão, é possível estimar (ou pelo menos colocar um limite de ordem de grandeza) na seção de choque de autointeração $\sigma/m$ da matéria escura — sendo que $\sigma/m|_{\text{gás}} \gg \sigma/m|_{\text{galáxias}}$ (o gás interage fortemente consigo mesmo via pressão/atrito hidrodinâmico, enquanto galáxias e matéria escura, em princípio, não colidem da mesma forma).

É exatamente esse tipo de anatomia pós-colisão — o deslocamento relativo entre os componentes, comparado com modelos físicos da colisão — que Rogério Monteiro-Oliveira pesquisa no Observatório Nacional: determinar com precisão a anatomia de aglomerados pós-colisão, integrando o mapeamento de massa via lentes fracas à dinâmica das galáxias membro (obtida via espectroscopia). A aula cita como exemplos os aglomerados **A1758**, **A3376** e **SPT-CL J0307-6225**.

> [!tip] Conexão com minha própria pesquisa
> Esse é exatamente o mesmo tipo de problema da minha pesquisa em [Entendendo a Matéria Escura a partir de Choques Extragalácticos](pt-br/research/dark-matter-shocks): o código de Dawson (2013) estima o tempo decorrido desde a colisão de um par de aglomerados (incluindo o próprio Aglomerado Bala como caso de referência) a partir de parâmetros observacionais — o mesmo tipo de "anatomia pós-colisão" discutida aqui, embora com foco na cronologia da colisão em vez da seção de choque de autointeração da matéria escura.

---

## ⚠️ Pontos de atenção

> [!important] Atenção
> *(nenhuma anotação registrada ainda)*

---

## 📌 Conceitos-chave

- **Ângulo de deflexão**: $\hat\alpha = 4GM/(c^2\xi)$ (Relatividade Geral) — o dobro do valor newtoniano $\hat\alpha_N = 2GM/(c^2\xi)$.
- **Equação de lentes**: $\beta(\theta) = \theta - \alpha(\theta)$, relaciona posição real e observada da fonte.
- **Convergência ($\kappa$)**: densidade de massa projetada, em unidades da densidade crítica $\Sigma_{cr}$.
- **Cisalhamento ($\gamma$) e cisalhamento reduzido ($g = \gamma/(1-\kappa)$)**: distorção na forma das fontes de fundo, o que de fato se mede observacionalmente.
- **Aglomerado Bala**: caso clássico de separação espacial entre matéria escura (lentes) e gás (raio-X) numa colisão de aglomerados.
- **SIDM (Self-Interacting Dark Matter)**: hipótese de que a matéria escura interage consigo mesma além da gravidade, motivada pelos problemas do $\Lambda$CDM em pequena escala (núcleo-cúspide, diversidade, "grande demais para falhar").
- **$\sigma/m$**: seção de choque de autointeração da matéria escura, estimada a partir do deslocamento relativo entre componentes de aglomerados em colisão.

---

## ❓ Perguntas e discussões da aula

> [!question] Perguntas (Aula 3)
> *(nenhuma pergunta registrada ainda)*

---

## 🔗 Referências e correlatos
- [Slides oficiais da Aula 03 (PDF)](assets/escolainverno/aulas/mc4/L03.pdf)
- [Página do Prof. Rogério Monteiro-Oliveira](https://www.monteiro-oliveira.com/talks)
- [Aula 01](pt-br/resource/escolainverno/aglomerados/aglomerados-aula01) — lentes fracas já introduzidas como técnica de detecção de aglomerados, e a descoberta da matéria escura por Zwicky
- [Aula 02](pt-br/resource/escolainverno/aglomerados/aglomerados-aula02) — o cenário hierárquico de formação de aglomerados
- [Raio-X e Enriquecimento Químico](pt-br/resource/escolainverno/palestras/raiox) — outra palestra sobre o ICM em aglomerados, visto aqui em raio-X em vez de lentes gravitacionais
- [Entendendo a Matéria Escura a partir de Choques Extragalácticos](pt-br/research/dark-matter-shocks) — minha própria pesquisa, mesmo objeto de estudo (anatomia pós-colisão de aglomerados) por outro método (cronologia via Dawson 2013, em vez da seção de choque de autointeração)
