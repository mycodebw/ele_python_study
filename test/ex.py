class MyException(Exception):
    """自定义异常类,继承Base Exception下的Exception"""
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message   

a=input("please input a num:")

if a < "20":
    """如果小于20捕获异常,否则什么都不返回,类只定义没信息所以什么都没有"""
    try:
        raise MyException("my excepition is raised ")
    except MyException as e:
        print (e.message)
