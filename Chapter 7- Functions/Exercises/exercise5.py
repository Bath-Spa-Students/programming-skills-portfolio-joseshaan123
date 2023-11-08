#Defining a function
def describe_city(city, country='India'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

# Call the function for three different cities
describe_city('Kerala')
describe_city('Lahore', 'Pakistan')
describe_city('Tamil Nadu') #This will use new default country value
