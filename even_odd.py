# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# 1.  If the number is a multiple of 4, print out a different message.
# 2.  Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


num1 = input("Enter a number: ")
try:
    num1 = int(num1)
    mod_2 = num1%2
    if mod_2 == 0:
        mod_4 = num1%4
        if mod_4 == 0:
            print("The given number is a multiple of 4")
        else:
            print("The given number is even")

    if num % check == 0 :
        print("num divides check evenly")
    else :
        print("num DOES NOT divide check evenly")

    num = input("Enter the first number: ")
    check = input("Enter the second number: ")
    num = int(num)
    check = int(check)

except Exception as e:
    print(e)
    print("Enter a valid number")
else:
    print("The given number is odd")
