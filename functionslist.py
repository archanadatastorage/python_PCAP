print("I am in module")
print("in module" , __name__)
def add(x,y):
	return x+y

def sub(x,y):
	return x-y

if __name__== "__main__":
	print("module ")
else :
	print("module main is not called")