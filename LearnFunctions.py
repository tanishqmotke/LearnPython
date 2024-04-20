def Name(firstname):
    print('My name is :'+ firstname)

Name("Tanishq")

def Name(firstname,surname):
    print(firstname,surname)

Name('Tanishq','Motke')

print("--------------------")
print("Arbitary Arguments")
print("--------------------")

def Name(*firstname):
    print(firstname[2])
Name('Tanishq','Raj','Suresh')

print("--------------------")
print("Keyword Arguments")
print("--------------------")

def Name(firstname,surname):
    print("My name is "+firstname,surname)

Name(firstname="Tanishq",surname="Motke")

print("--------------------")
print("Arbitary Keyword Arguments")
print("--------------------")

def Name(**names):
    print("My name is "+ names['firstname'])

Name(firstname="tanu",lastname="motke",firstnames="Tanishq")

print("--------------------")
print("List as an Argument")
print("--------------------")
def NameofFruits(listofFruits):
    for x in fruits:
        print(x)

fruits=["Apple","Banana","Orange"]
NameofFruits(fruits)

print("--------------------")
print("Return")
print("--------------------")

def addNumber(num):
    return 2 + num

print(addNumber(2))
addNumber(4)