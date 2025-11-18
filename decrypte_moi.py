messages_gr3 = {
    "pseudo" : "DebugWoman",
    "messages" : ["Rendez vous au point 8 à midi", "Plan B activer en cas de problème", "Le code maître est 2345"],
    "cryptes" : ["Uhqghc yrxv dx srlqw 1 à plgl", "Sodq E dfwlyhu hq fdv gh sureoèph", "Oh frgh pdîwuh hvw 4567"]
}

def dechiffrer(message):
    alphabet="abcdefghijklmnopqrstuvwxz"
    chiffres="123456789"
    for i in messages_gr3:
        if i in alphabet:
            position = alphabet.index(i)
            resultat+= alphabet[(position-3) %26]
        elif i in chiffres:
            position=chiffres.index(i)
            resultat +=alphabet [(position - 3)%10]
        else:
            resultat +=i
    return resultat




if __name__ == '__main__':

    print("Accusé-réception")
    print("Attention, le 3ieme message a été intercepté.")
    print("Nous accusons réception des messages 1et 2.")

