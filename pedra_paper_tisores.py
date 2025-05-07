

import random

opcions = ["Pedra", "Paper", "Tisores"]

jugador_opcio = input("Escull: Pedra, Paper o tisores?")
ordinador_opcio = random.choice(opcions)

print("La teva elecció: ", jugador_opcio)
print("L'ordinadior ha tret: ", ordinador_opcio)

if jugador_opcio == ordinador_opcio:
    print("Empat!")
elif jugador_opcio == "Pedra" and ordinador_opcio == "Tisores":
    print("Guanyes!")
elif jugador_opcio == "Paper" and ordinador_opcio == "Pedra":
    print("Guanyes!")
elif jugador_opcio == "Tisores" and ordinador_opcio == "Paper":
    print("Guanyes!")
else:
    print("L'ordinador guanya, torna-ho a provar!")