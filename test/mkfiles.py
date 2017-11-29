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

        for num in range(numbers):
            os.mkdir(path + dirname +str(num))
    except OSError:
        print ("目录已经存在")
    else:
        for dirs in os.listdir(path):
            if dirs.startswith('test'):
                op = (path + dirs + '/' + filename)
                opfile = open(op, "w")
                opfile.write('test_write')
                opfile.close()
    finally:
        print ("关闭文件")


def read_files():
    for dirs in os.listdir(path):
        if dirs.startswith('test'):
            rdfiles = (path + dirs + '/' + filename)
            open_rdfiles = open(rdfiles,'r')
            for line in open_rdfiles.readlines():
                line = line.strip() 
                print (line)

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
