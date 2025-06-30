##################match_______________taskkkkk###################3
1##Odd_Even
a=int(input())
match a%2:
    case 1:
        print(a,"is odd")
    case 0:
        print(a,"is even")



2##Seasons
a=input("Enter the Month: ")
months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
match a in ["January", "February","December"]:
    case True:
        print("Winter Season")
    case False:
        match a in ["March", "April", "May",]:
            case True:
                print("Spring Season")
            case False:
                match a in ["June","July", "August"]:
                    case True:
                        print("Summer Season")
                    case False:
                        match a in ["September", "October", "November"]:
                            case True:
                                print("Autumn Season")
                            case _:
                                print("Invalid Month Name")


3##comparing two digits:
a=int(input("enter any number:"))
b=int(input("enter any number:"))
match a<b:
    case True :
        print("number b is greater than a")
    case False:
        print("number a is greater than b")


4##grade asper the percentage:
a=int(input("enter ur percentage:"))//10
match a :
    case 1|2:
        print("GRDE D")
    case 3|4|5:
        print("GRADE C")
    case 6|7|8:
              print("GRADE B")
    case 9|10:
              print("GRADE A ")
    case _ :
              print("invalid")

##number divisible by 3 and 5 and both 3 and 5:
a=int(input("enter any number:"))
match a%3==0 and a%5==0 :
    case True:
        print("the number is divisible both 5 and 3")
    case False:
        match a%3==0:
            case True :
                print("it  is divisible only by 3")
            case False:
                match a%5==0:
                    case True:
                        print("it is divisible only by 5")

5##types of triangle:
a=int(input("enter side a"))
b=int(input("enter side b"))
c=int(input("enter side c"))
match a==b==c:
    case True :
        print("its a equilateral triangle")
    case False:
        match a==b or b==c or c==a:
            case True:
                print("its a isoceles triangle")
            case _:
                print(" its  a  scalar triangle")
                

6## postive or negative
a=int(input("enter the number :"))
match a>0:
    case True:
        print("postive integer ")
    case False:
        match a>0:
            case True :
                print("negative integer")
            case False:
                print("maybe zero")

                

## 7day of the week :
i=int(input("input any number between 1 to 7:"))
match i==1:
    case True :
        print("SUNDAY")
    case False:
        match i==2:
             case True :
                 print("MONDAY")
             case False:
                 match i==3:
                     case True :
                         print("TUESDAY")
                     case False:
                         match i==4:
                             case True:
                                 print("WEDNESDAY ")
                             case False:
                                 match i==5:
                                     case True:
                                         print("THURSDAY")
                                     case False:
                                         match i==6:
                                             case True :
                                                 print("FRIDAY")
                                             case False:
                                                     match i==7:
                                                         case True :
                                                             print("saturday")
                                                         case  False :
                                                             print("invalid number")

##8check a number is two digit:
i=int(input("enter the 2 digit number:"))
match  i>=10 and i <=99:
    case True:
        print("its a two digit number")
    case False:
        match -10>=i and -99<=i:
            case True:
                print("its a negative 2 digit number")
            case _:
                 print("more than two digits  so invalid")


##9check -2digit ,1digit or more:
i=int(input("enter the 2 digit number:"))
match  i>=10 and i <=99:
    case True:
        print("its a two digit number")
    case False:
        match -10>=i and -99<=i:
            case True:
                print("its a negative 2 digit number")
            case False:
                 match i>10 and i>=1:
                     case True :
                         print("its a single digit postive number")
                     case False:
                         match -10<i and -1<=i:
                             case True :
                                 print("its a single digit  negative number")
                             case False :
                                 print("more than 2 digits")
                

 ##equqlity of string:

a=input("enter  any word ")
b=input("enter any word ")
match a==b:
    case True :
        print("both the strings are equal ")
    case False:
        print("both strings are not equal ")
