# Function to print graphics output based on season
def find_season_graphics(country, month):
    # Define the file paths for each season image
    season_images = {
        "australia": {
            "december": ["../documents/ISEimages/summer.png", "../documents/ISEimages/birak.png"],
            "january": ["../documents/ISEimages/summer.png", "../documents/ISEimages/birak.png"],
            "february": ["../documents/ISEimages/summer.png", "../documents/ISEimages/bunuru.png"],
            "march": ["../documents/ISEimages/autumn.png", "../documents/ISEimages/bunuru.png"],
            "april": ["../documents/ISEimages/autumn.png", "../documents/ISEimages/djeran.png"],
            "may": ["../documents/ISEimages/autumn.png", "../documents/ISEimages/djeran.png"],
            "june": ["../documents/ISEimages/winter.png", "../documents/ISEimages/makuru.png"],
            "july": ["../documents/ISEimages/winter.png", "../documents/ISEimages/makuru.png"],
            "august": ["../documents/ISEimages/winter.png", "../documents/ISEimages/djilba.png"],
            "september": ["../documents/ISEimages/spring.png", "../documents/ISEimages/djilba.png"],
            "october": ["../documents/ISEimages/spring.png", "../documents/ISEimages/kambarang.png"],
            "november": ["../documents/ISEimages/spring.png", "../documents/ISEimages/kambarang.png"]
        }
        "spain": {
            "december": "../documents/ISEimages/winter.png",
            "january": "../documents/ISEimages/winter.png",
            "feburary": "../documents/ISEimages/winter.png",
            "march": "../documents/ISEimages/spring.png",
            "april": "../documents/ISEimages/spring.png",
            "may": "../documents/ISEimages/spring.png",
            "june": "../documents/ISEimages/summer.png",
            "july": "../documents/ISEimages/summer.png",
            "august": "../documents/ISEimages/summer.png",
            "september": "../documents/ISEimages/autumn.png",
            "october": "../documents/ISEimages/autumn.png",
            "november": "../documents/ISEimages/autumn.png"
        },
        "japan": {
            "december": "../documents/ISEimages/winter.png",
            "january": "../documents/ISEimages/winter.png",
            "feburary": "../documents/ISEimages/winter.png",
            "march": "../documents/ISEimages/spring.png",
            "april": "../documents/ISEimages/spring.png",
            "may": "../documents/ISEimages/spring.png",
            "june": "../documents/ISEimages/summer.png",
            "july": "../documents/ISEimages/summer.png",
            "august": "../documents/ISEimages/summer.png",
            "september": "../documents/ISEimages/autumn.png",
            "october": "../documents/ISEimages/autumn.png",
            "november": "../documents/ISEimages/autumn.png"
        },
        "mauritius": {
            "november": "../documents/ISEimages/summer.png",
            "december": "../documents/ISEimages/summer.png",
            "january": "../documents/ISEimages/summer.png",
            "feburary": "../documents/ISEimages/summer.png",
            "march": "../documents/ISEimages/summer.png",
            "april": "../documents/ISEimages/summer.png",
            "may": "../documents/ISEimages/autumn.png",
            "june": "../documents/ISEimages/winter.png",
            "july": "../documents/ISEimages/winter.png",
            "august": "../documents/ISEimages/winter.png",
            "september": "../documents/ISEimages/winter.png",
            "october": "../documents/ISEimages/spring.png",
        },
        "malaysia": {
            "december": "../documents/ISEimages/monsoon.png",
            "january": "../documents/ISEimages/monsoon.png",
            "feburary": "../documents/ISEimages/monsoon.png",
            "march": "../documents/ISEimages/inter-monsoon.png",
            "april": "../documents/ISEimages/inter-monsoon.png",
            "may": "../documents/ISEimages/monsoon.png",
            "june": "../documents/ISEimages/monsoon.png",
            "july": "../documents/ISEimages/monsoon.png",
            "august": "../documents/ISEimages/monsoon.png",
            "september": "../documents/ISEimages/monsoon.png",
            "october": "../documents/ISEimages/inter-monsoon.png",
            "november": "../documents/ISEimages/inter-monsoon.png"
        },
        "sri lanka": {
            "december": "../documents/ISEimages/monsoon.png",
            "january": "../documents/ISEimages/monsoon.png",
            "feburary": "../documents/ISEimages/monsoon.png",
            "march": "../documents/ISEimages/inter-monsoon.png",
            "april": "../documents/ISEimages/inter-monsoon.png",
            "may": "../documents/ISEimages/monsoon.png",
            "june": "../documents/ISEimages/monsoon.png",
            "july": "../documents/ISEimages/monsoon.png",
            "august": "../documents/ISEimages/monsoon.png",
            "september": "../documents/ISEimages/monsoon.png",
            "october": "../documents/ISEimages/inter-monsoon.png",
            "november": "../documents/ISEimages/inter-monsoon.png"
        }
    }


    # Convert the country and month to lowercase to handle case-insensitivity
    country = country.lower()
    month = month.lower()

    # Check if the country and month have a corresponding season image
    if country in season_images and month in season_images[country]:
        image_path = season_images[country][month]
        return image_path
    else:
        return 'Invalid Input'
