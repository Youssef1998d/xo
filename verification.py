def verifCol(liste):
    for i in range(0,6,3):
        if "".join(liste[i:i+3])=="XXX" or "".join(liste[i:i+3])=="OOO":
            return True
    return False

def verifRow(liste):
    for i in range(3):
        if liste[i]+liste[i+3]+liste[i+6] == "XXX" or l[i]+l[i+3]+l[i+6] == "OOO":
            return True
    return False

def verifDiag(liste):
    if liste[0]+liste[4]+liste[8] == "OOO" or liste[0]+liste[4]+liste[8] == "XXX":
        return True
    elif liste[2]+liste[4]+liste[6] == "XXX" or liste[2]+liste[4]+liste[6] == "OOO":
        return True
    return False

def verifAllWin(liste):
    return verifCol(liste) or verifDiag(liste) or verifRow(liste)

def verifTie(liste):
    if not verifAllWin(liste) and "-" not in liste:
        return True
    return False
