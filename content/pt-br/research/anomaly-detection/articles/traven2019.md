---
publish: false
title: Machine Learning para Binárias
created: 2026-07-18
modified: 2026-07-25T23:58:08.057-03:00
published: 2026-07-25T23:58:08.057-03:00
tags:
  - artigo
  - pesquisa
---

> [!note] Em resumo
> Revisão que organiza a taxonomia de machine learning (supervisionado/não supervisionado, discriminativo/generativo) e aplica esse ferramental à descoberta e caracterização de estrelas binárias espectroscópicas em meio milhão de espectros do levantamento GALAH.

_Traven, G. et al. (2019)_

## Síntese

Revisão que organiza o "zoológico" de técnicas de ML em dois eixos: supervisionado vs. não supervisionado e, dentro do supervisionado, discriminativo (mapeia dado→rótulo diretamente — regressão logística, SVM, florestas aleatórias) vs. generativo (produz dado a partir do rótulo — GANs, autoencoders variacionais). O artigo aplica esse ferramental a um problema concreto: encontrar estrelas binárias espectroscópicas (SB2/SB3) em ~587 mil espectros do levantamento GALAH.

Na parte não supervisionada, os autores testam um autoencoder para reduzir a dimensionalidade dos espectros a um mapa 2D — o resultado não separa as classes de forma útil. Trocam para t-SNE, que revela uma estrutura rica: aglomerados que correspondem, sem nenhum rótulo prévio, a binárias, gigantes pobres em metais, estrelas quentes de rotação rápida e bandas moleculares. O algoritmo de clustering DBSCAN então isola cada grupo automaticamente a partir do mapa. Comparando essa detecção não supervisionada com o método clássico (função de correlação cruzada, CCF), mostram que os dois são complementares — cada um encontra binárias que o outro perde.

Na parte generativa (supervisionada), usam The Cannon e The Payne para construir, a partir de rótulos conhecidos (temperatura, gravidade, metalicidade), um modelo data-driven do espectro de uma estrela solteira; somando dois desses espectros-modelo, geram um template de binária e o ajustam aos dados observados — o que permite identificar até binárias espectroscopicamente não resolvidas, cuja velocidade orbital não separa as linhas. A conclusão central do artigo, e talvez a mais importante para quem está aprendendo ML: intervenção humana continua indispensável, porque efeitos instrumentais e de redução de dados podem imitar a assinatura de uma binária e enganar o algoritmo. É a base metodológica do projeto de detecção de anomalias deste site (aprendizado de padrões em dados estelares) e também um bom material introdutório de ML aplicado, referenciado na página de [Machine Learning](pt-br/resource/computacao/machine-learning).

[Ver artigo original](https://ui.adsabs.harvard.edu/abs/2019MmSAI..90..327T)

## Citação

```bibtex
@ARTICLE{Traven2019,
       author = {{Traven}, G. and {{\v{C}}otar}, K. and {Merle}, T. and {Van der Swaelmen}, M. and {Ting}, Y.-S. and {GALAH Team}},
        title = "{Machine learning techniques meet binaries}",
      journal = {\memsai},
     keywords = {Stars: binaries: close, Stars: binaries: spectroscopic, methods: data analysis, methods: numerical, techniques: radial velocities, techniques: spectroscopic},
         year = 2019,
        month = jan,
       volume = {90},
        pages = {327},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2019MmSAI..90..327T},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```
