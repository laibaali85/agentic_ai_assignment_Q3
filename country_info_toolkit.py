def get_capital(country):
    capitals = {
        "pakistan": "Islamabad",
        "india": "New Delhi",
        "china": "Beijing",
        "usa": "Washington, D.C.",
        "japan": "Tokyo"
    }
    return capitals.get(country.lower(), "Capital not found.")

def get_languages(country):
    languages={
         "pakistan": "Urdu",
        "india": "Hindi",
        "china": "Mandarin",
        "usa": "English",
        "japan": "Japanese"
    }
    return languages.get(country.lower(),"language not found.")

def get_population(country):
    populations ={
        "pakistan": "240 million",
        "india": "1.4 billion",
        "china": "1.4 billion",
        "usa": "331 million",
        "japan": "125 million"
    }
    return populations.get(country.lower(),"population not found")

def country_info(country):
    capital = get_capital(country)
    language = get_languages(country)
    population = get_population(country)

    info = (
        f"Country: {country.title()}\n"
        f"Capital: {capital}\n"
        f"Official Language: {language}\n"
        f"Population: {population}"
    )
    return info



if __name__ == "__main__":
    country_name = input("Enter a country name: ")
    print("\nFetching information...\n")
    print(country_info(country_name))