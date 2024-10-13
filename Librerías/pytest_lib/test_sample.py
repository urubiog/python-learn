# content of test_sample.py

import pytest 

def f(x):
    if not x: raise ValueError("Expected some value")

def test_f():
    with pytest.raises(ValueError):
        f(6)
