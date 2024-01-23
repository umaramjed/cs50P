import seasons
import pytest

# Test cases for the convert_to_words function
def test_convert_to_words():
    assert seasons.convert_to_words(0) == "zero"
    assert seasons.convert_to_words(5) == "five"
    assert seasons.convert_to_words(15) == "fifteen"
    assert seasons.convert_to_words(21) == "twenty-one"
    assert seasons.convert_to_words(60) == "one hour"
    assert seasons.convert_to_words(61) == "one hour and one minute"
    assert seasons.convert_to_words(120) == "two hours"
    assert seasons.convert_to_words(123) == "two hours and three minutes"
    assert seasons.convert_to_words(999) == "sixteen hours and thirty-nine minutes"

# Test cases for the get_age_in_minutes function
def test_get_age_in_minutes():
    assert seasons.get_age_in_minutes("2000-01-01") == 0
    assert seasons.get_age_in_minutes("1990-12-31") == 525600
    assert seasons.get_age_in_minutes("1980-02-29") == 1680480
    assert seasons.get_age_in_minutes("2022-12-25") == 1585440

if __name__ == "__main__":
    test_convert_to_words()
    test_get_age_in_minutes()
    print("All tests passed!")
