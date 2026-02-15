import pytest
from calculator import square

def test_postive():
    assert square(2) == 4
    assert square(3) == 9
def test_negtive():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_y():
    with pytest.raises(TypeError):
        square("cat")
