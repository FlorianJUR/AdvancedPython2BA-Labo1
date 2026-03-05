# windows= pytest = python -m pytest 

import utils

def test_fact():
    assert utils.fact(3) == 6

def test_roots():
    assert utils.roots(0,1,0) == 0

def test_integrate():
    assert utils.integrate(x/2,0,1) == 1
