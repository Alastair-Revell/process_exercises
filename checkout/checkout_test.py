import pytest
import numpy as np
from checkout import checkout

def test_sum1():
    assert checkout('ABC') == 100

def test_sum2():
    assert checkout('AbC') == -1

def test_sum3():
    assert checkout('BCD') == 65

def test_sum4():
    assert checkout('DDA') == 80

def test_sum5():
    assert checkout('AAA') == 120

def test_sum6():
    assert checkout('BB') == 50

def test_sum6():
    assert checkout(18) == -1

def test_sum7():
    assert checkout('AAABB') == 170
