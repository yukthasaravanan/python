##1.
# ==============
# a='A'
# b='B'
# c='C'
# x = list()
# add a, b, c into x
# print the length of x
# selecting from lists
# # ====================
# a='A'
# b='B'
# c='C'
# x = list()
# x.append(a)
# x.append(b)
# x.append(c)
# print(x)
# print(len(x))

##2.
# ====================
# Given the list
# x = ['A', 'B', 'C']
# return the first item
# return the last item
# return the x reversed using indexing
# selecting first items
# ======================= 
# x = ['A', 'B', 'C']
# print(x[0])
# print(x[-1])
# print(x[::-1])


##3.
# ======================= 
# Given the following:
# x = [('A','x'), ('B','y'), ('C','z')]
# return ['A','B','C']
# =================
# x = [('A','x'), ('B','y'), ('C','z')]
# y=[]
# o=y.append(x[0][0])
# k=y.append(x[1][0])
# l=y.append(x[2][0])
# print(y)


##4.
# =======================
# Given the following:
# x = [1, 10, 20]
# return a list with 5 added to the numbers i.e. [6, 15, 25]
# # =======================
# x = [1, 10, 20]
# d=[4,5,67]
# print(x+d)


##5.
# ==================
# Given the following:
# x = [1, 10,  15, 3, 12, 15, 25, 50]
# return a list with only numbers divisible by 5 (% modulo operator)
# ===================
# x = [1, 10,  15, 3, 12, 15, 25, 50]
# c=[]
# for i in x:
#     if i%5==0:
#         c.append(i)
# print(c)
        

# ##6.
# ## ===================
# # given the lists:
# # x = ['A', 'B', 'C']
# # y = ['x', 'y', 'z']
# # create the following list:
# # [('A','x'), ('B','y'), ('C','z')]
# # ===========
# x = ['A', 'B', 'C']
# y = ['x', 'y', 'z']
# a=x[0],y[0]
# b=x[1],y[1]
# c=x[2],y[2]
# print("[",a,b,c,"]")

# def reverse_string(s):
#     result = ''
#     for char in s:
#         result = char + result
#     return result

# # Get input from user
# user_input = input("Enter a string: ")
# reversed_str = reverse_string(user_input)

# print("Reversed string:", reversed_str)
# num="12345"
# i=0
# max=num[0]
# while i<len(num):
#     if max<num:
#         max=num [i]
#     i+=1
# print("maximum value",max)    

