import datetime

name = input("What is your name: ")
age = int(input("How old are you: "))
hundred_years = (datetime.datetime.now().year-age)+100
hundred_years_str = str(hundred_years)
statement = ('hi '+name+'you will turn 100 in the year '+ hundred_years_str +'\n')
print(statement)
number_of_copies_input = input("How many copies do you want: ")
number_of_copies_int = int(number_of_copies_input)
result = (statement * number_of_copies_int)
print(result)
