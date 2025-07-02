# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%B"))#full month name 
# print(x.strftime("%a"))#day in short
# print(x.strftime("%A"))#full day name
# print(x.strftime("%b"))#month in short
# print(x.strftime("%w"))#week day in num
# print(x.strftime("%d"))#date in num
# print(x.strftime("%m"))#month in num
# print(x.strftime("%y"))#Year, full version
# print(x.strftime("%H"))#Hour 00-23
# print(x.strftime("%I"))#Hour 00-12
# print(x.strftime("%M"))#Minute 00-59

# ##to calculate age
# import datetime
# year = int(input("Enter your birth year: "))
# presentyear = datetime.datetime.now().year
# age = presentyear - year
# print("Your age is:", age)

# # # calculate how day a person lived 
# import datetime
# year = int(input("Enter your birth year: "))
# month = int(input("Enter your birth month: "))
# day = int(input("Enter your birth day: "))
# birth = datetime.date(year, month, day)
# today = datetime.date.today()
# days = (today - birth).days
# print("You have lived for", days)

