min = 0
max = 0
list_s1 = []
list_s2 = []

for T in range(int(input())):
	s1 = input()
	s2 = input()
	s1 = [c_s1 for c_s1 in s1]
	s2 = [c_s2 for c_s2 in s2]

	z = range(len(s1))
	for num in z:

		if s1[num] == "?" and s2[num] == "?":
			min += 0
			max += 1
		elif s1[num] == s2[num]:
			min += 0
			max += 0
		elif s1[num] == "?" or s2[num] == "?":
			min += 0
			max += 1
		else:
			min += 1
			max += 1
	print(min , " ", max)
	min = 0
	max = 0
