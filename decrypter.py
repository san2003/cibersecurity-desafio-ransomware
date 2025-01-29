import os
import pyaes

# Nome do arquivo criptografado
encrypted_file_name = "teste.txt.enc"

# Ler a chave armazenada
with open("chave.key", "rb") as key_file:
    key = key_file.read()

# Abrir o arquivo criptografado
with open(encrypted_file_name, "rb") as file:
    encrypted_data = file.read()

# Inicializar AES no modo CTR para descriptografia
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografar os dados
decrypted_data = aes.decrypt(encrypted_data)

# Remover o arquivo criptografado
os.remove(encrypted_file_name)

# Criar o arquivo descriptografado
decrypted_file_name = "teste.txt"
with open(decrypted_file_name, "wb") as new_file:
    new_file.write(decrypted_data)

print(f"Arquivo descriptografado salvo como: {decrypted_file_name}")
