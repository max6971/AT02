import pytest

from main import count_vowels
def test_all_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    assert count_vowels("bcdfg") == 0

def test_mixed_string():
    assert count_vowels("Hello World") == 3
    assert count_vowels("Python Programming") == 4

def test_empty_string():
    assert count_vowels("") == 0

def test_uppercase_vowels():
    assert count_vowels("AEIOU") == 5

def test_lowercase_vowels():
    assert count_vowels("aeiou") == 5