# ##################match_______________taskkkkk###################3
# 1##Odd_Even
# a=int(input())
# match a%2:
#     case 1:
#         print(a,"is odd")
#     case 0:
#         print(a,"is even")



# 2##Seasons
# a=input("Enter the Month: ")
# months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
# match a in ["January", "February","December"]:
#     case True:
#         print("Winter Season")
#     case False:
#         match a in ["March", "April", "May",]:
#             case True:
#                 print("Spring Season")
#             case False:
#                 match a in ["June","July", "August"]:
#                     case True:
#                         print("Summer Season")
#                     case False:
#                         match a in ["September", "October", "November"]:
#                             case True:
#                                 print("Autumn Season")
#                             case _:
#                                 print("Invalid Month Name")


# 3##comparing two digits:
# a=int(input("enter any number:"))
# b=int(input("enter any number:"))
# match a<b:
#     case True :
#         print("number b is greater than a")
#     case False:
#         print("number a is greater than b")


# 4##grade asper the percentage:
# a=int(input("enter ur percentage:"))//10
# match a :
#     case 1|2:
#         print("GRDE D")
#     case 3|4|5:
#         print("GRADE C")
#     case 6|7|8:
#               print("GRADE B")
#     case 9|10:
#               print("GRADE A ")
#     case _ :
#               print("invalid")

# ##number divisible by 3 and 5 and both 3 and 5:
# a=int(input("enter any number:"))
# match a%3==0 and a%5==0 :
#     case True:
#         print("the number is divisible both 5 and 3")
#     case False:
#         match a%3==0:
#             case True :
#                 print("it  is divisible only by 3")
#             case False:
#                 match a%5==0:
#                     case True:
#                         print("it is divisible only by 5")

# 5##types of triangle:
# a=int(input("enter side a"))
# b=int(input("enter side b"))
# c=int(input("enter side c"))
# match a==b==c:
#     case True :
#         print("its a equilateral triangle")
#     case False:
#         match a==b or b==c or c==a:
#             case True:
#                 print("its a isoceles triangle")
#             case _:
#                 print(" its  a  scalar triangle")
                

# 6## postive or negative
# a=int(input("enter the number :"))
# match a>0:
#     case True:
#         print("postive integer ")
#     case False:
#         match a>0:
#             case True :
#                 print("negative integer")
#             case False:
#                 print("maybe zero")

                

# ## 7day of the week :
# i=int(input("input any number between 1 to 7:"))
# match i==1:
#     case True :
#         print("SUNDAY")
#     case False:
#         match i==2:
#              case True :
#                  print("MONDAY")
#              case False:
#                  match i==3:
#                      case True :
#                          print("TUESDAY")
#                      case False:
#                          match i==4:
#                              case True:
#                                  print("WEDNESDAY ")
#                              case False:
#                                  match i==5:
#                                      case True:
#                                          print("THURSDAY")
#                                      case False:
#                                          match i==6:
#                                              case True :
#                                                  print("FRIDAY")
#                                              case False:
#                                                      match i==7:
#                                                          case True :
#                                                              print("saturday")
#                                                          case  False :
#                                                              print("invalid number")

# ##8check a number is two digit:
# i=int(input("enter the 2 digit number:"))
# match  i>=10 and i <=99:
#     case True:
#         print("its a two digit number")
#     case False:
#         match -10>=i and -99<=i:
#             case True:
#                 print("its a negative 2 digit number")
#             case _:
#                  print("more than two digits  so invalid")


# ##9check -2digit ,1digit or more:
# i=int(input("enter the 2 digit number:"))
# match  i>=10 and i <=99:
#     case True:
#         print("its a two digit number")
#     case False:
#         match -10>=i and -99<=i:
#             case True:
#                 print("its a negative 2 digit number")
#             case False:
#                  match i>10 and i>=1:
#                      case True :
#                          print("its a single digit postive number")
#                      case False:
#                          match -10<i and -1<=i:
#                              case True :
#                                  print("its a single digit  negative number")
#                              case False :
#                                  print("more than 2 digits")
                

#  ##equqlity of string:

# a=input("enter  any word ")
# b=input("enter any word ")
# match a==b:
#     case True :
#         print("both the strings are equal ")
#     case False:
#         print("both strings are not equal ")


# # #########################nested if condition###################################33
# ##################################nested if            
# username=input("enter your username")
# password=input("enter ur pass")
# if username=="" or password=="":
#     print(" field is required")
# if username=="yukthasri":
#     if password=="yukthasri08":
#         print("Login successful!")
#     else:
#         print("incorrect")

# else:
#     print("Incorrect username.")
        
    
# ######################################while_______________looppp###########################3           

# #### print all the numbers from 1 to 15:
# ##num = 1
# ##while num <= 15:
# ##    print(num,end=" ")
# ##    num += 1 

# ##print odd number from 6 to 29:
# ##num=6
# ##while num<=29:
# ##    if num%2==0:
# ##        print(num,end=" ")
# ##        num=num+1

# #### print even numbers from 20 to 40:
# ##num = 20
# ##while num <= 40:
# ##    print(num,end=" ")
# ##    num += 2
# ##
# ##
##print the numbers divisible by 3 and 5 ,only 5 , only 3  using while loop

# num = 1
# while num <= 100:
#    if num % 3 == 0 and num % 5 == 0:
#        print(num, end ="")
#    elif num % 5 == 0:
#        print(num, end="")
#    elif num % 3 == 0:
#        print(num,end="")
#    num += 1

# #### print all the elements in list:
# ##u=[1,2,3,4,5,6,7,8,9,10]
# ##print(u)

# ####leap year or not
# ##while True:
# ##    year = int(input("Enter a year : "))
# ##
# ##    if year % 4 == 0 :
# ##        print("its  a leap year", year)
# ##    else:
# ##        print("no a leap year",year)

# ####vowel or not:
# ##while True:
# ##    a=input("enter the word")
# ##
# ##    if a in ("a","e","i","o","u","A","E","I","O","U"):
# ##        print("its a vowel")
# ##    else :
# ##        print("not a vowel")
        
# ## check the numbers is in the given range
# ##while True :
# ##    a=int(input("enter the number:"))
# ##
# ##    if a>=0 and a<=50:
# ##        print(" it is in the given range")
# ##    else:
# ##        print ("not in the given range")


# #######################################string methods######################################
# ##rfind :
# a= "the promise of quality and authentcity"
# print(a.rfind("e"))

# ##rindex:
# a= "the promise of quality and authentcity"
# print(a.rindex("of"))

# ##rjust:
# a=" yuktha "
# print(a.rjust(50))

# ##rpartition
# y="i am yuktha"
# print(y.rpartition("am"))


# ##rsplit
# p=" hello world"
# print(p.rsplit("w"))

# ##rstrip:
# p="                                             hello world"
# print(p.strip ())

# ##split:
# p=" hello, world"
# print(p.split(","))
# ##difference between strip and rstrip:
# s = "!!hello!!"
# print(s.strip("!"))   # Output: "hello"
# print(s.rstrip("!"))  # Output: "!!hello"

# ##difference between split and rsplit:
# s = "one,two,three,four,five,six,seven"
# p=s.split(',', 2)
# print(p)
# # Output: ['one', 'two', 'three,four']

# s = "one,two,three,four,five,six"
# p=s.rsplit(',', 2)
# print(p)

# # Output: ['one,two', 'three', 'four']

# ##splitlines:
# d="hello \n world"
# print(d.splitlines())


# ##startswith:
# u="my self yuktha"
# h=u.startswith("am")
# print(h)

# ##strip:
# txt = "     banana     "
# x = txt.strip()
# print(x)

# txt = "     banana     "
# x = txt.strip()
# print("of all the fruits",x,"its my fav")

# ##swapcase:
# p="I Am YukTha"
# x=p.swapcase()
# print(x)

# ##title
# p="myself yuktha"
# print(p.title())

# ##zfill
# p="90"
# d=p.zfill(3)
# print(d)

# ##slicing :
# o="yuktha sri"
# print(o)
# print(o[0:3])
# print(o[7:10])
# print(o[0:6])

# ## python built in methods:
# p="   i am a super man     "
# print(p.upper())
# print(p.lower())
# print(p.strip())
# print(p.replace("man","women"))
# print(p.split("a"))



# ##String Concatenation
# a="i"
# b="am"
# c="yuktha"
# y="  "
# print(a+y+b+y+c)
# print(a+b+c)


# ##string format :
# age = 17
# txt = f"My name is yuktha, I am {age}"
# print(txt)
# print(f"total amount is ={50*80}")
# print(f"total amount is {age:.2f}")
# print("my name is \"yuktha\" ")
# print("my \"name\" is \"yuktha\"")

# ############listtttttttt############  
# myList = [10,20,30,40,20]
# print(len(myList))
# print(type(myList))
# studentData = ["ST001",945764956456,2,"demo name",True]

# department = list(("IT","CSE","ECE"))
# print(department[1])

# mobile = studentData[1]
# print(mobile)
# department[1] = "EEE"
# print(department)

# for i in department:
#     print(i)

# ## sum of the list
# list=[200,900,700,6700]
# total=0
# for i in list:
#     total +=i
# print(total)


# ##count postive and negative number
# num=[8,80,-5,-56,45]
# count_postive=0
# count_negative=0
# for i in num:
#     if i > 0:
#         count_postive+=1
#     elif i < 0:
#         count_negative+=1
# print("number of postive number is:",count_postive)
# print("number of negative number is:",count_negative)

# ## max val of the list
# o=[90,80,67,65,20]
# print(max(o))


# ## min val of the list
# o=[90,80,67,65,20]
# print(min(o))

# ## odd and even number in different list
# p=[2,3,4,5,6,7,8,9,22,67,56]
# odd_number=[]
# even_number=[]
# for i in p:
#     if i%2==0:
#         even_number.append(i)
#     elif i%2!=0:
#         odd_number.append(i)
# print(odd_number)
# print(even_number)

# ##reverse a list
# p=[90,78,56,45]
# print(p[::-1])

# ##number divisible 3:
# p=[45,789,3,99]
# for i in p:
#     if i%2!=0:
#         print(i,end="  ")

# ##how many time number appear:
# u=["90","0","0","0","7","6","7","5","4","4","5","6",]
# print(u.count("0"))

# ##replace all the negative  number with zero:
# numbers = [3, -1, 5, -7, 0, 8]
# numbers = [0 if x < 0 else x for x in numbers]
# print(numbers)


# a=["apple","box","car","devil","evil","friend","gram","hailstone","ink","joker","kart","love","market","ninja","orange","power","quil","rocket","star","track","umbrella","van","words","xylaphone","yonex","zebra"]
# for i in a:
#     print (i[0].upper(),i.upper(),len(i),sep="=")
    
# ##create a square of a numbers in a list
# u=[1,2,3,4,5,6,7,8,9,10]
# t=[]
# for i in u:
#     t .append (i**2)
# print(t)

# ##print only  duplicate elements 
# numbers = [1, 2, 3, 2, 4, 5, 3, 6, 5,6,1]
# dup = []

# for num in numbers:
#     if numbers.count(num) > 1 and num not in dup:
#         dup.append(num)

# print(dup)

# ## print second largest number from a list 
# numbers = [10, 20, 4, 45, 99]
# nums_copy = numbers.copy()
# nums_copy.remove(max(nums_copy))
# second = max(nums_copy)

# print("Second largest number is:", second)

# ##count how many numbers are less than ten
# p=[7,5,4,3,7,8,9,100,700,90,66,56,9,76]
# count=0
# for i in p:
#     if i>10:
#         count+=1
# print(count)

# ##print average of the list
# num = [10, 20, 30, 40, 50]
# ave = sum(num) / len(num)
# print("Average is:", ave)

# ##print  the prime number in a list
# numbers = [3, 4, 7, 9, 11, 13, 16, 17, 20]
# primes = []

# for num in numbers:
#     if num > 1:
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)

# print("Prime numbers in the list:", primes)


# ##multiply all the elements in list:
# p=[6,8,9,0,3,34,56]
# for i in p:
#     print(i*i)

# ##create a list from 1 to 10
# ##num = list(range(1, 11))
# ##print(num)

# ##create a all number divisile by 5 and 7
# t=[5,6,7,8,28,25,35]
# g=[]
# for i in t:
#     if i % 5==0 and i % 7==0 :
#         g.append(i)
# print(g)

# ## cont the element equal to their index
# numbers = [0, 2, 2, 3, 5, 5, 6]
# count = 0
# for i in range(len(numbers)):
#     if numbers[i] == i:
#         count += 1
# print("index count:", count)

# ##add 10 to all the odd numbes
# p=[2,3,5,7]
# for i in p:
#     if i%2!=0:
#         print(i+10)

# ##replace all the even number by -1:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers[i] = -1
# print(numbers)

# ##check if a number exist in a list:
# numbers = [10, 20, 30, 40, 50]
# check = 30
# if check in numbers:
#     print("Number exists in the list.")
# else:
#     print("Number does not exist in the list.")

# ##print common element in two list:
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# common = []

# for item in list1:
#     if item in list2 and item not in common:
#         common.append(item)

# print("Common elements:", common)



# # ## max value form the give list
# list=[23,56,78]
# max=list[0]
# for p in list:
#     if p> max:
#         max=p
# print(max)




# ##remove all the negative numbers list
# o=[4,-9,9,-8,-7,-6]
# d=[]
# for i in o:
#     if i>0:
#         d.append(i)
# print(d)

# ##sum only even numbers:
# p=[8,3,4,56,22,33,42]
# k=0
# for i in p:
#     if i>0:
#         k+=i
# print(k)


# ##remove all the element less than 10:
# u=[2,3,4,5,6,7,8,10,101,199]
# o=[]
# for i in u:
#     if i>=10:
#         o.append(i)
# print(o)


# ##print all the alpha character from the mixtered list:
# ##u=["yuktha",56,78,"true","happy",67]
# ##if type(u)=="string":
# ##  if u.isalpha(u):
# ##print(u)

# ##u=[1000,5000,700,560]
# ##total = 0
# ##for i in u:
# ##    total =total +i
# ##    print(i)

# ##############tupleeeeeeeeeeee############
# ###tuple
# u=("yuktha","apple","orange")
# print(u)
# print(type(u))
# print(u[1])

# p=list(u)
# p[-1]="banana"
# print(tuple(p))
# print(len(u))

# ##packing and unpacking:
# o=("one","two","three")
# a,b,c=o
# print(a)
# print(b)
# print(c)

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(type(a))          # <class 'tuple'>
# p = list(a)             # Convert tuple to list
# print(p)                # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1## sum of the tuple
# list=(200,900,700,6700)
# total=0
# for i in list:
#     total +=i
# print(total)

# 2##reverse a tuple
# p=(90,78,56,45)
# print(p[::-1])

# 3##number divisible 3:
# p=(45,789,3,99,42)
# for i in p:
#     if i%2!=0:
#         print(i)

# 4##how many time number appear:
# u=("90","0","0","0","7","6","7","5","4","4","5","6",)
# print(u.count("0"))

# 5##create a square of a numbers in a tuple:
# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# o=[]
# f=list(a) 
# for i in a:
#     o.append(i**2)
# print(tuple(o))

# 6##remove all the negative numbers
# o=(4,-9,9,-8,-7,-6)
# d=[]
# p=list(o)
# for i in p:
#     if i>0:
#         d.append(i)
# print(tuple(d))

# 7##print average of the list
# num = (10, 20, 30, 40, 50)
# ave = sum(num) / len(num)
# print("Average is:", ave)


# 8##print only  duplicate elements 
# numbers = (1, 2, 3, 2, 4, 5, 3, 6, 5,6,1)
# dup = []
# o=list(numbers)
# for num in o:
#     if o.count(num) > 1 and num not in dup:
#         dup.append(num)

# print(tuple(dup))

###################################settttttttttttttttttt################################################
# ##add 6 to a set
# e={"2","3","4","5"}
# e.add("6")
# print(e)

# ##remove 3 from a set
# i={"9","6","5"}
# i.remove("9")
# print(i)

# ##create a list with string
# r="yuktha"
# o=set(r)
# print(o)

# ##check 4 in the given set
# o={6,5,4,3,4}
# print(9 in o)

# ##union of two sets
# y={"one","two"}
# z={"three","four","five"}
# p=y.union(z)
# print(p)

# ##vowels
# o={"a","l","o","y"}
# for i in o:
#     if i in ["a","e","i","o","u","A","E","I","O","U"]:
#         print(i)


# ##intersection of two sets
# y={"one","two"}
# z={"three","four","five"}
# c=y.intersection(z)
# print(c)


# ##difference between to sets
# y={"one","two"}
# z={"three","four","five"}
# x=y.difference(z)
# print(x)

# ##duplicate value from a list
# u=[8,0,7,6,5,4,6,4]
# p=set(u)
# print(p)


# ##length of the set
# p={6,4,5,6,7,8,9,3,4,67}
# print(len(p))

# ##square of the set
# p={6,4,5,6,7,8,9,3,4,67}
# for i in p:
#     print(i**2 )


# ##sum of the list:
# list = [[34, 56, 23], [23, 78, 56]]
# sum_list = []

# for sub in list:
#     total = 0
#     for num in sub:
#         total += num
#     sum_list.append(total)

# print(sum_list)

# ##splite all the datatpe in a different list
# p=["name","age",90,"open",78.2,"yuktha",True]
# string=[]
# integer=[]
# fl=[]
# boo=[]
# for i in p:

#     if type(i)== str:
#         string.append(i)
        
#     if type (i)== int:
#         integer.append(i)
#     if type (i)== float :
#         fl.append(i)
#     elif  type(i)== bool:
#         boo.append(i)
# print(string)
# print(integer)
# print(fl)
# print(boo)

# ## sum the list in side the dict :
# data = [
#     {"name": "aaa", "score": [98,82, 100 ,78,67]},
#     {"name": "bbbb", "score": [55, 6,0, 54]},
#     {"name": "cccc", "score": [34, 7,8, 89]},
# ]
# total_score =
# print(total_score)

# ##count the datatype present inside the list:

# p=["name","age",90,"open",78.2,"yuktha",True]
# string=[]
# integer=[]
# fl=[]
# boo=[]
# count_str=0
# count_int=0
# count_fl=0
# count_bo=0        
# for i in p:

#     if type(i)== str:
#         string.append(i)
#         count_str+=1
#     if type (i)== int:
#         integer.append(i)
#         count_int+=1
#     if type (i)== float :
#         fl.append(i)
#         count_fl+=1
#     elif  type(i)== bool:
#         boo.append(i)
#         count_bo=0
# print(string)
# print(integer)
# print(fl)
# print(boo)
# print(count_str)
# print(count_int)
# print(count_bo)
# print(count_fl)
##########################patttern##########################################
# ##square
# for i in range(9):
#     for j in range (9):
#         print("*",end=" ")
#     print()

# ##right triangle
# for i in range(9):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# ##inverse right triangle
# for i in range(9,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# ##pyramid
# for i in range(6):
#     for j in range(6-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()



# ##halow prymid:
# def hollow_pyramid(rows):
#     for i in range(rows):
#         for j in range(rows - i - 1):
#             print(" ", end="")
#         for k in range(2 * i + 1):
#             if k == 0 or k == 2 * i or i == rows - 1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()
# hollow_pyramid(5)


# ##inverse pyramid
# rows = 3 
# for i in range(rows):
#     line = ' ' * i + '* ' * (rows - i)
#     print(line)


# ##hallow square:
# size = 5
# for i in range(size):
#     for j in range(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()



# ##hallow right triangle
# rows = 5  
# for i in range(1, rows + 1):
#     row = []
#     for j in range(1, i + 1):
#         if j == 1 or j == i or i == rows:
#             row.append("*")
#         else:
#             row.append(" ")
#     print(' '.join(row))

# def print_diamond(n):
#     # Upper half
#     for i in range(n):
#         print(' ' * (n - i - 1) + '*' * (2 * i + 1))
#     # Lower half
#     for i in range(n - 2, -1, -1):
#         print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# # Example usage
# print_diamond(5)




# my_tuple = (1, 2, 3)  
# a, b, c = my_tuple  
# print(a, b, c)  

#  # print all the numbers from 1 to 15:
# num = 1
# while num <= 15:
#    print(num)
#    num += 1 

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["year"])


# ##replacing a value
# thisdict["brand"]="BMW"
# print(thisdict)


# ##items(),values(),keys()
# print(thisdict.items())
# print(thisdict.values())
# print(thisdict.keys())


# ##pop(),popitems(),clear()
# print(thisdict.pop("model"))
# print(thisdict.popitem())
# print(thisdict.clear())


# ##update()
# print(thisdict.update({"age":90}))

# ##del
# del thisdict



# # dict methods:
# # 1) Create an empty dictionary.
# u={}

# # 2) Create a dictionary with three key-value pairs.
# u={"name":"yuktha","age":16,"class":12,"year":2008}
# print(u)

# # 3)Change the value of an existing key.
# u["name"]="bbb"
# print(u)

# #4)  Access the value of a key.
# print(u["name"])

# #5) Add a new key-value pair.
# u["add_no"]=90
# print(u)


# # 6) Delete a key-value pair.
# print(u.pop("add_no"))
# print(u)

# #7) Check if a key exists in the dictionary.
# print("name" in u)


# #8) Get all the keys from the dictionary.
# print(u.keys())


# #9) Get all the values from the dictionary.
# print(u.values())

# #10) Get all the key-value pairs as tuples.
# print(u.items())


# # #11) Merge two dictionaries.
# a={"one":1,"two":2}
# b={"three":3,"four":4}
# d=a.update(b)
# print(a)


# # 12)  Use get() to access a key with a default value.
# print(u.get("age"))


# ##13) Loop through a dictionary.
# for i in u:
#     print(u[i],end=" ")

# ##14)  Remove all items from a dictionary.
# print(u.clear())
# print(u)


# ##15) Create a nested dictionary.
# f={"one":1,"two":2,"three": 3,"four":{"four":4}}
# print(f)
# print(f["four"])


# ##16) Find the key with the maximum value
# fromo = {'a': 5, 'b': 9, 'c': 2}
# max_key = max(fromo, key=fromo.get)
# print("Key with maximum value:", max_key)


# ##17) Remove a key using pop()
# print(fromo.pop("a"))
# print(fromo)


# ##18) Check if all dictionary values are even.
# o = {'a': 5, 'b': 9, 'c': 2}
# r=o.values()
# print(r)
# for i in r:
#     if i%2==0:
#         print("its a even number")
#     else:
#         print("its a odd number")


# ##19) Sum all values in a dictionary.
# o = {'a': 5, 'b': 9, 'c': 2}
# r=o.values()
# print(sum(r))


# ##20) Filter dictionary to keep items with values above a 50.
# o = {'a': 51, 'b': 93, 'c': 2}
# r=o.values()
# for i in r:
#     if i>=50:
#         print(i)

#  ##print odd number from 6 to 29:
# num = 6
# while num <= 29:
#     if num % 2 != 0:
#         print(num)
#     num += 1



# num = 7
# while num <= 29:
#     print(num)

# #split all the datatype in a different list
# p=["name","DOB","hello",90.0,"false",78.2]
# string=[]
# integer=[]
# fl=[]
# boo=[]
# for i in p:

