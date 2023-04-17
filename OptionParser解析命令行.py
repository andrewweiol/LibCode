#Python之OptionParser模块使用详解 
#https://www.jb51.net/article/236808.htm

#!/usr/bin/env python3.8.8
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2022/02/08 11:48:40
@Author  :   热气球 
@Version :   1.0
@Contact :   17695691664@163.com
'''

from optparse import OptionParser
def main():
    parser = OptionParser(usage="usage: %prog [options] arg",version="%prog 1.0",description="hello OptionParser!")
    parser.add_option("-f", "--file", dest="filename",help="read data from FILENAME")
    parser.add_option("-v", "--verbose",action="store", default='reqiqiu',dest="verbosename",help="这是帮助文档")
    parser.add_option("-q", "--quiet",action="store_false", dest="verbose")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    if options.verbose:
        print("reading %s..." % options.filename)

if __name__ == "__main__":
    main()
#===test.py -h输出===#
PS C:\Users\Administrator> & E:/python3.8.8/python.exe c:/Users/Administrator/Desktop/test.py -h     
Usage: test.py [options] arg
hello OptionParser!
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -f FILENAME, --file=FILENAME
                        read data from FILENAME
  -v VERBOSENAME, --verbose=VERBOSENAME
                        这是帮助文档
  -q, --quiet

#===test.py -v输出===#
PS C:\Users\Administrator> & E:/python3.8.8/python.exe c:/Users/Administrator/Desktop/test.py --version
test.py 1.0


