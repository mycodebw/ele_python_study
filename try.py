#a=10
#b=0
#try:
#    print (a/b)
#except:
#    print ("error")
#finally:
#    print ("always excute")


try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print ("关闭文件")
        fh.close()

except IOError:
    print ("Error: 没有找到文件或读取文件失败")
