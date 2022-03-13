import pytest
import requests

def pytest_addoption(parser):
    parser.addoption('--foo',action="store",default='dyy',help="自定义参数")


@pytest.fixture()
def getFoo(request):
    return request.config.getoption('--foo')

# @pytest.fixture()
# def getIni(pytestconfig):
#     return  pytestconfig.getini('url')