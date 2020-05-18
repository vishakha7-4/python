inp1 = int(input())
arr = []
arr2 = []

for input_int in range(inp1):
	inp = input()
	arr.append(inp)

print(arr)

for arr_in in arr:
	print(arr_in)
	if not len(arr_in) == 1:
		for char in arr_in:
			print(char)
			arr2.append(char)
			print(arr2)
		first_digit = int(arr2[0])
		second_digit = int(arr2[-1])
		print(first_digit)
		print(second_digit)


	else:
		print('sum',arr_in )
		




		# if not len(arr_in) == 1:
		# 	first_digit = int(arr[0])
		# 	second_digit = int(arr[-1])

		# 	sum = first_digit + second_digit
		# 	print("sum",sum)
		# else:
		# 	pass

	
