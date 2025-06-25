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