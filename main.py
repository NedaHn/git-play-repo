import sys


def func(n: int)->str:
    if n%2 == 0:
        return 'even'
    else:
        return 'odd'
    
def test_func():
    assert func(10) == 'even'
    assert func(5) == 'odd'
