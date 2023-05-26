import pytest
import sys
sys.path.append("..")
from exercice2 import StringAnalyzer

def test_count_vowels():
    analyzer = StringAnalyzer("Hello, World!")
    assert analyzer.count_vowels() == 3

    analyzer = StringAnalyzer("aeiou")
    assert analyzer.count_vowels() == 5

    analyzer = StringAnalyzer("bcdfg")
    assert analyzer.count_vowels() == 0

def test_count_consonants():
    analyzer = StringAnalyzer("Hello, World!")
    assert analyzer.count_consonants() == 7

    analyzer = StringAnalyzer("aeiou")
    assert analyzer.count_consonants() == 0

    analyzer = StringAnalyzer("bcdfg")
    assert analyzer.count_consonants() == 5

def test_count_digits():
    analyzer = StringAnalyzer("Hello123")
    assert analyzer.count_digits() == 3

    analyzer = StringAnalyzer("NoDigits")
    assert analyzer.count_digits() == 0

    analyzer = StringAnalyzer("1234567890")
    assert analyzer.count_digits() == 10

def test_count_words():
    analyzer = StringAnalyzer("Hello, World!")
    assert analyzer.count_words() == 2

    analyzer = StringAnalyzer("This is a sentence.")
    assert analyzer.count_words() == 4

    analyzer = StringAnalyzer("SingleWord")
    assert analyzer.count_words() == 1

def test_count_lines():
    analyzer = StringAnalyzer("Line 1\nLine 2\nLine 3")
    assert analyzer.count_lines() == 3

    analyzer = StringAnalyzer("Single Line")
    assert analyzer.count_lines() == 1

if __name__ == "__main__":
    pytest.main()































































































































































































































































































































































































































































































































































































































