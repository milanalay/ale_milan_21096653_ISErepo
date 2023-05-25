import find_season_module

# Submodule: find_season_module
# Input: country, month (string)
# Output: season (string)
# If country and month exist in the available data dictionary, 
#   then return 'season' otherwise return 'Not found'.


def test_find_season():
    # Test case for valid Equivalence class, country or month with available data.
    assert ["Summer", "Birak"] == find_season_module.find_season('australia', 'december')

    assert 'Winter' == find_season_module.find_season('spain', 'january')

    assert 'Spring' == find_season_module.find_season('japan', 'march')

    assert 'Autumn' == find_season_module.find_season('mauritius', 'may')

    assert 'Northeast Monsoon' == find_season_module.find_season('malaysia', 'february')

    assert 'Inter-monsoon' == find_season_module.find_season('sri lanka', 'november')

    # Test case for Invalid Equivalence class
    # country or month not available in the data
    assert 'Not found' == find_season_module.find_season('denmark', 'june')

    # Empty country or month
    assert 'Not found' == find_season_module.find_season('', 'july')
    assert 'Not found' == find_season_module.find_season('japan', '')

    # Invalid Input type
    assert 'Not found' == find_season_module.find_season('123', 'august')
    assert 'Not found' == find_season_module.find_season('australia', '9')



if __name__ == '__main__':
    test_find_season()
