def binarysearch(arr,l,r,x):
	if r>=l:
		mid = l+(r-l)//2

		if x == arr[mid]:
			return mid
		elif x > arr[mid]:
			return binarysearch(arr,mid+1,r,x)
		else:
			return binarysearch(arr,l,mid-1,x)
	else:
		return -1


arr = [10,20,40,70,80,100,130]
x=80

result = binarysearch(arr,0,len(arr)-1,x)
print(result)