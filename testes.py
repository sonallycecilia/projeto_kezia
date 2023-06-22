import os

nome_banco_dados = 'C:\Users\sonal_rkyba0o\OneDrive\Documentos\Vs projects\projeto_kezia\Sistema_cadastro.db'

# Verifica se o arquivo do banco de dados existe
if os.path.exists(nome_banco_dados):
    # Exclui o arquivo do banco de dados
    os.remove(nome_banco_dados)
    print("Banco de dados excluído com sucesso!")
else:
    print("O banco de dados não existe.")