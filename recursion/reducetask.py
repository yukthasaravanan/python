##sum of all numbers
from functools import reduce
numbers = [1, 2, 3, 4, 5]

total_sum=reduce(lambda x, y: x + y, numbers)

print("Sum of all numbers:", total_sum)

##product of all numbers
from functools import reduce
numbers = [1, 2, 3, 4, 5]

product=reduce(lambda x, y: x * y, numbers)

print("product of all numbers:", product)

##to find the maximum
from functools import reduce
numbers = [4, 9, 2, 15, 6, 10]

maximum = reduce(lambda x, y: x if x > y else y, numbers)

print("Maximum number:", maximum)

##to concatenate the string 
from functools import reduce
words=["hello"," world "]
conc=reduce(lambda x,y: x+y,words)
print(conc)


##to find a number from the digits
from functools import reduce
numbers =[1,2,3,4,5,6,7,8,9]
sum=reduce(lambda x,y : x*10+y,numbers)
print(sum)