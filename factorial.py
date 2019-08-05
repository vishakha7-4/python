# factorial 

num_inputs = int(input("Number of inputs: "))


for inputs in range(num_inputs):
	n = int(input())
	fact_data = range(1,n+1)
	num = 1
	for fact_num in fact_data:
		num = num * fact_num
	
	print(num)
		
				
