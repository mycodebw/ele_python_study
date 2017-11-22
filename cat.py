import os
try:
    fh = open("testfile", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close()

class error(tryError):
    def __init__(self, arg):
        self.args = arg

try:
    raise error("Bad file")
except error,e:
    print (e.args)
