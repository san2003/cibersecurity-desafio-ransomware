#  Desafio Ransomware - Criptografia e Descriptografia AES

Este projeto demonstra um sistema simples de criptografia e descriptografia de arquivos usando **AES (Advanced Encryption Standard)** no modo **CTR (Counter Mode)**. O código criptografa um arquivo de texto e gera uma chave secreta, que deve ser usada para descriptografar o arquivo posteriormente.

---

##  Tecnologias Utilizadas
- **Python 3**
- **PyAES** (Biblioteca para criptografia AES)

---

##  Instalação
1. **Clone este repositório:**
   ```sh
   git clone https://github.com/san2003/cibersecurity-desafio-ransomware.git
   cd cibersecurity-desafio-ransomware
   ```
2. **Instale as dependências:**
   ```sh
   pip install pyaes
   ```

---

##  Como Funciona a Criptografia

1. O script **`encrypt.py`**:
   - Lê o conteúdo do arquivo original (`teste.txt`).
   - Gera uma **chave AES de 16 bytes** e a salva em um arquivo `chave.key`.
   - Usa **AES-CTR** para criptografar os dados.
   - Salva o arquivo criptografado como `teste.txt.enc`.
   - Remove o arquivo original para simular um ataque ransomware.

### **Executar a Criptografia:**
```sh
python encrypt.py
```

Após a execução, o arquivo original será removido e um novo arquivo criptografado será gerado.

---

##  Como Funciona a Descriptografia

1. O script **`decrypt.py`**:
   - Lê a chave de descriptografia do arquivo `chave.key`.
   - Lê o arquivo criptografado `teste.txt.enc`.
   - Usa a chave correta para descriptografar os dados.
   - Salva o arquivo recuperado como `teste.txt`.
   - Remove o arquivo criptografado.

### **Executar a Descriptografia:**
```sh
python decrypt.py
```

Após a execução, o arquivo original será restaurado.

---

##  Importante
- **A chave de criptografia é essencial!** Sem o arquivo `chave.key`, não será possível recuperar o arquivo original.
- **Não compartilhe a chave secreta**, pois qualquer pessoa com acesso a ela poderá descriptografar seus arquivos.
- Este projeto é apenas para **fins educacionais** e não deve ser utilizado para atividades maliciosas.

---

##  Licença
Este projeto está licenciado sob a **MIT License**. Sinta-se à vontade para usá-lo e modificá-lo.

---


