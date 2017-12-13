class MyException(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message   

a=input("please input a num:")

if a < "20":
    try:
        raise MyException("my excepition is raised ")
    except MyException as e:
        print (e.message)
