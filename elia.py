import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
import os
import time
import playsound3 as ps
import webbrowser
import subprocess

# Configura a API do Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
r = sr.Recognizer()

# Fala o texto gerado
def falar(text):
    tts = gTTS(text=text, lang='pt')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except:
        pass
    tts.save(filename)
    time.sleep(0.3)
    ps.playsound(filename)

# Escuta o microfone
def ouvir():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            texto = r.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {texto}")
            return texto.lower()
        except:
            return None

# Comandos locais
def executar_comando_local(comando):
    home = os.path.expanduser("~")

    if "navegador" in comando:
        webbrowser.open("https://www.google.com")
        falar("Abrindo o navegador.")
        return True

    elif "downloads" in comando:
        subprocess.Popen(["xdg-open", os.path.join(home, "Downloads")])
        falar("Abrindo sua pasta de downloads.")
        return True

    elif "documentos" in comando:
        subprocess.Popen(["xdg-open", os.path.join(home, "Documentos")])
        falar("Abrindo a pasta de documentos.")
        return True

    elif "música" in comando or "tocar música" in comando:
        subprocess.Popen(["xdg-open", os.path.join(home, "Música")])
        falar("Abrindo a pasta de músicas.")
        return True

    elif "calculadora" in comando:
        subprocess.Popen(["gnome-calculator"])
        falar("Calculadora aberta.")
        return True

    elif "terminal" in comando:
        subprocess.Popen(["gnome-terminal"])
        falar("Abrindo o terminal.")
        return True
    
    elif "spotify" in comando:
        subprocess.Popen(["spotify"])
        falar("Abrindo o Spotify.")
        return True

    elif "youtube" in comando:
        webbrowser.open("https://www.youtube.com")
        falar("Abrindo o Youtube.")
        return True

    return False

# Consulta Gemini
def get_gemini_response(texto):
    try:
        response = model.generate_content(texto)
        return response.text
    except:
        return "Desculpe, estou com dificuldades para responder no momento."

# Lida com comandos
def responder(texto):
    if "abrir" in texto or "abra" in texto:
        if executar_comando_local(texto):
            return
    else:
        resposta = get_gemini_response(texto)
        falar(resposta)

# Loop principal
if __name__ == "__main__":
    while True:
        texto = ouvir()
        responder(texto)