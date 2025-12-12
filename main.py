# Écrivez votre code ici !
import csv

entete=["nom", "salaire"]

with open('input.csv','r') as fichier_csv:
    
    reader = csv.DictReader(fichier_csv, delimiter=',')
    noms_textes=[]
    salaires_textes=[]
    for ligne in reader:
        noms_textes.append( ligne['nom'])
        salaires_textes.append(str(float(ligne['heures_travaillees'])*15))
           
print(noms_textes)
print(salaires_textes)
    
    
    
with open('output.csv','w') as fichierOutput_csv:


    writer = csv.writer(fichierOutput_csv, delimiter=',')
    writer.writerow(entete)   
    
    for nom, salaire in zip(noms_textes,salaires_textes):

    # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle

        ligne = [nom, salaire]

        writer.writerow(ligne)
    


#with open('input.csv') as fichier_csv:
    #reader = csv.DictReader(fichier_csv, delimiter=',')
    #for ligne in reader:

    #  salaire=str(float(ligne['heures_travaillees'])*15)
    #  print(ligne['nom'] + "," + salaire )

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
