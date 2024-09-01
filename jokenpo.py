import random
# precisarei do cálculo pseudoaleatoriedade do python aplicada a uma lista de 3 elementos.

print("======================================================\n Bem vindo ao jogo de Pedra, Papel, Tesoura - JokenPo \n =====================================================")

placarVoce = 0
placarComputador = 0

dictPlays = [
    {"Jogada":"Pedra", "Número":0},
    {"Jogada":"Papel", "Número":1},
    {"Jogada":"Tesoura", "Número":2}                
]

print("PLACAR: \n Você: {} \n Computador: {}".format(placarVoce,placarComputador))


choice = int(input("Escolha seu lance: \n 0 - Papel | 1 - Pedra | 2 - Tesoura"))

choiceComputer = random.randint(0,3)