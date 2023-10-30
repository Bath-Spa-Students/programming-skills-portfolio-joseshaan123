def describe_city(city, country='India'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Kerala')
describe_city('Lahore', 'Pakistan')
describe_city('Tamil Nadu')