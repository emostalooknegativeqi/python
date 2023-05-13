import pyttsx3
print("digite o texto a ser dito")
texto = (input())
print("falando")
engine = pyttsx3.init()
engine.say(texto)
engine.runAndWait()
