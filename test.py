#pl = input("请输入年份")
#
#year = int(pl)
#
#if year / 4 and year != 100:
#    print (year)

#coding=utf-8

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5


class TestClass:

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert x == "hi"
