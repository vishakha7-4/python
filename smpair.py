t = int(input())

for T in range(t):
	n = int(input())
	# nums_list = list(map(int,input().split()))
	nums_list = list(map(int, input().split()))
	nums_list.sort()
	# print(nums_list)
	print(int(nums_list[0])+int(nums_list[1]))
