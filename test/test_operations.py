from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(4,5)==9
    assert add(-2,3)==1
    
def test_sub():
    assert sub(-6,4)==-10
    assert sub(-1,-1)==0
    
    
