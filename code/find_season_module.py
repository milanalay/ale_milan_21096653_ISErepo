# Function to find the season based on country and month
def find_season(country, month):
    seasons = {
        "australia": {
            "december": ["Summer", "Birak"],
            "january": ["Summer", "Birak"],
            "february": ["Summer", "Bunuru"],
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
        # "australia": {
        #     "december": "Summer",
        #     "january": "Summer",
        #     "february": "Summer",
        #     "march": "Autumn",
        #     "april": "Autumn",
        #     "may": "Autumn",
        #     "june": "Winter",
        #     "july": "Winter",
        #     "august": "Winter",
        #     "september": "Spring",
        #     "october": "Spring",
        #     "november": "Spring"
        # },
        # "australia": {
        #     "december": "Birak",
        #     "january": "Birak",
        #     "february": "Bunuru",
        #     "march": "Bunuru",
        #     "april": "Djeran",
        #     "may": "Djeran",
        #     "june": "Makuru",
        #     "july": "Makuru",
        #     "august": "Dijiba",
        #     "september": "Dijiba",
        #     "october": "Kambarabg",
        #     "november": "Kambarabg"
        # },
        "spain": {
            "december": "Winter",
            "january": "Winter",
            "february": "Winter",
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
            "february": "Winter",
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
            "february": "Summer",
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
            "february": "Northeast Monsoon",
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
            "february": "Northeast Monsoon",
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
        return season
    else:
        invalid = f"Not found"
        return invalid