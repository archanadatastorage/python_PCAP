from mypackage.sub_package.math_op import add
import mypackage.module as md
import logging

logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s-%(levelno)s-%(message)s-%(name)s')
logging.debug("hello")
print(add(2,13))
print(md.hello())

import sys
print(sys.path)