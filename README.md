# 🔳 QR Code Link Converter

Aplicação em **Python com interface gráfica** que permite converter qualquer link em um **QR Code instantaneamente**.

O usuário apenas cola o link, gera o QR Code e pode salvar a imagem no computador.

---

## 🚀 Funcionalidades

* Converter **links em QR Code**
* Interface simples com **Tkinter**
* Pré-visualização do QR Code
* Salvar QR Code em **PNG**
* Validação básica de URL
* Aplicação leve e rápida

---

## 🧰 Tecnologias utilizadas

* Python
* Tkinter
* qrcode
* Pillow (PIL)

---

## 📦 Instalação

Clone o repositório:

```
git clone https://github.com/douglaslobatodev/qr-code-converter-python.git
```

Entre na pasta do projeto:

```
cd qr-code-converter-python
```

Instale as dependências:

```
pip install -r requirements.txt
```

---

## ▶️ Executar o programa

```
python app.py
```

A interface do gerador de QR Code será aberta.

---

## 🖼️ Gerar executável (.exe)

Para criar uma versão executável do programa:

Instale o PyInstaller:

```
pip install pyinstaller
```

Execute:

```
pyinstaller --onefile --windowed app.py
```

O executável será criado na pasta:

```
dist/
```

---

## 📁 Estrutura do projeto

```
qr-code-converter-python
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📌 Exemplo de uso

1. Digite ou cole um link
2. Clique em **Gerar QR Code**
3. Visualize o QR Code
4. Clique em **Salvar QR Code**

---

## 👨‍💻 Autor

Douglas Lobato
Analista de TI / Desenvolvedor

GitHub:
https://github.com/douglaslobatodev

---

## 📄 Licença

Este projeto é open-source e pode ser utilizado para fins educacionais e comerciais.
