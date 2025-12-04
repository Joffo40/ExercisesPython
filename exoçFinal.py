from bs4 import BeautifulSoup
import re


with open("index.html", 'r') as file:

    soup = BeautifulSoup(file, 'html.parser')

    listeProduits=soup.find_all('h2')

    #print(listeProduits)


    #listeProduit=soup.find_all('h2')

    listePrix=soup.find_all("p",class_ = "price")


    #print(listeProduits)
    #print(listePrix)
    #listeProduits[0]=listeProduits[0].replace('<h2>','')
    #listePrix[0]=listePrix[0].replace('Prix: ',' ')
    #listePrix[1]=listePrix[1].replace('Prix: ',' ')
    #listePrix[2]=listePrix[2].replace('Prix: ',' ')

    produits= {listeProduits[0]:listePrix[0],listeProduits[1]:listePrix[1],listeProduits[2]:listePrix[2]}
    #test= listeProduits.split("<h2>")
    #print(listeProduits[0].string)
    #print((listePrix)split)
    
    for num in range(3):
        print(listeProduits[num].string)
        affichage=(produits[listeProduits[num]].string.replace('Prix:',''))
        affichage=affichage.replace('€','')
        print(f'Prix {affichage} Euros')
        valeur=str(float(affichage)*1.2)
        print(f'Prix {valeur} Dollars')