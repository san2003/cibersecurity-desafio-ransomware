import os
import pyaes
import secrets

# Abrir o arquivo original
file_name = "teste.txt"
with open(file_name, "rb") as file:
    file_data = file.read()

# Gerar uma chave de 16 bytes (128 bits) e salvar em um arquivo
key = secrets.token_bytes(16)
with open("chave.key", "wb") as key_file:
    key_file.write(key)

# Inicializar AES no modo CTR
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar os dados
crypto_data = aes.encrypt(file_data)

# Remover o arquivo original
os.remove(file_name)

# Criar o arquivo criptografado
encrypted_file_name = f"{file_name}.enc"
with open(encrypted_file_name, "wb") as new_file:
    new_file.write(crypto_data)

print(f"Arquivo criptografado salvo como: {encrypted_file_name}")
print(f"Chave de descriptografia salva em: chave.key")
