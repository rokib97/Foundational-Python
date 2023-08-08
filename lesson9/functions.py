# declare function 

def hello_world():
    print("Hello From Function!")   
# hello_world()s


# parameter and arguments 
def add(a,b):
    return a + b

result2 = add(10,23)
result = add(100,230)
# print(result)


# checking arguments type 

# def sum(num1=0,num2=0):
#     if(type(num1) is not int or type(num2) is not int):
#         return 0
#     else:
#         return num1 + num2
    
# result = sum(10,20)
# print(result)


# def multiple_items(*args):
#     print(args)
#     print(type(args))
    
# multiple_items(10,20,30,40)
    
    
    
def mult_names_items(**kwargs):
    print(kwargs)
    

mult_names_items(first = "rokib",last ="hasan")