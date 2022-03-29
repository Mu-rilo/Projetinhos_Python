from operator import le
import random
import os
from colorama import Fore, Style, Back

pergunta = input("Deseja rodar o dado? [s/n]: ")

while True: 
    while pergunta == "s" or pergunta == "S":
        os.system('cls')
        print("Você tirou o número: " + Fore.LIGHTGREEN_EX + str(random.randrange(1,7)) + Fore.RESET)
        pergunta = input("Deseja rodar o dado? [s/n]: ")
        
    if pergunta == "n" or pergunta == "N":
        print(Fore.LIGHTRED_EX + "Fim do programa!" + Fore.RESET)
        break
    else:
        print("COMANDO INVÁLIDO!")
        os.system('pause')
        pergunta = input("Deseja rodar o dado? [s/n]: ")