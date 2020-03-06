from string_calculator.calculator import add

import pytest


def test_empty_str():
    assert add("") == 0

def test_one_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,2") == 3

def test_many_numbers():
    assert add("1,2,3,4") == 10

def test_new_lines():
    assert add("1\n2,3") == 6

def test_diff_delimiters():
    assert add("//;\n1;2") == 3

def test_check_negatives():
    with pytest.raises(Exception) as err:
        assert add("//;\n-1;2,-3")
        assert str(err.value) == "Negatives not allowed: -1,-3,"

def test_more_than_twenty():
    assert add("//;\n1;2") == 3

def test_delimeter_len():
    assert add("//[***]\n1\n2\n3") == 6

def test_multiple_delimeters():
    assert add("//[*][%]\n1*2%3") == 6





