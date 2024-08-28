
def add():
	print("add")

print("File name is mycode",__name__)
if __name__ == "__main__":
	add()
	from functionslist import add,sub
	a = input("Enter a msg:")
	print(a)

	b=200
	c =add(int(a),b)
	print("sum is ",c)
	c =sub(int(a),b)
	print("diff is ",c)
	c =add(int(a),b)
	print("sum is ",c)

