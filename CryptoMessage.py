'''
MESSAGE CRYPTOGRAPHING AND DECRYPTOGRAPHING SCRIPT - v1.0
Author: Mateus Cardoso Cypriano

Ideas:
1 - Menu to choose between cryptographing a message, decryptographing a message, generate a key (perharps)
2 - Crypto: Insert message (clear), insert key, return crypto message
3 - Decrypt: Insert crypto message, insert key, return message (clear)

edit:
1 - two options available: simple key and double key crypto/decrypt
2 - no key generation, the user must know beforehand

'''

# Adjust the key to the message length
def ajustar_chave(mensagem, chave):
    chave = (chave * (len(mensagem) // len(chave)) + chave[:len(mensagem) % len(chave)])
    return chave

# Crypto using simple key (one word)
def criptografar_simples(mensagem, chave):
    chave_ajustada = ajustar_chave(mensagem, chave)
    mensagem_cripto = ''.join(chr((ord(m) + ord(k)) % 256) for m, k in zip(mensagem, chave_ajustada))
    return mensagem_cripto

# Decrypt using simple key
def descriptografar_simples(mensagem_cripto, chave):
    chave_ajustada = ajustar_chave(mensagem_cripto, chave)
    mensagem_claro = ''.join(chr((ord(m) - ord(k)) % 256) for m, k in zip(mensagem_cripto, chave_ajustada))
    return mensagem_claro

# Crypto using double key (two words)
def criptografar_dupla(mensagem, chave1, chave2):
    # First step: crypto using the first key
    mensagem_cripto = criptografar_simples(mensagem, chave1)
    # Second step: crypto using the second key
    mensagem_cripto = criptografar_simples(mensagem_cripto, chave2)
    return mensagem_cripto

# Decrypt using double key
def descriptografar_dupla(mensagem_cripto, chave1, chave2):
    # First step: decrypt using the second key
    mensagem_cripto = descriptografar_simples(mensagem_cripto, chave2)
    # Second step: decrypt using the first key
    mensagem_claro = descriptografar_simples(mensagem_cripto, chave1)
    return mensagem_claro

# Interactive menu
def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Criptografar com chave simples")
        print("2 - Descriptografar com chave simples")
        print("3 - Criptografar com chave dupla")
        print("4 - Descriptografar com chave dupla")
        print("5 - Sair")
        escolha = input("Digite o número da opção: ")

        if escolha == '1':
            mensagem = input("Digite a mensagem que deseja criptografar: ")
            chave = input("Digite a chave (uma palavra): ")
            mensagem_criptografada = criptografar_simples(mensagem, chave)
            print(f"Mensagem criptografada: {mensagem_criptografada}")

        elif escolha == '2':
            mensagem_cripto = input("Digite a mensagem criptografada: ")
            chave = input("Digite a chave usada para criptografar: ")
            mensagem_decriptada = descriptografar_simples(mensagem_cripto, chave)
            print(f"Mensagem descriptografada: {mensagem_decriptada}")

        elif escolha == '3':
            mensagem = input("Digite a mensagem que deseja criptografar: ")
            chave1 = input("Digite a primeira chave (uma palavra): ")
            chave2 = input("Digite a segunda chave (uma palavra): ")
            mensagem_criptografada = criptografar_dupla(mensagem, chave1, chave2)
            print(f"Mensagem criptografada com chave dupla: {mensagem_criptografada}")

        elif escolha == '4':
            mensagem_cripto = input("Digite a mensagem criptografada: ")
            chave1 = input("Digite a primeira chave: ")
            chave2 = input("Digite a segunda chave: ")
            mensagem_decriptada = descriptografar_dupla(mensagem_cripto, chave1, chave2)
            print(f"Mensagem descriptografada com chave dupla: {mensagem_decriptada}")

        elif escolha == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()