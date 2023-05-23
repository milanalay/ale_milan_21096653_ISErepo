# Function to check temperature status
def check_temperature(city, time, temperature):
    # Dictionary containing average temperatures for cities
    average_temperatures = {
        "perth": {
            "morning": 18.2,
            "evening": 16.5
        },
        "adelaide": {
            "morning": 23,
            "evening": 21
        }
    }

    # Convert the city and time to lowercase to handle case-insensitivity
    city = city.lower()
    time = time.lower()

    # Check if the city and time are in the average_temperatures dictionary
    if city in average_temperatures and time in average_temperatures[city]:
        average_temp = average_temperatures[city][time]
        difference = temperature - average_temp
        if difference > 5:
            return f"The temperature in {city} {time} is {temperature}°C, which is {difference}°C above the average."
        elif difference < -5:
            return f"The temperature in {city} {time} is {temperature}°C, which is {abs(difference)}°C below the average."
        else:
            return f"The temperature in {city} {time} is {temperature}°C, which is around the average."
    else:
        return "Invalid input or data not available for the given city and time."
