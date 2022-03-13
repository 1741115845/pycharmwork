import pytest


class Test_002():
    def test002(self):
      assert 1==1

def test_001_smoke():
    assert 1==1
def test_002_smoke():
    assert 1=='1'

def test_003():
    assert 1==1
def add(a,b):
    print(a+b)

@pytest.mark.exit
def test_exit_001():
    assert 1==1

@pytest.mark.exit
@pytest.mark.register
def test_exit_002():
    assert 1==1

@pytest.mark.login
def test_login_001():
    assert 1==1

@pytest.mark.register
def test_register_001():
    assert 1==1
