(n,k) = map(int, input().split(' '))
count = 0
for no in range(n):
	a = int(input())
	if a%k == 0:
		count = count+1

print(count)
