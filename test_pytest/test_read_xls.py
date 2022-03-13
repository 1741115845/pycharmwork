import pytest
from test_pytest import open_readxlsx
import requests
import json
@pytest.mark.parametrize('data',open_readxlsx.read_xlsx())
def test_login(data):
    # a=json.loads(data[1])
    # b=data[0]
    # c=json.loads(data[2])
    b=json.loads(data[2])['code']
    resporce=requests.post(url=data[0],
                  json=json.loads(data[1]))
    a=json.loads(resporce.text)['code']

    assert a==b

if __name__=='__main__':
    pytest.main('-v','-s','./test_login_xls.py')
