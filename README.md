# 🤖 Assistente Pessoal para Ubuntu

**Elia** é uma assistente pessoal por voz desenvolvida em Python, projetada para funcionar de forma fluida e natural no Ubuntu. Ela reconhece comandos de voz, interage com o modelo Gemini da Google e executa ações locais como abrir o navegador, pastas do sistema, terminal e muito mais.

---

## 🚀 Funcionalidades

- 🗣️ Reconhecimento de voz em português (Google Speech Recognition)
- 🧠 Respostas inteligentes via [Gemini](https://ai.google.dev/)
- 🗂️ Execução de comandos locais (navegador, pastas, programas)
- 🔊 Conversão de texto em fala com `gTTS`
- 💻 Compatível com Ubuntu e distribuições Linux

---

## 🛠️ Tecnologias utilizadas

- Python 3.12+
- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/)
- [`google.generativeai`](https://pypi.org/project/google-generativeai/)
- [`gTTS`](https://pypi.org/project/gTTS/)
- [`playsound3`](https://pypi.org/project/playsound3/)
- ALSA/JACK (áudio no Linux)

---

## ⚙️ Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/cayocesaras/assistente-ubuntu.git
cd assistente-ubuntu
```

### 2. Crie e ative o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Adicione sua chave da API Gemini

Edite o arquivo `elia.py` e substitua a linha:

```python
genai.configure(api_key="SUA_CHAVE_AQUI")
```

com sua chave da [Google AI Studio](https://makersuite.google.com/app).

---

## 🧪 Comandos disponíveis

- `Abrir navegador`
- `Abrir downloads`
- `Abrir documentos`
- `Abrir música`
- `Abrir terminal`
- `Abrir calculadora`
- `Perguntas serão respondidas usando o modelo gemini`

---

## 📌 Exemplo de uso

> 💬 Você diz:  
> `Abrir navegador`

> 🧠 Elia responde:  
> `Abrindo o navegador.`  
> *(E o navegador é aberto)*

---

## 💡 Contribuindo

Fique à vontade para sugerir melhorias, abrir issues ou enviar pull requests! A Elia está em constante evolução.

---

## 📜 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## ✨ Autor

Desenvolvido por [Cayo](https://github.com/cayocesaras) 🐍💻
