import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
for1 = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')


#first handler - file handler
file_handler = logging.FileHandler("emp.log")
file_handler.setFormatter(for1)

#second handler - stream handler
st_handler = logging.StreamHandler()
st_handler.setFormatter(for1)


# add the handler
logger.addHandler(file_handler)
logger.addHandler(st_handler)

def add(x,y):
	return x+y

def subtract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	try :
		result = x/y
	except ZeroDivisionError :
		logger.exception("try with diff denominator")
	else:
		return result


result = add(2,3)
logger.info("Sum is : {}".format(result))

div_result = divide(10,5)
print("div result is : {}".format(div_result))

div_result1 = divide(10,0)
print("div result2 is : {}".format(div_result1))