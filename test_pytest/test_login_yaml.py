import pytest
import yaml

from test_pytest import open_readyaml
import requests

@pytest.mark.parametrize('data',open_readyaml.read_yaml())
def test_yaml(data):
    # print(data['url'])
    # print(data['request'])
    login=requests.post(url=data['url'],json=data['request'])
    response=yaml.safe_load(login.text)
    assert response['code']==data['resport']['code']

if __name__=='__main__':
    pytest.main('-v','-s','./test_login_yaml.py')