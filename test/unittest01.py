import unittest
class Test(unittest.TestCase):
    def test_001(self):
        try:
            self.assertEqual("1","2")
        except Exception as e:
            print("错误提醒")
        print("测试001")
    def test_002(self):
        print("测试002")
if __name__=='__main__':
    suite=unittest.TextTestRunner().run(Test)



