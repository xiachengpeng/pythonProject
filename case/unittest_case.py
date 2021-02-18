import unittest


class FirstCase1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有case执行前的前置动作")

    @classmethod
    def tearDownClass(cls):
        print("所有case执行后的后置动作")

    def setUp(self):
        print("前置条件")

    def tearDown(self):
        print("后置条件")

    @unittest.skip("不执行第一条")  # 跳过执行
    def testfirst1(self):
        print("第一条case")

    def testfirst2(self):
        print("第二条case")

    def testfirst3(self):
        print("第三条case")


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(FirstCase1('testfirst2'))
    # suite.addTest(FirstCase1('testfirst3'))
    # unittest.TextTestRunner().run(suite)
