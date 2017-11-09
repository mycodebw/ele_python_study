import unittest
#pl = input("请输入年份")
#
#year = int(pl)
#
#if year / 4 and year != 100:
#    print (year)

#coding=utf-8

#def func(x):
#    return x + 1
#
#def test_answer():
#    assert func(3) == 5
#
#
#class TestClass:
#
#    def test_one(self):
#        x = "this"
#        assert "h" in x
#
#    def test_two(self):
#        x = "hello"
#        assert x == "hi"
#
#class Dict(dict):
#
#    def __init__(self, **kw):
#        super(Dict, self).__init__(**kw)
#
#    def __getattr__(self, key):
#        try:
#            return self[key]
#        except KeyError:
#            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#    def __setattr__(self, key, value):
#            self[key] = value


class Test(unittest.TestCase):
    def setUp(self):
        self.num = input('Enter a number: ')

    def test_case1(self):
        print (self.number)
        self.assertEqual(self.number,10,msg='Your input is not 10')

    def test_case2(self):
        print (self.number)
        self.assertEqual(self.number,20,msg='Your input is not 20')

    @unittest.skip
    def test_case3(self):
        print (self.number)
        self.assertEqual(self.number,30,msg='Your input is not 30')

    if __name__ == '__main__':
        unittest.main()
