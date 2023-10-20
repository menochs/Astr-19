# defines a function f(x) that returns x**3 + 8 
def f(x):
	return x**3 + 8

# in the main function, call f(x) with x = 9 and print result 
def main():
	result = f(9)
	print(result)

	# Use if statement that executes if result is larger than 27 and prints "YAY!"
	if result>27:
		print("YAY!")
if __name__=="__main__":
	main()