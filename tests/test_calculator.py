import re
import pytest
from string_calculator.calculator import add


def test_empty_string():
    assert add('') == 0

def test_single_digit():
    assert add('1') == 1
    assert add('2') == 2
    assert add('9') == 9

def test_two_digits():
    assert add('2,2') == 4
    assert add('1,5') == 6

def test_multiple_digits():
    assert add('5,8,9') == 22
    assert add('20,5,100') == 125

def test_ignore_numbers_over_1001():
    assert add('2,1005,2') == 4
    assert add('10000') == 0

def test_line_delimeter():
    assert add('2\n3,5') == 10
    assert add('5,3\n4\n6') == 18

def test_multiple_delimeters():
    assert add('//[*][%]\n11*20%2') == 33