fruits = {}

fruits['ananas'] = "jaune"

fruits['pomme'] = "orange"

fruits['tomate'] = "rouge"

fruits['kiwi'] = "vert"

couleurAnanas = fruits['ananas']

fruits['pomme'] = "vert"

del fruits["ananas"]

print(fruits)

print(f"couleurAnanas = {couleurAnanas}")