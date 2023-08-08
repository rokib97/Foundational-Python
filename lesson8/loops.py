# while loop 
# value = 1
# while value <=10:
#     print(value)
#     if(value == 5):
#         break
#     value += 1
    
    

# i = 1
# while (i <= 10):
    
#     if( i == 5):
#         i += 1
#         continue
#     print(i)
#     i += 1
# else:
#     print("The value of i outside of the loop is: " + str(i))
    
# Basic  for loop 
names = ["rokib", "sara", "Totini"]

# looping through a list 
# for name in names:
#     print(name)
    
# looping through string 
# for x in "rokib":
#     print(x.upper())
    
# break inside for loop 
# for name in names:
#     if name == "totini".title():
#         break
#     print(name)

# continue inside for loop 
# for name in names:
#     if name == "sara":
#         continue
#     print(name)


# looping through a range 
# for x in range(10): #0 to 9
#     print(x)
    
# range start and end 
# for x in range(1,11): # 1 to 10
#     print(x)
    
# range increment value 
# for x in range(5,101,5):
#     print(x)
# else:
#     print("Glad that's over!")

# nested loops 
names = ["rokib", "sara", "Totini"]
actions = ["code", "eat", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")