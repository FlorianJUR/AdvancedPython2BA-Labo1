# windows= pytest = python -m pytest 

import pytest
import utils

def test_fact():
    assert utils.fact(3) == 6

def test_roots():
    assert utils.roots(0,1,0) == 0

def test_integrate():
    assert utils.integrate('x/2',0,1) == 0.25
    assert utils.integrate('x**3+2*x-9',0,1) == pytest.approx(-7.75)
