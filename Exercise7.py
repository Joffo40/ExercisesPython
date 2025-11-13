def salaire_mensuel(salaire_annuel):
    
    salaire_mensuel=float(salaire_annuel)/12

    return salaire_mensuel

def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire=float(salaire_mensuel)/4

    return salaire_hebdomadaire

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    salaire_horaire=float(salaire_hebdomadaire)/float(heures_travaillees)
    return salaire_horaire


print("Quel est votre salaire annuel")
salaire_annuel=input()
print("Quel sont vos heures")
heures_travaillees=input()




salaire_mensuel_value = salaire_mensuel(salaire_annuel)
salaire_hebdomadaire_value = salaire_hebdomadaire(salaire_mensuel_value)
salaire_horaire_value = salaire_horaire(salaire_hebdomadaire_value,heures_travaillees)

print(f"Le salaire mensuel est {int(salaire_mensuel_value)} euros")
print(f"Le salaire hebdomadaire est {int(salaire_hebdomadaire_value)} euros")
print(f"Le salaire horaire est {int(salaire_horaire_value)} euros")

