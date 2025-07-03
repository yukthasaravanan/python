##1.Square all numbers in a list using map function
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)

# ##2.Convert all strings to uppercase.
# words = ['apple', 'banana', 'cherry']
# uppercased = list(map(str.upper, words))
# print(uppercased)

##3.Convert list of string numbers to integers ['1', '2', '3', '4'].
# num=['1', '2', '3', '4']
# change=str(num)
# print(change)
# print(type(change))

# ##4.Add two lists element-wise using lambda.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = list(map(lambda x, y: x + y, list1, list2))
# print(result)



# ##5.Get the length of each string:
# words = ['apple', 'banana', 'cherry']
# lengths = list(map(len, words))
# print(lengths)

# ##6. Check if elements are even using lambda.
# f=[4,2,3,45,5]
# print(list(map(lambda a : "even" if a % 2==0 else "odd",f)))

# ##7.Capitalize the first letter of each word using lambda.
# u=["yuktha","hello","world"]
# print (list(map(lambda h: h.capitalize(),u)))


##8.Reverse all strings in a list using lambda
u=["yuktha"]
print (list(map(lambda h:h[::-1],u)))
