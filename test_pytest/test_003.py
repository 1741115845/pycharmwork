import pytest
import requests
# def test_001():
#     assert 1==2
# def test_002():
#     assert 1==1
def test_baidu():
    r=requests.get(url='https://www.baidu.com')
    assert r.status_code==200
def test_taobao():
    r=requests.get(url='https://www.taobao.com')
    assert r.status_code==200
def test_jd():
    r=requests.get(url='https://www.jd.com')
    assert r.status_code==200
