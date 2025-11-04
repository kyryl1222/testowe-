import pytest
from aplikacja import dodawanie,odejmowanie,mnozenie

def test_dodawanie():
    assert dodawanie(2, 3) == 5

def test_odejmowanie():
    assert odejmowanie(5, 2) == 3

def test_mnozenie():
    assert mnozenie(3,5) == 15
