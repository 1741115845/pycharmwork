import pytest
import requests

def test_baidu():
    r=requests.get(url="https://www.baidu.com/",timeout=0.01)
    print("time:",r.elapsed.total_seconds())

def test_baidu02():
    r = requests.get(url="https://www.baidu.com/", timeout=0.3)
    print("time:", r.elapsed.total_seconds())

if __name__ == '__main__':
    # 先执行失败的用例
    # pytest.main('-v','-s','./test_cash.py','--tb=no','--failed-first')
    #
    pytest.mian(['./test_cash.py','--tb=no','--last-failed'])