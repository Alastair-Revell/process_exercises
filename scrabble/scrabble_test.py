import pytest
from scrabble import *

def test_one():
    assert score('a') == 1

def test_two():
    assert score('f') == 4

def test_three():
    assert score('street') == 6

def test_four():
    assert score('OXYPHENBUTAZONE') == 41
