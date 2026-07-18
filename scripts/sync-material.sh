#!/usr/bin/env bash
# Copies one file from the hardcore-life vault into content/assets, for
# publishing a single, already-vetted material on a Recursos topic page.
#
# This is deliberately NOT a bulk mirror. Most of what lives in
# "05 - Recursos" is either copyrighted textbook scans or personal exam
# material — copying a whole folder blindly would republish both. Pick
# files one at a time, after checking they're actually safe to publish.
#
# Usage:
#   ./scripts/sync-material.sh "<path inside hardcore-life>" <topic-slug>
#
# Example:
#   ./scripts/sync-material.sh \
#     "05 - Recursos/Livros e Apostilas/Computação/Machine Learning/meu-resumo.pdf" \
#     machine-learning
#
# Result: copies the file into content/assets/computacao/<topic-slug>/,
# ready to link from content/pt-br/resource/computacao/<topic-slug>.md.

set -euo pipefail

VAULT_ROOT="/home/pedro/Documentos/hardcore-life"
SITE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST_BASE="$SITE_ROOT/content/assets/computacao"

if [[ $# -ne 2 ]]; then
  echo "Uso: $0 \"<caminho dentro de hardcore-life>\" <topic-slug>"
  echo "Exemplo: $0 \"05 - Recursos/Livros e Apostilas/Computação/Machine Learning/arquivo.pdf\" machine-learning"
  exit 1
fi

REL_PATH="$1"
TOPIC_SLUG="$2"
SRC="$VAULT_ROOT/$REL_PATH"

if [[ ! -f "$SRC" ]]; then
  echo "Erro: arquivo não encontrado em: $SRC"
  exit 1
fi

TOPIC_PAGE="$SITE_ROOT/content/pt-br/resource/computacao/$TOPIC_SLUG.md"
if [[ ! -f "$TOPIC_PAGE" ]]; then
  echo "Aviso: não existe uma página de tópico em content/pt-br/resource/computacao/$TOPIC_SLUG.md"
  echo "Confira se o slug está certo antes de continuar."
  exit 1
fi

FILENAME="$(basename "$SRC")"

# Basic safety net: flag filenames that look personal or copyrighted before copying.
# Not exhaustive — always double-check the actual content, not just the name.
SUSPICIOUS_PATTERN='(?i)(prova|avalia[cç][aã]o|exame|recupera[cç][aã]o|correc[aã]o|pedro henrique|rocha de andrade|z-lib|kupdf|pdfcoffee|toaz\.info|scribd)'
if echo "$FILENAME" | grep -qP "$SUSPICIOUS_PATTERN"; then
  echo "⚠️  Nome do arquivo bate com um padrão suspeito (pessoal ou de fonte pirata):"
  echo "    $FILENAME"
  echo "Revise o conteúdo com atenção antes de publicar. Copiando mesmo assim..."
fi

DEST_DIR="$DEST_BASE/$TOPIC_SLUG"
mkdir -p "$DEST_DIR"
cp -v "$SRC" "$DEST_DIR/$FILENAME"

echo ""
echo "✓ Copiado para: content/assets/computacao/$TOPIC_SLUG/$FILENAME"
echo ""
echo "Próximo passo: adicione um link pra esse arquivo na seção ## 📎 Materiais de"
echo "  content/pt-br/resource/computacao/$TOPIC_SLUG.md"
echo "Depois: npx quartz build (conferir) e npx quartz sync (publicar)."
