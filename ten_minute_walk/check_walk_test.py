import pytest
import numpy as np
from ten_minute_walk import check_walk

def test_false_answer():
    assert check_walk(['n','n','n']) == False

def test_true_answer():
    assert check_walk(['w', 's', 'e', 'e', 'n', 'n', 'e', 's', 'w', 'w']) == True
