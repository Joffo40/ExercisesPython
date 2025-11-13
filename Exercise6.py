print("Saisissez des chiffres séparés par une virgule:")
chaine=input()

liste=chaine.split(',')

listeEntier=[]
n=0
for chiffre in liste:
    chiffre=int(chiffre)
    listeEntier.append(chiffre)
    n=n+1
m=0
somme=0
for chiffreEntier in listeEntier:

    somme=somme+ listeEntier[m]
    m=m+1

print(f"La somme est egale à {somme}")

moyenne=somme/(n+1)

print(f"La moyenne est egale à {moyenne}")
nombreSup=0
j=0
for chiffreEntier in listeEntier:

    if chiffreEntier>moyenne:
        nombreSup=nombreSup+1
j=j+1
print(f"Il y a {nombreSup} supperieur à la moyenne")