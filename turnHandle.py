def flipPlayer(player):
    dic = {"O":"X", "X":"O"}
    return dic[player]

def initGame():
    first = (input("Choose the first player 'X' or 'O' : ")).upper
