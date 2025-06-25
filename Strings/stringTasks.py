#######################################string methods######################################
##rfind :
a= "the promise of quality and authentcity"
print(a.rfind("e"))

##rindex:
a= "the promise of quality and authentcity"
print(a.rindex("of"))

##rjust:
a=" yuktha "
print(a.rjust(50))

##rpartition
y="i am yuktha"
print(y.rpartition("am"))


##rsplit
p=" hello world"
print(p.rsplit("w"))

##rstrip:
p="                                             hello world"
print(p.strip ())

##split:
p=" hello, world"
print(p.split(","))
##difference between strip and rstrip:
s = "!!hello!!"
print(s.strip("!"))   # Output: "hello"
print(s.rstrip("!"))  # Output: "!!hello"

##difference between split and rsplit:
s = "one,two,three,four,five,six,seven"
p=s.split(',', 2)
print(p)
# Output: ['one', 'two', 'three,four']

s = "one,two,three,four,five,six"
p=s.rsplit(',', 2)
print(p)

# Output: ['one,two', 'three', 'four']

##splitlines:
d="hello \n world"
print(d.splitlines())


##startswith:
u="my self yuktha"
h=u.startswith("am")
print(h)

##strip:
txt = "     banana     "
x = txt.strip()
print(x)

txt = "     banana     "
x = txt.strip()
print("of all the fruits",x,"its my fav")

##swapcase:
p="I Am YukTha"
x=p.swapcase()
print(x)

##title
p="myself yuktha"
print(p.title())

##zfill
p="90"
d=p.zfill(3)
print(d)

##slicing :
o="yuktha sri"
print(o)
print(o[0:3])
print(o[7:10])
print(o[0:6])

## python built in methods:
p="   i am a super man     "
print(p.upper())
print(p.lower())
print(p.strip())
print(p.replace("man","women"))
print(p.split("a"))