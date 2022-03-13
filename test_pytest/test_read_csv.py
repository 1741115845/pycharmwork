import pytest
from test_pytest import oepn_readcsv
import requests
import json
@pytest.mark.parametrize('param',oepn_readcsv.read_csv())
def test_login(param):
    url=param[0]
    request=json.loads(param[1])
    print(request)
    response=json.loads(param[2])
    login=requests.post(url=url,json=request)
    print(json.loads(login.text))
    result=json.loads(login.text)
    assert result['code']==response['code']


if __name__=='__main__':
    pytest.main('-v','-s','./test_read_csv.py')