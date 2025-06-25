#  ##1. check odd or even using 
# a=int(input("num1"))
# b=int(input("num2"))
# def check(a1,b2):
#     c=a1*b2
#     if c%2!=0:
#         return ("odd num")
#     else:
#         return ('even')
# print(check(a,b))

    
# ##2.compare 2 numbers and display the largest number.
# a=int(input("num1"))
# b=int(input("num2"))
# def check(a2,b2):
#     if a2>b2:
#         return ("num1 is greater")
#     elif a2<b2:
#         return ("num2 is greater")
#     else:
#         return("both are equal")
# print(check(a,b))

# #3.determines the type of triangle based on the side length.0
# a=int(input("enter side a"))
# b=int(input("enter side b"))
# c=int(input("enter side c"))
# def tri(a,b,c):
#     if a==b==c:
#         return("its a equilateral triangle")
#     elif a==b or b==c or c==a :
#         return("its a isoceles triangle")
#     else:
        
#         return(" its  a  scalar triangle")
# print(tri(a,b,c))

# # ## 4.check three persons salary and display the maximum salary .
# sal1=int(input("salary 1"))
# sal2=int(input("salary 2"))
# sal3=int(input("salary 3"))
# def max(a,b,c):
#     if a<b or a<c:
#         return(" a is max")
#     elif b<a or b<a:
#         return("b is max")
#     else:
#         return("c is max")
# print(max(sal1,sal2 ,sal3))

# ##5.check the number is postive or negative:
# a=int(input("nnum1"))
# def check(i):
#     if i>0:
#         return("postive")
#     elif i<0:
#         return("negative")
#     else:
#         return("its a zero")
# print(check(a))

# #6.Check if a year is a leap year.
# p=int(input("entter the year"))
# def year(i):
#     if i%4==0:
#         return("leap year")
#     else:
#         return("non leap year")
# print(year(p))

# #7.Check if a character is a vowel or consonant
# l=input("enter any letter")
# def letter(p):
#     if p in ["a","e","i","o","u","A","E","I","O","U"]:
#         print( "vowel")
#     else:
#         return("consonant")
# print(letter(l))

# #8.  Check if a number is 2-digit
# k=int(input("num"))
# def digit(a):
#     if a>=10 and a<=99:
#         return("2-digit")
#     else:
#         return("1-digit or 3-digit")
# print(digit(k))


# #9.Check if number is divisible by either 2 or 7
# p=int(input("num"))
# def div(j):
#     if j%2==0 or j%7==0:
#         return("either 2 or 7")
#     else:
#         return("ntg")
# print(div(p))

# ##10.divisible by 3 and 5:
# h=int(input("num"))
# def dev(b):
#     if b%3==0 and b%5==0:
#         return("divisile by 3 and 5")
#     elif b%3==0:
#         return("divisible only by 3")
#     elif b%5==0:
#         return("divisible only by 5")
#     else:
#         return("ntg")
# print(dev(h))

# #11.print max from the list
# list=[23,56,78,89]
# def max(p):
#     max=list[0]
#     for i in list:
#         if i >max:
#             max=i
#     return(max)
# print(max(list))

# 12 reverse the list
# list=[89,78,67,44]
# def reverse(i):
#     return(list[::-1])
# print(reverse(list))

# ##13.comparing the two numbers and display the greatest number
# a=int(input("enter your number"))
# b=int(input("enter your number"))
# def myfunction(a,b):
#     if a>b:
#         return(" a is greater ",a)
#     else:
#         return(" b is greater",b)
# print(myfunction(a,b))
 
# #14.average
# numbers = [4, 15, 8, 23, 9, 2, 12, 7]
# def avg():
#     average = sum(numbers) / len(numbers)
#     return(average) 
# print(avg())


# 15.to print the grade with the percentage

# a=int(input("enter your percentage"))
# def function():
#  if a>=90:
#     return("grade A")
#  elif a>=80:
#     return("grade B")

#  elif a>=70:
#      return("grade C")

#  else:
#      return("grade D")
# print(function())

# 16.print the index number of the following elements
# numbers = [4, 15, 8, 23, 9, 2, 12, 7]
# def my(o):
#     for i in o:
#         return(numbers.index(i))
# print(my(numbers))




