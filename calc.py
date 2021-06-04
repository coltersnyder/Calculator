def add(x,y):#TODO
	print("Add")
	pass
def subtract(x,y):#TODO
	print("sub")
	pass
def multiply(x,y):#TODO
	print("mult")
	pass
def divide(x,y):#TODO
	print("div")
	pass
print("Welcome to the calculator")
while(True):
	x = int(input("Enter Number 1: "))
	y = int(input("Enter Number 2: "))
	op = input("What Operation do you want?\n(+,-,*,/): ")
	r = 0;
	if(op == '+'):
		r = add(x,y)
	elif(op == '-'):
		r = subtract(x,y)
	elif(op == '*'):
		r = multiply(x,y)
	elif(op == '/'):
		r = divide(x,y)
	else:
		print(f"ERROR: UNKNOWN OPERATION {op}")
		break
	print(f"Result: {r}")
	choice = input("Do you wish to continue: ").lower()
	if(choice == "n" or choice == "no"):
		print("Thank you!")
		break
