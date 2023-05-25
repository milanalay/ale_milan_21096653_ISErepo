import find_season_module



def test_find_season():
    # enter the if part
    result = find_season_module.find_season("australia", "june")
    assert result == ["Winter", "Makuru"]

    # do not enter the if part
    result = find_season_module.find_season("france", "september")
    assert result == "Not found"


if __name__ == "__main__":
    test_find_season()
