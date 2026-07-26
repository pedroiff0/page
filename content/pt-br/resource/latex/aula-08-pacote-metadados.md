---
publish: true
title: "Aula 08 — Arquivo de Preenchimento: metadados.sty"
created: 2026-07-26
tags:
  - latex
  - escrita
  - recursos
---

> [!note] Resumo
> A terceira peça do trio, e a única que o estudante realmente edita: `metadados.sty` não define nenhum comando novo — ele apenas **chama** os comandos de metadado já declarados por [`ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese), preenchendo cada um com o dado real do trabalho.

**Pré-requisito**: [Aula 06 — Classe `ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese) (para entender **o que** cada chamada aqui está configurando por baixo dos panos).

## 1. Por que um arquivo separado?

`ifftese.cls` já faz `\RequirePackage{metadados}` internamente (carregado automaticamente, sem precisar de `\usepackage` no `.tex` principal). A separação existe por um motivo pedagógico: o estudante deve poder configurar **todo** o trabalho — flags de comportamento, autoria, banca, ficha catalográfica — mexendo em um único arquivo simples, sem nunca precisar abrir a classe (que usa `\makeatletter`, `\csname`, fábricas de macro — conteúdo da Aula 06, não deste arquivo). `metadados.sty` é, na prática, uma lista de "preencha os espaços em branco".

```latex
\ProvidesPackage{metadados}[2026/06/12 Chamadas de Metadados do Estudante]
```

Repare que não há `\newcommand` nem `\makeatletter` neste arquivo — só chamadas a comandos que **já existem**, declarados pela classe.

## 2. Atalhos de notação científica

```latex
\newcommand{\feh}{[Fe/H]}
\newcommand{\mgfe}{[Mg/Fe]}
\newcommand{\teff}{$T_{\text{eff}}$}
\newcommand{\logg}{$\log g$}
\newcommand{\sel}{s$^{-1}$}
\newcommand{\estrela}{$\bigstar$s }
```

Esta é a única parte do arquivo que de fato **cria** comandos novos — mas são atalhos de conteúdo, não de configuração da classe: notações de astrofísica estelar (razões de abundância química, temperatura efetiva, gravidade superficial) repetidas dezenas de vezes ao longo de um texto científico, definidas uma vez para consistência e economia de digitação.

## 3. Flags comportamentais preenchidas

Cada chamada aqui liga uma das flags explicadas em detalhe na [Aula 06, §1.2](pt-br/resource/latex/aula-06-classe-ifftese#12-flags-comportamentais-declararcondicional):

```latex
\tipo{tcc}              % capa/contracapa/ficha no layout de TCC (não relatório)
\figuracaminho{img}      % \inserirfigura busca em img/
\numeracaoPorSecao{}     % vazio = "não": numeração contínua, não reinicia por seção
\cabecalho{sim}          % cabeçalho mostra o nome da seção
\corlink{sim}            % links do sumário/citações coloridos (verde/vermelho)
\legendacurta{sim}       % Lista de Figuras usa legenda curta separada da legenda do corpo
\sumarioescada{sim}      % sumário em escada (indentação progressiva por nível)
\frenteVerso{}           % vazio = "não": modo só-frente, sem forçar página ímpar
\capaiff{}               % vazio = "não": sem imagem de fundo institucional na capa
\numero{1}               % número do trabalho (relevante só para relatório técnico)
```

Um detalhe que vale destacar: como as flags são comparadas com `\ifdefstring{\flag}{sim}{...}`, deixar o valor **vazio** (`{}`) em vez de escrever `nao` tem exatamente o mesmo efeito prático — qualquer string diferente de `sim` cai no ramo "não" da comparação. Ambos os estilos aparecem neste arquivo (`\capaiff{}` vazio vs. poder-se-ia escrever `\capaiff{nao}`), o que mostra que a escolha é estética/de clareza, não funcional.

## 4. Autoria, curso e instituição

```latex
\aluno{}
\abreviaturanome{}
\abreviaturanomecompleto{}
\email{\href{mailto:pedroiff0@gmail.com}{pedroiff0@gmail.com}}

\ano{2026}
\instituicao{Instituto Federal de Ciência, Tecnologia e Educação Fluminense}
\shortinstituicao{Instituto Federal Fluminense}
\siglainstituicao{IFF}
\curso{Bacharelado em Engenharia de Computação}
\areaconcentracao{Engenharia de Computação}
\disciplinaFormatada{Trabalho de Conclusão de Curso}
\estado{RJ}
\estadocompleto{Rio de Janeiro}
\local{Bom Jesus do Itabapoana}
\campus{\textit{Campus} \tcc@local}
```

Note que `\instituicao` e `\shortinstituicao` guardam o mesmo dado em dois níveis de formalidade (nome completo do órgão vs. nome curto de uso corrente) — cada macro de capa/ficha/citação (Aula 07) escolhe qual dos dois usar conforme o contexto exige mais ou menos formalidade. `\campus` é um caso de metadado que **referencia outro metadado dentro do próprio valor** (`\tcc@local`), um padrão só possível porque a classe o declarou como `\@declararMetadadoComplexo` (Aula 06 §1.1) em vez de `\@criarMetadoBase` — do contrário, a referência a `\tcc@local` seria expandida prematuramente, antes de `\local{}` ter sido chamado.

## 5. Título e banca examinadora

```latex
\titulo{}
\subtitulo{}
\tituloingles{}
\palavraschave{}
\keywords{}

\orientador{}
\abreviaturaorientador{}
\siglainstituicaoorientador{}
\coorientador{}
\membrobancaum{}
\siglainstituicaomembroum{}
\membrobancadois{}
\dataaprovacao{\today}
```

Cada campo de banca vazio simplesmente **não aparece** na folha de assinaturas (`\banca`, Aula 07 §2.6) nem na contracapa — não é preciso comentar ou remover linhas para um trabalho sem coorientador ou com só um membro de banca, a lógica condicional já está na macro que consome esses valores, não aqui.

## 6. Campos de relatório técnico (não relevantes para TCC)

```latex
\dadosrelatorio{Dados do relatório técnico e/ou científico}
\classificacaoseguranca{}
\tiporelatorio{}
\datarelatorio{}
% ...
```

Este bloco inteiro só produz efeito visível se `\tipo` (§3) estiver configurado como `relatorio`/`relatoriotecnico` em vez de `tcc` — no arquivo real do autor, permanece preenchido com os valores-padrão da classe (a maioria vazios) simplesmente porque não se aplica ao caso de uso atual. Mantê-los aqui, mesmo vazios, documenta **quais campos existem** caso o mesmo arquivo de metadados precise, um dia, virar um relatório técnico em vez de um TCC.

## 7. Dados de catalogação (ficha catalográfica)

```latex
\tccCodigo{}
\tccBiblioteca{Biblioteca Anton Dakitsch}
\tccBib{CIP -- Catalogação na Publicação}
\tccSistema{Elaborada pelo Sistema de Geração Automática de Ficha Catalográfica da Biblioteca Anton Dakitsch do IFF com os dados fornecidos pelo(a) autor(a)}
```

Estes três últimos campos são textos praticamente fixos, específicos da biblioteca da instituição — preenchidos uma vez e, na prática, nunca alterados entre diferentes trabalhos do mesmo campus. `\endinput` fecha o arquivo, sinalizando ao LaTeX para ignorar qualquer coisa depois dessa linha (convenção padrão de fim de pacote).

---

## 🔗 Referências e correlatos

- [Aula 06 — Classe `ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese) — onde cada um destes comandos é de fato definido (fábricas de macro, flags condicionais).
- [Aula 07 — Pacote `macros.sty`](pt-br/resource/latex/aula-07-pacote-macros) — as macros de conteúdo (`\capa`, `\contracapa`, `\fichacatalografica`, `\banca`) que consomem estes metadados.
- [Curso — visão geral](pt-br/resource/latex)
- [Metodologia Científica e Tecnológica](pt-br/resource/engenharia-de-computação/8-periodo/metodologia-cientifica-e-tecnologica)
