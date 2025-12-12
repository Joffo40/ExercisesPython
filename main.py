# Écrivez votre code ici !
import csv

import csv

with open('input.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:

        salaire=(float(ligne['heures_travaillees']))*15
        print(ligne['nom'] + "," + salaire )

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
