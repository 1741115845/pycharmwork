import pytest
import requests
from selenium import webdriver

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    print("001")
    return driver

@pytest.fixture()
def init(driver):
    driver.get("https://www.baidu.com/")
    print("002")
    yield
    driver.quit()

def test_title(driver,init):
    print("003")
    assert driver.title=='百度一下，你就知道'


@pytest.fixture()
def login():
    print("这个是请求登录接口，接口返回token")

@pytest.fixture()
def inster(login):
    print("这个新增接口，拿登录接口的token作为请求头，故这个需要调用login")

def test_delete(inster,login):
    print("删除接口，先调用新增接口，新增接口在调用login拿到token，删除再通过新增接口拿到删除id")

@pytest.fixture()
def init():
    print("相当于unittest的setUP函数，作为初始化执行")
    yield
    print("相当于unittest的tearDown函数，作为结束执行")

@pytest.fixture(scope='session')
def fix_session():
    print("测试")

class TestClass_1:
    @pytest.mark.usefixtures('fix_class') #执行顺序 num2
    @pytest.mark.usefixtures('fix_session') #执行顺序 num1
    @pytest.mark.usefixtures('fix_func_decorator_3')#执行顺序 num4
    @pytest.mark.usefixtures('fix_func_decorator_2') #执行顺序 num3
    def test_fun(self,fix_func_param1,fix_func_param2):#执行顺序 num5,num6
        print("测试")


