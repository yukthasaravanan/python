# ############listtttttttt############  
myList = [10,20,30,40,20]
print(len(myList))
print(type(myList))
studentData = ["ST001",945764956456,2,"demo name",True]

department = list(("IT","CSE","ECE"))
print(department[1])

mobile = studentData[1]
print(mobile)
department[1] = "EEE"
print(department)

for i in department:
    print(i)

## sum of the list
list=[200,900,700,6700]
total=0
for i in list:
    total +=i
print(total)


##count postive and negative number
num=[8,80,-5,-56,45]
count_postive=0
count_negative=0
for i in num:
    if i > 0:
        count_postive+=1
    elif i < 0:
        count_negative+=1
print("number of postive number is:",count_postive)
print("number of negative number is:",count_negative)

## max val of the list
o=[90,80,67,65,20]
print(max(o))


## min val of the list
o=[90,80,67,65,20]
print(min(o))

## odd and even number in different list
p=[2,3,4,5,6,7,8,9,22,67,56]
odd_number=[]
even_number=[]
for i in p:
    if i%2==0:
        even_number.append(i)
    elif i%2!=0:
        odd_number.append(i)
print(odd_number)
print(even_number)

##reverse a list
p=[90,78,56,45]
print(p[::-1])

##number divisible 3:
p=[45,789,3,99]
for i in p:
    if i%2!=0:
        print(i,end="  ")

##how many time number appear:
u=["90","0","0","0","7","6","7","5","4","4","5","6",]
print(u.count("0"))

##replace all the negative  number with zero:
numbers = [3, -1, 5, -7, 0, 8]
numbers = [0 if x < 0 else x for x in numbers]
print(numbers)


a=["apple","box","car","devil","evil","friend","gram","hailstone","ink","joker","kart","love","market","ninja","orange","power","quil","rocket","star","track","umbrella","van","words","xylaphone","yonex","zebra"]
for i in a:
    print (i[0].upper(),i.upper(),len(i),sep="=")
    
##create a square of a numbers in a list
u=[1,2,3,4,5,6,7,8,9,10]
t=[]
for i in u:
    t .append (i**2)
print(t)

##print only  duplicate elements 
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 5,6,1]
dup = []

for num in numbers:
    if numbers.count(num) > 1 and num not in dup:
        dup.append(num)

print(dup)

## print second largest number from a list 
numbers = [10, 20, 4, 45, 99]
nums_copy = numbers.copy()
nums_copy.remove(max(nums_copy))
second = max(nums_copy)

print("Second largest number is:", second)

##count how many numbers are less than ten
p=[7,5,4,3,7,8,9,100,700,90,66,56,9,76]
count=0
for i in p:
    if i>10:
        count+=1
print(count)

##print average of the list
num = [10, 20, 30, 40, 50]
ave = sum(num) / len(num)
print("Average is:", ave)

##print  the prime number in a list
numbers = [3, 4, 7, 9, 11, 13, 16, 17, 20]
primes = []

for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

print("Prime numbers in the list:", primes)


##multiply all the elements in list:
p=[6,8,9,0,3,34,56]
for i in p:
    print(i*i)

##create a list from 1 to 10
num = list(range(1, 11))
print(num)

##create a all number divisile by 5 and 7
t=[5,6,7,8,28,25,35]
g=[]
for i in t:
    if i % 5==0 and i % 7==0 :
        g.append(i)
print(g)

## cont the element equal to their index
numbers = [0, 2, 2, 3, 5, 5, 6]
count = 0
for i in range(len(numbers)):
    if numbers[i] == i:
        count += 1
print("index count:", count)

##add 10 to all the odd numbes
p=[2,3,5,7]
for i in p:
    if i%2!=0:
        print(i+10)

##replace all the even number by -1:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = -1
print(numbers)

##check if a number exist in a list:
numbers = [10, 20, 30, 40, 50]
check = 30
if check in numbers:
    print("Number exists in the list.")
else:
    print("Number does not exist in the list.")

##print common element in two list:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)



# ## max value form the give list
list=[23,56,78]
max=list[0]
for p in list:
    if p> max:
        max=p
print(max)




##remove all the negative numbers list
o=[4,-9,9,-8,-7,-6]
d=[]
for i in o:
    if i>0:
        d.append(i)
print(d)

##sum only even numbers:
p=[8,3,4,56,22,33,42]
k=0
for i in p:
    if i>0:
        k+=i
print(k)


##remove all the element less than 10:
u=[2,3,4,5,6,7,8,10,101,199]
o=[]
for i in u:
    if i>=10:
        o.append(i)
print(o)


##print all the alpha character from the mixtered list:
u=["yuktha",56,78,"true","happy",67]
if type(u)=="string":
 if u.isalpha(u):
     print(u)

u=[1000,5000,700,560]
total = 0
for i in u:
   total =total +i
   print(i)

##sum of the list:
list = [[34, 56, 23], [23, 78, 56]]
sum_list = []

for sub in list:
    total = 0
    for num in sub:
        total += num
    sum_list.append(total)

print(sum_list)

##splite all the datatpe in a different list
p=["name","age",90,"open",78.2,"yuktha",True]
string=[]
integer=[]
fl=[]
boo=[]
for i in p:

    if type(i)== str:
        string.append(i)
        
    if type (i)== int:
        integer.append(i)
    if type (i)== float :
        fl.append(i)
    elif  type(i)== bool:
        boo.append(i)
print(string)
print(integer)
print(fl)
print(boo)




##sum the score ,print the name nd output in list of dict
data= [
    {"name": "AA", "score": [78, 98, 76]},
    {"name": "BB", "score": [67, 56, 45]},
    {"name": "CC", "score": [45, 68, 94]},
]
k=[]
for student in data:
    name = student["name"]
    scores = student["score"]
    average = sum(scores) / len(scores)
    status=""
    if average >90:
        status="excellent"
    elif average >80:
        status="verygood"
    elif average >70:
        status=" good"
    elif average >60:
        status="average"
    else:
        status="poor"      
    average = sum(scores) / len(scores)
    k.append({"name":name,"average":average,"status":status}) 
print(k)