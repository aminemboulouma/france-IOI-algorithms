texte = input()
# Trouver la lettre la plus frequente
nbOccurrences = [0] * 26
for idCaractere in range(len(texte)):
    caractereLu = texte[idCaractere]
    if caractereLu.isalpha():
        indiceLettre = ord(caractereLu.upper()) - ord("A")
        nbOccurrences[indiceLettre] = nbOccurrences[indiceLettre] + 1
indiceLettreMaxOcc = 0
for indiceLettre in range(26):
    if nbOccurrences[indiceLettre] > nbOccurrences[indiceLettreMaxOcc]:
        indiceLettreMaxOcc = indiceLettre

# On connait le decalage !
decalage = -(indiceLettreMaxOcc - (ord("E") - ord("A")))
# Decodage
for idCaractere in range(len(texte)):
    caractere = texte[idCaractere]
    if caractere.isalpha():
        isMaj = caractere.isupper()
        if isMaj:
            caractere = caractere.lower()
        numero = (ord(caractere) - ord("a") + decalage) % 26
        caractere = chr(numero + ord("a"))
        if isMaj:
            caractere = caractere.upper()
    print(caractere, end="")
print()