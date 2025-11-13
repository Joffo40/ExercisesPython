
import operations

print("donnez la valeur a")

a = input()
a=int(a)

print("donnez la valeur b")
b = input()
b=int(b)

add=operations.addition(a,b)
mult=operations.multiplication(a,b)

print(f"Le resultat de l'addition est {add}")
print(f"Le resultat de la multiplication est {mult}")