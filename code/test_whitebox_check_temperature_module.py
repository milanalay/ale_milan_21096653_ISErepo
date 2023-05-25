import check_temperature_module



def test_check_temperature():
    # enter the third If part
    result = check_temperature_module.check_temperature("perth", "morning", 25)
    assert result == f"The temperature in perth morning is 25°C, which is 6.8°C above the average temperature."

    # enter the first else part
    result = check_temperature_module.check_temperature("perth", "morning", 20)
    assert result == "Above"

    # enter the second else part
    result = check_temperature_module.check_temperature("adelaide", "evening", 19)
    assert result == "Below"

    # enter the outer else part
    result = check_temperature_module.check_temperature("sydney", "afternoon", '')
    assert result == "Not found"



if __name__ == "__main__":
    test_check_temperature()