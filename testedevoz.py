import pyttsx3

texto = "Hello World!"
engine = pyttsx3.init()
engine.say(texto)
engine.runAndWait()
