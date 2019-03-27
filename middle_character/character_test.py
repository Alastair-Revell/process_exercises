import pytest
from character import middle_characters

def test_one():
    assert middle_characters('Abbc') == 'bb'

def test_two():
    assert middle_characters('Abbbc') == 'b'

def test_three():
    assert middle_characters("testing") == 't'
