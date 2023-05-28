import check_temperature_module

# average_temperatures = {
#         "perth": {
#             "morning": 18.2,
#             "evening": 16.5
#         },
#         "adelaide": {
#             "morning": 23,
#             "evening": 21
#         }  
#     }


# Submodule: check_temperature_module
# Input: city(string), time(string), temperature(float)
# Output: result(string)

# If the temperature is greater than average temperature and the difference is more than 5, 
# then return message ('The temperature in {city} {time} is {temperature}°C' which is {difference}°C above the average temperature.)
# else return 'Above'. If less than average temperature, return 'Below', otherwise return 'Not found'.



def test_check_temperature():
    # Test case for difference more than 5.
    message = 'The temperature in perth morning is 25°C, which is 6.8°C above the average temperature.'
    assert message == check_temperature_module.check_temperature('perth', 'morning', 25)

    # Test case for 'Above'
    assert 'Above' == check_temperature_module.check_temperature('adelaide', 'evening', 25)

    # Test case for 'Below'
    assert 'Below' == check_temperature_module.check_temperature('perth', 'evening', 15)

    # Test case for Invalid Data
    # follows name of a country wish to visit, last name as appear in the ID, last four digits of student ID
    assert 'Not found' == check_temperature_module.check_temperature('norway', 'ale', 6653)
    assert 'Not found' == check_temperature_module.check_temperature('perth', 'afternoon', 25)
    assert 'Not found' == check_temperature_module.check_temperature('adelaide', 'morning', '')






if __name__ == '__main__':
    test_check_temperature()