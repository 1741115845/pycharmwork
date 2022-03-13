import pytest
def add(a,b):
    sum=a+b
    return sum
# 列表
@pytest.mark.parametrize('a,b,sum',[[1,1,2],[2,2,4]])
def test_add001(a,b,sum):
    assert add(a,b)==sum
# 元组
@pytest.mark.parametrize('a,b,sum',[(3,1,4),(4,2,6)])
def test_add002(a,b,sum):
    assert add(a,b)==sum
#字典{'a':1,'b':2,'sum':3},{'a':2,'b':3,'sum':5}
@pytest.mark.parametrize('data',[pytest.param({'a':1,'b':2,'sum':3},id='test'),pytest.param({'a':2,'b':3,'sum':5},id='test')])
def test_add003(data):
    assert add(data.get('a'),data['b'])==data['sum']
