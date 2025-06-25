#  ##1. check odd or even using 
# a=int(input("num1"))
# b=int(input("num2"))
# def check(a1,b2):
#     c=a1*b2
#     print(c)
#     if c%2!=0:
#         print("odd num")
#     else:
#         print('even')
# check(a,b)

    
##2.compare 2 numbers and display the largest number.
# a=int(input("num1"))
# b=int(input("num2"))
# def check(a2,b2):
#     if a2>b2:
#         print("num1 is greater")
#     elif a2<b2:
#         print("num2 is greater")
#     else:
#         print("both are equal")
# check(a,b)

##3.determines the type of triangle based on the side length.0
# a=int(input("enter side a"))
# b=int(input("enter side b"))
# c=int(input("enter side c"))
# def tri(a,b,c):
#     if a==b==c:
#         print("its a equilateral triangle")
#     elif a==b or b==c or c==a :
#         print("its a isoceles triangle")
#     else:
#         print(" its  a  scalar triangle")
# tri(a,b,c)

# # ## 4.check three persons salary and display the maximum salary .
# sal1=int(input("salary 1"))
# sal2=int(input("salary 2"))
# sal3=int(input("salary 3"))
# def max(a,b,c):
#     if a<b or a<c:
#         print(" a is max")
#     elif b<a or b<a:
#         print("b is max")
#     else:
#         print("c is max")
# max(sal1,sal2 ,sal3)

# ##5.check the number is postive or negative:
# a=int(input("nnum1"))
# def check(i):
#     if i>0:
#         print("postive")
#     elif i<0:
#         print("negative")
#     else:
#         print("its a zero")
# check(a)

# #6.Check if a year is a leap year.
# p=int(input("entter the year"))
# def year(i):
#     if i%4==0:
#         print("leap year")
#     else:
#         print("non leap year")
# year(p)

# #7.Check if a character is a vowel or consonant
# l=input("enter any letter")
# def letter(p):
#     if p in ["a","e","i","o","u","A","E","I","O","U"]:
#         print( "vowel")
#     else:
#         print("consonant")
# letter(l)

# #8.  Check if a number is 2-digit
# k=int(input("num"))
# def digit(a):
#     if a>=10 and a<=99:
#         print("2-digit")
#     else:
#         print("1-digit or 3-digit")
# digit(k)


# #9.Check if number is divisible by either 2 or 7
# p=int(input("num"))
# def div(j):
#     if j%2==0 or j%7==0:
#         print("either 2 or 7")
#     else:
#         print("ntg")
# div(p)

# ##10.divisible by 3 and 5:
# h=int(input("num"))
# def dev(b):
#     if b%3==0 and b%5==0:
#         print("divisile by 3 and 5")
#     elif b%3==0:
#         print("divisible only by 3")
#     elif b%5==0:
#         print("divisible only by 5")
#     else:
#         print("ntg")
# dev(h)

# #11.print max from the list
# list=[23,56,78,89]
# def max(p):
#     max=list[0]
#     for i in list:
#         if i >max:
#             max=i
#     print(max)
# max(list)

#12reverse the list
# list=[89,78,67,44]
# def reverse(i):
#     print(list[::-1])
# reverse(list)

# ##13.comparing the two numbers and display the greatest number
# a=int(input("enter your number"))
# b=int(input("enter your number"))
# def myfunction(a,b):
#     if a>b:
#         print(" a is greater ",a)
#     else:
#         print(" b is greater",b)
# myfunction(a,b)
 
##14.average
# numbers = [4, 15, 8, 23, 9, 2, 12, 7]
# def avg():
#     average = sum(numbers) / len(numbers)
#     print(average) 
# avg()


# 15.to print the grade with the percentage

# a=int(input("enter your percentage"))
# def function():
#  if a>=90:
#     print("grade A")
#  elif a>=80:
#     print("grade B")

#  elif a>=70:
#      print("grade C")

#  else:
#      print("grade D")
# function()

# 16.print the index number of the following elements
# numbers = [4, 15, 8, 23, 9, 2, 12, 7]
# def my(o):
#     for i in o:
#         print(numbers.index(i))
# my(numbers)


# 17.print sum of the list
# numbers = [4, 15, 8, 23, 9, 2, 12, 7]
# def my(p):
#     sum=0
#     for i in p:
#         sum+=i
#         print(sum)
#     return sum
