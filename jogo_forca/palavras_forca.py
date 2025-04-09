import random

def get_country() -> str:
    famous_countries = [
    "United States",
    "China",
    "Japan",
    "Germany",
    "United Kingdom",
    "France",
    "Italy",
    "Canada",
    "Brazil",
    "India",
    "Russia",
    "Australia",
    "South Korea",
    "Spain",
    "Mexico",
    "Netherlands",
    "Switzerland",
    "Sweden",
    "Austria",
    "Belgium",
    "Norway",
    "Denmark",
    "Finland",
    "Ireland",
    "Portugal",
    "Greece",
    "Turkey",
    "Egypt",
    "South Africa",
    "Nigeria",
    "Argentina",
    "Thailand",
    "Indonesia",
    "Vietnam",
    "Philippines",
    "Saudi Arabia",
    "United Arab Emirates",
    "Singapore",
    "Israel",
    "Morocco",
    "Kenya",
    "New Zealand",
    "Poland",
    "Hungary"]

    pos = random.randint(0, len(famous_countries) - 1)
    return famous_countries[pos]

print(get_country())
print(get_country())

