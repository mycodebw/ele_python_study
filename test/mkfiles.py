import os
import sys
import threadpool
import time

path = '/Users/elesh/test/'
dirname = 'test'
filename = 'a'
crfile = []

def create_mk_files(numbers):
    try:
        """循环创建目录"""
        for num in range(numbers):
            os.mkdir(path + dirname +str(num))
    except OSError:
        """异常捕获"""
        print ("目录已经存在")
    else:
        """用startwith判断test开头的文件写入test_write"""
        for dirs in os.listdir(path):
            if dirs.startswith('test'):
                op = (path + dirs + '/' + filename)
                opfile = open(op, "w")
                opfile.write('test_write')
                opfile.close()
    finally:
        print ("关闭文件")


def read_files():
    try:
        """循环读取然后strip去空格"""
        for dirs in os.listdir(path):
            if dirs.startswith('test'):
                rdfiles = (path + dirs + '/' + filename)
                open_rdfiles = open(rdfiles,'r')
                for line in open_rdfiles.readlines():
                    line = line.strip() 
                    print (line)
    except OSError:
        """异常捕获文件不存在打印"""
        print ("不存在读取失败")
    finally:
        print ("Close")

def files_num(numbers):
    for num in range (numbers):
        crfile.append(filename + str(num))   

def create_files(crefile):
    for num in crefile:
#        print (num)
        ofile = open(num, "w")
        ofile.close()


                    

if __name__ == '__main__':
    files_num(5)
    create_mk_files(5)
    #start_time = time.time()
    #pool = threadpool.ThreadPool(2) 
    #requests = threadpool.makeRequests(create_files, crfile)
    #[pool.putRequest(req) for req in requests]
    #pool.wait() 
    #print ('%d second'% (time.time()-start_time))
    create_files(crfile)
    read_files()
