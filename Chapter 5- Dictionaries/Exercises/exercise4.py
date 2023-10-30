rivers = {
    'Ganges': 'India',
    'Amazon River':'South America',
    'Thames':'England',
    'Volga':'Russia',
    'Congo':'Africa',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows in {country.title()}.")

print("\nThe following rivers in this list are:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries where the river flows are:")
for country in rivers.values():
    print(f"- {country.title()}")