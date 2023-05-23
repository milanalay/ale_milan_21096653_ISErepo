# Function to find the season based on country and month
def find_season(country, month):
    seasons = {
        "australia": {
            "december": ["Summer", "Birak"],
            "january": ["Summer", "Birak"],
            "feburary": ["Summer", "Bunuru"],
            "march": ["Autumn", "Bunuru"],
            "april": ["Autumn", "Djeran"],
            "may": ["Autumn", "Djeran"],
            "june": ["Winter", "Makuru"],
            "july": ["Winter", "Makuru"],
            "august": ["Winter", "Dijiba"],
            "september": ["Spring", "Dijiba"],
            "october": ["Spring", "Kambarabg"],
            "november": ["Spring", "Kambarabg"]
        },
        "spain": {
            "december": "Winter",
            "january": "Winter",
            "feburary": "Winter",
            "march": "Spring",
            "april": "Spring",
            "may": "Spring",
            "june": "Summer",
            "july": "Summer",
            "august": "Summer",
            "september": "Autumn",
            "october": "Autumn",
            "november": "Autumn"
        },
        "japan": {
            "december": "Winter",
            "january": "Winter",
            "feburary": "Winter",
            "march": "Spring",
            "april": "Spring",
            "may": "Spring",
            "june": "Summer",
            "july": "Summer",
            "august": "Summer",
            "september": "Autumn",
            "october": "Autumn",
            "november": "Autumn"
        },
        "mauritius": {
            "november": "Summer",
            "december": "Summer",
            "january": "Summer",
            "feburary": "Summer",
            "march": "Summer",
            "april": "Summer",
            "may": "Autumn",
            "june": "Winter",
            "july": "Winter",
            "august": "Winter",
            "september": "Winter",
            "october": "Spring",
        },
        "malaysia": {
            "december": "Northeast Monsoon",
            "january": "Northeast Monsoon",
            "feburary": "Northeast Monsoon",
            "march": "Inter-monsoon",
            "april": "Inter-monsoon",
            "may": "Southeast Monsoon",
            "june": "Southeast Monsoon",
            "july": "Southeast Monsoon",
            "august": "Southeast Monsoon",
            "september": "Southeast Monsoon",
            "october": "Inter-monsoon",
            "november": "Inter-monsoon"
        },
        "sri lanka": {
            "december": "Northeast Monsoon",
            "january": "Northeast Monsoon",
            "feburary": "Northeast Monsoon",
            "march": "Inter-monsoon",
            "april": "Inter-monsoon",
            "may": "Southeast Monsoon",
            "june": "Southeast Monsoon",
            "july": "Southeast Monsoon",
            "august": "Southeast Monsoon",
            "september": "Southeast Monsoon",
            "october": "Inter-monsoon",
            "november": "Inter-monsoon"
        }

    }

    # Convert the country and month to lowercase to handle case-insensitivity
    country = country.lower()
    month = month.lower()
    
    # Check if the country and month are in the seasons dictionary
    if country in seasons and month in seasons[country]:
        season = seasons[country][month]
        if country == 'australia':
            print(f"The Meteorological season in '{country}' for the month of '{month}' is '{season[0]}' and the Noongar season is '{season[1]}'.")
        else:
            print(f"The season in '{country}' for the month of '{month}' is '{season}'.")
    else:
        print(f'Invalid input or data not available for the given country and month.')
