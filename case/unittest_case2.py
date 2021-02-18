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
    def testfirst001(self):
        print("第001条case")

    def testfirst002(self):
        print("第002条case")

    def testfirst003(self):
        print("第003条case")


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(FirstCase1('testfirst002'))
    # suite.addTest(FirstCase1('testfirst003'))
    # unittest.TextTestRunner().run(suite)
