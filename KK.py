import speech_recognition as sr
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import time

# Define a palavra-chave que ativará a música
palavra_chave = "iniciar"
print("A hora atual é: ", time.time())
# Define o caminho do arquivo de música
caminho_musica = "ballin.mp3"

# Cria um objeto reconhecedor
r = sr.Recognizer()

# Inicia a gravação do áudio do microfone
with sr.Microphone() as source:
    print("Diga algo para iniciar a música!")
    while True:
        # Captura o áudio do microfone
        audio = r.listen(source)
        # Usa o reconhecedor de fala do Google para converter a fala em texto
        try:
            texto = r.recognize_google(audio, language='pt-BR')
            print("Você disse: " + texto)
            # Verifica se a palavra-chave foi dita
            if palavra_chave in texto:
                # Toca a música
                playsound("ballin.mp3")
                # Espera 10 segundos
                time.sleep(10)
                # Interrompe a reprodução da música
                play(AudioSegment.silent(duration=10))
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio")
        except sr.RequestError as e:
            print("Erro ao se comunicar com o serviço de reconhecimento de fala; {0}".format(e))
