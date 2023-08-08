# string data type 

# literal assignment 

first_name = "Rokib"
last_name = "Hasan"
# print(type(first_name))
# print(type(first_name) == str)
# print(isinstance(first_name, str))

# constructor function 

myName = str("Hasan")
# print(type(myName))
# print(type(myName) == str)
# print(isinstance(myName, str))

# concatenating 
full_name = first_name + " " + last_name
full_name += "!" + " Hello"
# print(full_name)

# casting a number to a string

the_year = str(1980)
statement = "I like the movie from " + the_year + " and i loved it"
# print(statement)

# multi line string 
multipline = """
Hey, This is Rokib.
    I don't know how to write multiline but i am escaping a tab.
                let's make the world a better place together.
"""
# print(multipline)

# escaping special caharacters 

sentence = 'I\'am back at work.\tHey!\n\nWhere\'s this at \\located?'
# print(sentence)


# string method 
# print(first_name)
# print(first_name.lower())
# print(first_name.upper())
# print(first_name)

# print(multipline.title())
# print(full_name.replace(first_name," MyNameIsRokib"))


# check string length 
# print(len(first_name))
first_name+= "                                        "
first_name+= "                   " + first_name
# print(len(first_name))

# remove white space 
white_space_example = "     Hello    "
# print(white_space_example)
# print(white_space_example.strip())
# print(white_space_example.lstrip())
# print(white_space_example.rstrip())


# Building a menu 

title = "menus".upper()
# print(title.center(20,"="))
# print("Coffee".ljust(16,".") + "$1".rjust(4))
# print("Muffin".ljust(16,".") + "$5".rjust(4))
# print("CheeseCake".ljust(16,".") + "$10".rjust(4))


# string index and index range 
new_name = "Brokib"
# print(new_name[0])
# print(new_name[-1])
# print(new_name[0:-1]) 
# print(new_name[0:1]) # last value excluded 


# Boolean Data Type 

# print(new_name.startswith('b'.upper()))
print(new_name.endswith('B'))

my_value  = False
x = bool(False)
# print(x)
# print(type(x))
# print(isinstance(my_value,bool))


# Numeric data type 
price = 100
best_price = int(80)
# print(type(price))
# print(isinstance(best_price,int))

# float 

gpa = 3.18
my_gpa = float(2.97)

# print(type(gpa))
# print(isinstance(my_gpa,float))

# complex type 
com_value = 5 + 3J
# print(type(com_value))
# print(com_value.real)
# print(com_value.imag)


# Built in numeric function

# print(abs(gpa * -1))
# print(round(gpa,1))


import math
# print(math.pi)
# print(math.ceil(3.12))
# print(math.floor(3.12))
# print(int(math.sqrt(64)))
# print(math.ceil(math.sqrt(124)))


# type casting 

zip_code = "1216"
zip_value = int(zip_code)
# print(type(zip_value))