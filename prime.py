n = int(input("Enter the number: "))

for i in range(2, n-1):
	if (n % i == 0 ):
		print("Its not a prime number")
		break
	
else:
	print("It is a prime number")