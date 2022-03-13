import unittest
from selenium import webdriver
from time import sleep
class BaiduSo(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
    def tearDown(self):
        self.driver.quit()
    def test_enable(self):
        '''百度搜索：搜索框可编辑'''
        enable=self.driver.find_element('id','kw')
        self.assertTrue(enable.is_enabled())
    def test_so(self):
        '''百度搜索：可支持搜索'''
        so=self.driver.find_element('id','kw')
        so.send_keys('webdriver')
        sleep(2)
        self.driver.find_element('id','su')
        self.assertTrue(so.get_attribute('value'),'webdriver')

# if __name__=='__main__':
#     unittest.main(verbosity=2)