# End Project of CS50P
import cowsay
import pyttsx3

engine = pyttsx3.init()
phrase = input("What's this? ")
cowsay.tux(phrase)
engine.say(phrase)
engine.runAndWait()