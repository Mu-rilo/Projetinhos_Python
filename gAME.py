from cgitb import reset
from glob import glob
import imp
import os
import random
from colorama import Back, Style, Fore
from numpy import spacing

playAgain = "s"
plays = 0
whoplay = 1 # 1 = PLAYER | 2 = CPU
maxPlays = 9
victory = "n"
game = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def beginning():
    os.system('cls')
    print(Fore.LIGHTGREEN_EX + "------------------------------------")
    print("SEJA BEM-VINDO(A) AO JOGO DA VELHA!!")
    print("------------------------------------" + Fore.RESET)
    os.system('pause')

def trophy():
    print(Fore.MAGENTA + "       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       " + Fore.RESET)

def screen():
    global game
    global plays
    os.system('cls')
    print("    0   1   2")
    print("0:  " + game[0][0] + " | " + game[0][1] + " | " + game[0][2])
    print("   -----------")
    print("1:  " + game[1][0] + " | " + game[1][1] + " | " + game[1][2])
    print("   -----------")
    print("2:  " + game[2][0] + " | " + game[2][1] + " | " + game[2][2])
    print("JOGADAS: " + Fore.GREEN + str(plays) + Fore.RESET)

def playerMoves():
    global plays
    global whoplay
    global maxPlays
    if whoplay == 1 and plays < maxPlays:
        try:
            l = int(input("LINHA..: "))
            c = int(input("COLUNA.: "))
            while game[l][c] != " ":
                print("ERRO! ESPAÇO JÁ PREENCHIDO")
                l = int(input("LINHA..: "))
                c = int(input("COLUNA.: "))
            game[l][c] = (Fore.CYAN + "O" + Fore.RESET)
            whoplay = 2
            plays+=1
        except:
            print("JOGADA INVÁLIDA!")
            os.system('pause')

def cpuMoves():
    global plays
    global whoplay
    global maxPlays
    if whoplay == 2 and plays < maxPlays:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while game[l][c] != " ":
            l = random.randrange(0,3)
            c = random.randrange(0,3)
        game[l][c] = (Fore.RED + "X" + Fore.RESET)
        plays+=1
        whoplay = 1

def verifyVictory():
    global game
    vit = "n"
    symbols = [(Fore.CYAN + "O" + Fore.RESET),(Fore.RED + "X" + Fore.RESET)]
    for s in symbols:
        vit = "n"
        il = ic = 0
        while il < 3:
            sum = 0
            ic = 0
            while ic < 3:
                if(game[il][ic] == s):
                    sum+=1
                ic+=1
            if(sum == 3):
                vit = s
                break
            il+=1
        if(vit != "n"):
            break
        il = ic = 0
        while ic < 3:
            sum = 0
            il = 0
            while il < 3:
                if(game[il][ic] == s):
                    sum+=1
                il+=1
            if(sum == 3):
                vit = s
                break
            ic+=1
        if(vit != "n"):
            break
        sum = 0
        indag = 0
        while indag < 3:
            if(game[indag][indag] == s):
                sum+=1
            indag+=1
        if(sum == 3):
            vit = s
            break
        sum = 0
        indagl = 0
        indagc = 2
        while indagc >= 0:
            if(game[indagl][indagc] == s):
                sum+=1
            indagl+=1
            indagc-=1
        if(sum == 3):
            vit = s
            break
    return vit

def reset():
    global game
    global plays
    global whoplay
    global maxPlays
    global victory
    plays = 0
    whoplay = 1 # 1 = JOGADOR | 2 = CPU
    maxPlays = 9
    victory = "n"
    game = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

beginning()

while (playAgain == "s" or playAgain == "S"):
    while True:
        screen()
        playerMoves()
        cpuMoves()
        screen()
        victory = verifyVictory()
        if(victory != "n") or (plays >= maxPlays):
            break

    print(Fore.RED + "GAME OVER" + Fore.RESET)
    if(victory == (Fore.CYAN + "O" + Fore.RESET)):
        print(Fore.CYAN + "PARABÉNS! VOCÊ VENCEU!" + Fore.RESET)
        trophy()
    elif(victory == (Fore.CYAN + "O" + Fore.RESET)):
        print("CPU VENCEU!")
    else:
        print("EMPATE!")
    playAgain = input(Fore.LIGHTYELLOW_EX + "Deseja jogar novamente? [s/n]: " + Fore.RESET)
    if(playAgain == "n" or playAgain == "N"):
        print("FIM DO PROGRAMA!")
    reset()