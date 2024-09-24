import logging
logging.basicConfig(filename='mylogs.log',level=logging.DEBUG,format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        logging.debug('created emp {} {}'.format(self.first,self.last))
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)


emp1 = Employee('sia','kumari')