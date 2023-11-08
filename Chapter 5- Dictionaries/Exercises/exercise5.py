# Create an empty list called 'pets' to store information about pets.

# Define a dictionary 'pet' with information about a pet and append it to the 'pets' list.

pets=[]

pet = {
    'Species': 'Mammal',
    'name': 'Rambo',
    'owner': 'Shaan',
    'weight': 35,
    'Food': 'Meat',
}
pets.append(pet)

# Define another dictionary 'pet' with information about a different pet and append it to the 'pets' list.
pet = {
    'Species': 'bird',
    'name': 'Annie',
    'owner': 'Jose',
    'weight': 2,
    'Food': 'seeds',
}
pets.append(pet)

# Define one more dictionary 'pet' with information about another pet and append it to the 'pets' list.
pet = {
    'Species': 'Mammal',
    'name': 'Negan',
    'owner': 'Baiju',
    'weight': 10,
    'Food': 'Meat',
}
pets.append(pet)

# Use a for loop to iterate through the 'pets' list and print information about each pet.
for pet in pets:
    print(f"\nThings I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
