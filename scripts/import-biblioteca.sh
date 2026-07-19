#!/usr/bin/env bash
# Importa a biblioteca curada de PDFs abertos do vault hardcore-life para
# content/assets/biblioteca/, com nomes limpos (ASCII, sem espaços).
#
# Curadoria feita em 2026-07-19: cada arquivo desta lista teve a licença
# verificada no texto do próprio PDF (Rede e-Tec Brasil/MEC, Escola Técnica
# Aberta, UAB, CETAM, Creative Commons, ou permissão explícita do autor).
# Livros comerciais escaneados (Stewart, Halliday, Tanenbaum, Kurose, etc.)
# e material pessoal (Provas IFF) foram deliberadamente EXCLUÍDOS — não
# podem ser publicados num site público.
#
# Total: ~62 arquivos, ~330MB.
#
# Uso:  bash scripts/import-biblioteca.sh
# Depois: npx quartz build   (conferir)   e   npx quartz sync   (publicar)

set -euo pipefail

SRC="/home/pedro/Documentos/hardcore-life/05 - Recursos/Livros e Apostilas"
DST="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/content/assets/biblioteca"

copy() { # copy "origem relativa" area destino.pdf
  local rel="$1" area="$2" name="$3"
  mkdir -p "$DST/$area"
  if [[ -f "$SRC/$rel" ]]; then
    cp "$SRC/$rel" "$DST/$area/$name"
    echo "✓ $area/$name"
  else
    echo "✗ NÃO ENCONTRADO: $rel" >&2
  fi
}

# ---------- Computação ----------
copy "Computação/Fundamentos da Computação/978-65-87196-55-8.pdf" computacao fundamentos-computacao-cc.pdf
copy "Computação/Fundamentos da Computação/Introducao_a_computacao_COR_capa_ficha_20110502.pdf.pdf" computacao introducao-a-computacao-etec.pdf
copy "Computação/Informática Básica/Perifericos_Suprimentos_capa_FICHA_ISBN_20110128.pdf" computacao perifericos-e-suprimentos-etec.pdf
copy "Computação/Lógica de Computação/SI_Alexandre_FundamentosLogicaMat.pdf" computacao fundamentos-logica-matematica-uab.pdf
copy "Computação/Programação/Lógica/Logica_programacao_COR_CAPA_ficha_ISBN_20130910_marca_corte.pdf" computacao logica-de-programacao-etec.pdf
copy "Computação/Programação/Lógica/15.8_versao_Final_com_ISBN-Tecnicas_Programacao_07.07.14.pdf" computacao tecnicas-de-programacao-ifro.pdf
copy "Computação/Programação/C++/apostilaC.pdf" computacao linguagem-c-descomplicada-backes.pdf
copy "Computação/Programação/C++/apostilacpp_2019 (1).pdf" computacao apostila-cpp-unesp.pdf
copy "Computação/Programação/C++/treinamento-cpp.pdf" computacao treinamento-cpp-cc.pdf
copy "Computação/Programação/C++/Curso de Introdução à Programação em C++.pdf" computacao curso-intro-cpp-ufrgs.pdf
copy "Computação/Programação/C++/NotasAula.pdf" computacao notas-aula-cpp-ufpr.pdf
copy "Computação/Programação/C++/slago-C++.pdf" computacao linguagem-cpp-slago.pdf
copy "Computação/Programação/C++/Estrutura de dados_COR_CAPA_ficha_ISBN_20130814.pdf" computacao estrutura-de-dados-etec.pdf
copy "Computação/Programação/C++/15.3_versao_Final_com_ISBN-Estrutura_de_Dados_07.07.14.pdf" computacao estrutura-de-dados-ifro.pdf
copy "Computação/Programação/Java/Intro_Progr_OrientadaObjetos_COR_CAPA_FICHA_ISBN_20130813.pdf" computacao intro-poo-java-etec.pdf
copy "Computação/Programação/Python/Fundamentos_de_Lógica_e_Algoritmo_-_com_ISBN.pdf" computacao fundamentos-logica-algoritmo-etec.pdf
copy "Computação/Programação/Programação Web/ProgramacaoWeb_miolo_gráfica.pdf" computacao programacao-web-etec.pdf
copy "Computação/Programação/Programação Web/Aplicativos_para_Web_II_COR_CAP_FICHA_ISBN_20130918.pdf" computacao aplicativos-web-2-etec.pdf
copy "Computação/Programação/Programação Web/150.Web Design - INFORMÁTICA - UTFPR.pdf" computacao web-design-utfpr.pdf
copy "Computação/Programação/Programação Web/87.Projeto Sistemas Web - INFORMÁTICA - IFRO.pdf" computacao projeto-sistemas-web-ifro.pdf
copy "Computação/Banco de Dados/Introducao_banco_dados_ISBN.pdf" computacao introducao-banco-de-dados-etec.pdf
copy "Computação/Banco de Dados/Banco_de_Dados_I_COR_CAPA_ficha_ISBN_20130918.pdf" computacao banco-de-dados-1-etec.pdf
copy "Computação/Análise e Desempenho de Sistemas/Análise e Projeto de Sistemas - IFB.pdf" computacao analise-projeto-sistemas-ifb.pdf
copy "Computação/Análise e Desempenho de Sistemas/Analise_de_Sistemas_COR_capa_ficha_ISBN_20120903.pdf" computacao analise-de-sistemas-etec.pdf
copy "Computação/Análise e Desempenho de Sistemas/Projeto_de_Sistemas_COR_CAPA_ficha_ISBN_20130918.pdf" computacao projeto-de-sistemas-etec.pdf
copy "Computação/Arquitetura de Computadores/OrganizacaoArqComputadores_COR_capa_ficha_ISBN_20111020.pdf" computacao organizacao-arquitetura-computadores-etec.pdf
copy "Computação/Circuitos/Circuitos_Digitais_COR_CAPA_FICHA_ISBN_20130510.pdf" computacao circuitos-digitais-etec.pdf
copy "Computação/Redes/15.5_versao_Finalizada-Redes_Computadores_21.07.15.pdf" computacao redes-de-computadores-ifro.pdf
copy "Computação/Redes/Redes_computadores_II_ISBN.pdf" computacao redes-de-computadores-2-etec.pdf
copy "Computação/Redes/Protocolos_e_Serviços_de_Redes_marcadecorte.pdf" computacao protocolos-servicos-redes-etec.pdf
copy "Computação/Sistemas Operacionais/Introducao_Linux_COR_capa_20090602_ISBN.pdf.pdf" computacao introducao-ao-linux-etec.pdf
copy "Computação/Sistemas Operacionais/15.7_versao_Diagramada_para_impressao_ISBN-Sistemas_Operacionais_04.03.15.pdf" computacao sistemas-operacionais-ifro.pdf
copy "Computação/Sistemas Operacionais/Sistemas_Operacionais_II_COR_CAPA_FICHA_ISBN_20130916.pdf" computacao sistemas-operacionais-2-etec.pdf
copy "Computação/Segurança da Informação/15.6_versao_Finalizada_com_Logo_IFRO-Seguranca_Informacao_04_04_14.pdf" computacao seguranca-da-informacao-ifro.pdf
copy "Computação/Prática Profissional/15.9_versao_Final_com_ISBN-Orientacao_Pratica_Profissional_Pesquisa_07.07.14.pdf" computacao orientacao-pratica-profissional-ifro.pdf

# ---------- Matemática ----------
copy "Cálculos/matematicabasica.pdf" matematica formulario-matematica-basica.pdf
copy "Cálculos/revisaocalc.pdf" matematica revisao-calculo.pdf
copy "Cálculos/Cálculo III/livro.pdf" matematica calculo-3-livro-aberto.pdf
copy "Cálculos/Cálculo Numérico/Calculo_Numerico_Python_final.pdf" matematica calculo-numerico-python-ifsc.pdf
copy "Cálculos/Equações Diferenciais/eBook_Equacoes_Diferenciais-Licenciatura_Matematica_UFBA.pdf" matematica equacoes-diferenciais-ufba.pdf
copy "Probabilidade e Estatística/ESTATISTICA_I.pdf" matematica estatistica-1-etec.pdf
copy "Probabilidade e Estatística/ESTATISTICA_APLICADA.pdf" matematica estatistica-aplicada-etec.pdf

# ---------- Física ----------
copy "Físicas/FundamentosdeFisica_COR_capa_ficha_ISBN_20120808.pdf" fisica fundamentos-de-fisica-etec.pdf

# ---------- Eletricidade / Eletrônica ----------
copy "Eletricidade Aplicada/Fundamentos_Eletricidade_COR_ISBN_20110729.pdf" eletroeletronica fundamentos-eletricidade-etec.pdf
copy "Eletrônica/64.Nocoes Basicas Eletrotecnica - METALURGIA - IFPA.pdf" eletroeletronica nocoes-eletrotecnica-ifpa.pdf
copy "Eletrônica/Principios_Basicos_Eletronica_01_09_15.pdf" eletroeletronica principios-basicos-eletronica-etec.pdf
copy "Eletrônica/INTRODUÇÃO A TECNOLOGIAS DE ENGENHARIAS.pdf" eletroeletronica eletronica-1-cetam.pdf
copy "Eletricidade Aplicada/ELETRICIDADE.pdf" eletroeletronica eletronica-3-cetam.pdf
copy "Eletrônica/INSTRUMENTAÇÃO ELETRÔNICA - CIRCUITOS ELÉTRICOS.pdf" eletroeletronica eletronica-5-cetam.pdf

# ---------- Ciências ----------
copy "Ciências/Ciências Ambientais/Ciencias_Ambientais_para_Engenharia.pdf" ciencias ciencias-ambientais-para-engenharia.pdf

# ---------- LaTeX / Escrita ----------
copy "LaTeX/apostila_latex.pdf" latex-escrita apostila-latex-ufes.pdf
copy "LaTeX/introtikz.pdf" latex-escrita figuras-diagramas-tikz-ufpb.pdf
copy "LaTeX/biblatex-cheatsheet.pdf" latex-escrita biblatex-cheatsheet.pdf
copy "Escrita/ABNT/biblatex-abnt.pdf" latex-escrita biblatex-abnt-manual.pdf
copy "Escrita/ABNT/ABNT-GUIA-COMPLETO-Elaborar-formatar-trabalho-cientifico.pdf" latex-escrita guia-abnt-puc-minas.pdf
copy "Escrita/ABNT/manual_de_normalizacao_abnt.pdf" latex-escrita guia-abnt-unip.pdf

# ---------- Astronomia ----------
copy "Astronomia/2020_maciel_fund_evol_quim_galaxia.pdf" astronomia maciel-evolucao-quimica-galaxia.pdf

echo ""
echo "Concluído. Tamanho total da biblioteca:"
du -sh "$DST"
