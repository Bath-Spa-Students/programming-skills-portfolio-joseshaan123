pets=[]

pet = {
    'Species': 'Mammal',
    'name': 'Rambo',
    'owner': 'Shaan',
    'weight': 35,
    'Food': 'Meat',
}
pets.append(pet)

pet = {
    'Species': 'bird',
    'name': 'Annie',
    'owner': 'Jose',
    'weight': 2,
    'Food': 'seeds',
}
pets.append(pet)

pet = {
    'Species': 'Mammal',
    'name': 'Negan',
    'owner': 'Baiju',
    'weight': 10,
    'Food': 'Meat',
}
pets.append(pet)

for pet in pets:
    print(f"\nThings I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")