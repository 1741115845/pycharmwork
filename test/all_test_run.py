import unittest
import os
import HTMLTestRunner
import time

def all_test():
    suite=unittest.TestLoader().discover(start_dir=os.path.dirname(__file__),pattern='test*.py',top_level_dir=None)
    return suite
def run():
    name=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+'自动化测试报告.html'
    fp=os.path.join(os.path.dirname(__file__),'resporthtml',name)
    HTMLTestRunner.HTMLTestRunner(stream=open(fp,'wb'),title='自动化测试报告',description='自动化测试详情描述').run(all_test())
if __name__=='__main__':
    run()
