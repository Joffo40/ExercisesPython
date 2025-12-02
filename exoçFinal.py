from bs4 import BeautifulSoup



with open("index.html", 'r') as file:

    soup = BeautifulSoup(file, 'html.parser')

    listeProduits=soup.find_all('h2')

    #print(listeProduits)


    listeProduit=soup.find_all('h2')

    listePrix=soup.find_all("p",class_ = "price")


    print(listeProduits)
    print(listePrix)
    produit= dict()
    #listeProduits[0]=listeProduits[0].replace('<h2>','')
    
   # listePrix[0]=listePrix[0].replace('Prix: ',' ')
    #listePrix[1]=listePrix[1].replace('Prix: ',' ')
    #listePrix[2]=listePrix[2].replace('Prix: ',' ')
    
    
    
print(listeProduits[0])    
print(listePrix[0].replace("Prix: ","price"))
print(listeProduits[1]) 
print(listePrix[1].replace('Prix: ',' price'))
print(listeProduits[2]) 
print(listePrix[2].replace('Prix: ',' price'))
print (listePrix)