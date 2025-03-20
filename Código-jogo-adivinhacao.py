import random
import os
 
os.system ("cls")
 
numerosecreto = random.randint (1,10)
 
 
tentativas = 0
maxtentativas = 3
 
 
jogador = input("Nome do jogador: ")
 
print("\nBem-vindo ao jogo de adivinhação, jogador")
print("Você tem 3 tentativas para adivinhar o número secreto de 1 a 10.\n")
 
while tentativas < maxtentativas:
 
    numerodigitado = int(input("escolha seu número: "))
 
    tentativas+= 1
    if numerodigitado > numerosecreto:
        print("O número secreto é menor!\n")
    elif numerodigitado < numerosecreto:
        print("O número secreto é maior!\n")
    else:
        print("\nParabéns,", jogador + "! Você acertou o número secreto:", numerosecreto)
        break