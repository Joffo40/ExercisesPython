print("Entrez votre nombre1 : ",end="")
nombre1 = input()
print("Entrez votre nombre2 : ",end="")
nombre2 = input()
if not(str.isnumeric(nombre1)) or not(str.isnumeric(nombre2)):
    #print(f"Le programme continue")
    raise SystemExit("Fin du programme")
    
else:
    print(f"Le programme continue")
    nombre1=int(nombre1)
    nombre2=int(nombre2)

print("Entrez l'operation : ",end="")
operation = input()
verification=(operation=="+") or (operation=="-") or  (operation=="*") or (operation=="/")
if not(verification) or (operation=="/"and nombre2==0):
    raise SystemExit("Fin du programme")
else:
    
    if (operation=="+"):
        resultat=nombre1 + nombre2
    elif (operation=="-"):
        resultat=nombre1 - nombre2
    elif (operation=="*"):
        resultat=nombre1 * nombre2
    else:
        resultat=nombre1 / nombre2
        resultat=round(resultat)

    print(f"Le resultat est {resultat}")