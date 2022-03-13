import unittest
from selenium import webdriver
from time import sleep

class BaiduLink(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com/?tn=49055317_26_hao_pg")
        sleep(2)
    def tearDown(self):
        self.driver.quit()
    def test_link_news(self):
        '''首页：点击百度新闻链接'''
        self.driver.find_element("link text",'新闻').click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(3)
        self.assertEqual(self.driver.current_url,'http://news.baidu.com/')

    def test_linke_map(self):
        '''首页：点击百度地图链接'''
        self.driver.find_element("link text",'地图').click()
        sleep(2)
        # 定位到最新的浏览器窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(3)
        self.assertIn('https://map.baidu.com',self.driver.current_url,'断言失败不存在包含内容')
# if __name__=='__main__':
#     unittest.main(verbosity=2)

