import find_season_module
import find_season_graphics_module
import check_temperature_module

if __name__ == "__main__":
    choice = input("Please enter 'season' to find the season or enter 'temperature' to find the temperature of some countries in the database: ")
    # converting the input to handle case-insensitivity
    choice = choice.lower()
    if choice == 'season':
        country = input("Enter the country name: ")
        month = input("Enter the month: ")
        find_season_module.find_season(country, month)
        find_season_graphics_module.find_season_graphics(country, month)
    elif choice == 'temperature':
        city = input("Enter the city (Perth or Adelaide): ")
        time = input("Enter the time (Morning or Evening): ")
        temperature = float(input("Enter the temperature: "))
        check_temperature_module.check_temperature(city, time, temperature)
    else:
        print('Invalid Input') 


