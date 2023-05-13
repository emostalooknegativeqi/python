import pyttsx3
print("digite o texto a ser dito")
texto = (input())
print("falando")
engine = pyttsx3.init()
engine.say(texto)
engine.runAndWait()
if texto.endswith("ão"):
    engine.say("meu pau na sua mão kk")
    engine.runAndWait()
if texto.endswith("ido"):
    engine.say("meu pau no seu ouvido kk")
    engine.runAndWait()