from cryptography.fernet import Fernet
import os

# 1. Carregar a chave salva anteriormente pelo ransomware
def carregar_chave():
    try:
        return open("chave.key", "rb").read()
    except FileNotFoundError:
        print("Erro: O arquivo 'chave.key' não foi encontrado.")
        return None

# 2. Descriptografar um único arquivo
def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_encriptados = file.read()
    
    dados_restaurados = f.decrypt(dados_encriptados)
    
    with open(arquivo, "wb") as file:
        file.write(dados_restaurados)

# 3. Encontrar arquivos para restaurar
def encontrar_arquivos(diretorio):
    lista = []
    if not os.path.exists(diretorio):
        return lista

    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            # ATENÇÃO: Ajustamos aqui para o novo nome do arquivo!
            if nome not in ["ransomware.py", "descriptografar.py"] and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

# 4. Execução principal
def main():
    alvo = "test_files"
    chave = carregar_chave()
    
    if chave:
        arquivos = encontrar_arquivos(alvo)
        if arquivos:
            for arquivo in arquivos:
                descriptografar_arquivo(arquivo, chave)
            print(f"Sucesso: {len(arquivos)} arquivos restaurados em '{alvo}'.")
        else:
            print("Nenhum arquivo encontrado para restaurar.")

if __name__ == "__main__":
    main()
