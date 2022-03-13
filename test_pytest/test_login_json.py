import json

import pytest
from test_pytest import open_readjson
import requests

@pytest.mark.parametrize('data',open_readjson.read_json())
def test_login(data):
    login=requests.post(url=data['url'],json=data['request'])
    resurt=json.loads(login.text)
    assert resurt['code']==data['resport']['code']

if __name__=='__main__':
    pytest.main('-v','-s','test_login_json.py')