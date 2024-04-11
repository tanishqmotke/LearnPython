name = "Harry"
print(name[-4:-2])
print(name[len(name)-4:])

#String Methods
# To find the length of the strings
print(len(name))

#Upper method and lower method
firstname ="tanu !!!! TanIshQ  MoTKE    !!!!!"
print(firstname.upper()) # it will convert all the string in CAPITAL letters.
print(firstname.lower()) # it will convert the string in smallcase.
print(firstname.strip()) # it will remove spaces before and after the string.
print(firstname.rstrip("!")) # it will remove the trailing characters present in the right side of the string.
print(firstname.replace('!','%')) # it will replace all the occurences of a string with another string.
print(firstname.split(" ")) # split method splits the given string at the specified isntance and return the separated strings as list items.
print(firstname.capitalize()) #It turns only the first character of the string to uppercase and rest other characters are turned into lowercase.
print(firstname.center(100)) #the method aligns the string to the center as per the parameter
print(firstname.count('a')) #the method returns the number of times the given value has occured within the given string.
print(firstname.endswith('!!')) #it checks if the string ends with a given value. If yes then return true, else false.
print(firstname.endswith("!!!", 3, 8)) # we can even check for a value in between the given index positions.
print(firstname.find("MoTKE")) #searches for the first occurrence of the given value. If not present then return -1
print(firstname.index('M'))
print(firstname.isalnum()) # it returns true only if the entire string only consists of A-Z,a-z,0-9.If any other characters are present, then it returns False.
print(firstname.isalpha()) #same as isalnum just it return true only for alphabets
print(firstname.islower()) #returns true is everything is in lowercase else false.
print(firstname.isprintable()) #returns true for all the string (\n will return false as it is not printed)
surname = "     "
print(surname.isspace()) #returns true if only spaces are there in the string.
print(firstname.istitle()) #returns true is all the first letter of each word in string is capitalized else false.
print(firstname.isupper()) #returns true if everything is in uppercase.
print(firstname.startswith("tanu")) #returns true is string starts with given value else false.
print(firstname.swapcase()) #it changes capital letter in string to smallercase and vise versa.
print(firstname.title()) #it will capital the first letter of each word in the string.


