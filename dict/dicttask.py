# ###################################dictmethods############################3
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
# print()


# ##update()
# print(thisdict.update({"age":90}))

# ##del
# del thisdict


# ########################################dicttask#####################################
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

# height = int(input())0
# width = int(input())
# for _ in range(height):
#     print(width*"0")
a=int(input("num"))
b=int(input("num"))
def sum(a,b):
    c=a+b
    print(c)
sum(a,b)