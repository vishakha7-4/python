# Array Rotation


def arrayrot(arr,d,n):
	print(arr)

	for i in range(d):
		print(i)
		arrayrotleft(arr,n)

def arrayrotleft(arr,n):
	temp = arr[0]

	for i in range(n-1):
		print(i)
		arr[i] = arr[i+1]
		print(arr)

	arr[n-1] = temp
	print(arr)


array = [1,2,3,4,5,6,7]

arrayrot(array,2,7)