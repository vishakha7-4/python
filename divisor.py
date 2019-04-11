# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = input("Please choose a number to divide: ")
num = int(num)

listRange = list(range(1,num+1))
list_divisors = []

for a in listRange:
    if num%a == 0 :
        list_divisors.append(a)
    else:
        pass

print(list_divisors)
