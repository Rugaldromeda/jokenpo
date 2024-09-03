import random
import os
# precisarei do cálculo pseudoaleatoriedade do python aplicada a uma lista de 3 elementos.

print("======================================================\n Bem vindo ao jogo de Pedra, Papel, Tesoura - JokenPo \n =====================================================")

placarVoce = 0
placarComputador = 0

dictPlays = [
    {"Jogada":"Pedra", "Número":0},
    {"Jogada":"Papel", "Número":1},
    {"Jogada":"Tesoura", "Número":2}                
]

def again():
    cont = int(input("Jogar novamente? 0 - CONTINUAR | 1 - SAIR \n"))
    if(cont == 0):
        os.system('cls') or None
        main()
    else:
        os.system('cls') or None
        exit()

def checkWin(play1,play2):
    calcWin = play1 - play2
    if(calcWin == -1 or calcWin ==2):
        print("Computador venceu!")
        placarComputador=+1
        print(placarComputador)
    elif(calcWin == 0):
        print("Empate!")
    else:
        print("Você venceu!")
        placarVoce=+1

def main():
    print("PLACAR: \n Você: {} \n Computador: {}".format(placarVoce,placarComputador))

    choice = int(input("Escolha seu lance: \n 0 - Pedra | 1 - Papel | 2 - Tesoura : "))

    choiceComputer = random.randint(0,2)

    print("======================\n Sua jogada: {} \n Jogada do computador: {} \n ======================".format(dictPlays[choice]["Jogada"],dictPlays[choiceComputer]["Jogada"]))
    checkWin(choice,choiceComputer)
    again()
main()