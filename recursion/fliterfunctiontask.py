# ##1Reverse all strings in a list using lambda
# s=[6,5,6,7,8]
# def num(inner):
#     return inner%2==0
# print (list(filter(num,s)))

# #2) words longer than 3 characters using filter()
# g=["yuktha","in","out"]
# print(list(filter (lambda f:len(f)>3,g)))

# ##3 remove empty string from a list using filter()
# g=["yuktha","in","out",""]
# print(list(filter (lambda f:len(f)!=0,g)))

# ##4positive numbers from list using filter()
# s=[6,5,6,-8,7,8]
# print(list(filter(lambda g : g>0,s)))

# ##5. keep names that start with 'A' using filter
# p=["yuktha","in","out","","Apple"]
# print(list(filter(lambda g : g.startswith("A"),p)))