from src.mathoperations import add,substract

def test_add():
    assert add(3,4) == 7
    assert add(-1,1)==0

def test_sub():
    assert substract(7,2) ==5
    assert substract(5,5)==0
    assert substract(2,3)==-1

