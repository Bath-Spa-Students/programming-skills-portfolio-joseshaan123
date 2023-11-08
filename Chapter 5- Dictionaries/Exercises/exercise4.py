# Create a dictionary 'rivers' with river names as keys and the countries they flow through as values.
rivers = {
    'Ganges': 'India',
    'Amazon River': 'South America',
    'Thames': 'England',
    'Volga': 'Russia',
    'Congo': 'Africa',
}

# Use a for loop to iterate through the 'rivers' dictionary and print river names and the countries they flow through.
for river, country in rivers.items():
    print(f"The {river.title()} flows in {country.title()}.")

# Print a list of river names by iterating through the keys of the 'rivers' dictionary.
print("\nThe following rivers in this list are:")
for river in rivers.keys():
    print(f"- {river.title()}")

# Print a list of countries by iterating through the values of the 'rivers' dictionary.
print("\nThe following countries where the river flows are:")
for country in rivers.values():
    print(f"- {country.title()}")
