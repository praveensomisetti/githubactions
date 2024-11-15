from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(4,5)==9
    assert add(-2,3)==1
    assert add(45,40)==85
    assert add(0,-90)==-90
    assert add(20,30)==50
    
def test_sub():
    assert sub(-6,4)==-10
    assert sub(-1,-1)==0
    
