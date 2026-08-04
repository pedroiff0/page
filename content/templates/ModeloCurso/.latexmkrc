# Arquivo de configuração canônico do Latexmk com proteção automática por senha (.pdf -> pdf protegido)
# Desenvolvido para o IFF Campus Bom Jesus do Itabapoana - Prof. Dr. Pedro Henrique Rocha de Andrade

$pdf_mode = 1; # PDFLaTeX por padrão (use 4 para LuaLaTeX ou 5 para XeLaTeX)
$interaction = "nonstopmode";
$halt_on_error = 1;

# Ao compilar com sucesso, executa automaticamente a criptografia com a senha padrão (escritaiff2026)
$success_cmd = "python3 -c \"from pypdf import PdfReader, PdfWriter; import sys, os; r=PdfReader('%D'); w=PdfWriter(); w.append_pages_from_reader(r); w.encrypt('escritaiff2026'); w.write('%D'); print('>>> PDF [%D] protegido automaticamente com a senha institucional.')\"";

# Extensões para limpar ao executar 'latexmk -c'
$clean_ext = "%R.nav %R.snm %R.vrb %R.fls %R.fdb_latexmk %R.synctex.gz";
