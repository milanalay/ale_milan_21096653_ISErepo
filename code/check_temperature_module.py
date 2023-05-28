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
    if city in average_temperatures and time in average_temperatures[city] and temperature:
        average_temp = average_temperatures[city][time]
        difference = round(float(temperature) - average_temp, 2)
        if float(temperature) > average_temp:
            if difference > 5:
                message = f"The temperature in {city} {time} is {temperature}°C, which is {difference}°C above the average temperature."
                return message
            else:
                result1 = f"Above"
                return result1
        else:
            result2 = f"Below"
            return result2
    else:
        result = f"Not found"
        return result
        
