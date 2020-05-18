def fib(n):
	a=0;
	b=1
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fib(n-1)+fib(n-2)


print(fib(8))

