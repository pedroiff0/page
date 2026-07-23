---
publish: true
password: "TROQUE-ESTA-SENHA"
title: "{{value}}"
created: {{DATE:YYYY-MM-DD}}
---
# 🔒 {{value}}

> [!note] Resumo
> 

> [!warning] Cada nota dentro desta pasta precisa da própria senha
> A proteção por senha do Quartz (plugin `encrypted-pages`) é por **arquivo**, não por pasta — não existe uma senha "de pasta" que proteja tudo automaticamente. Ao criar novas notas aqui dentro, copie o mesmo campo `password: "TROQUE-ESTA-SENHA"` (com a mesma senha desta página) no frontmatter de cada uma delas.
