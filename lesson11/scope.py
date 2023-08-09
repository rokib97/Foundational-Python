# global scope 
# name = "rokib"

# def greeting(name):
    
    
#     color = "blue"
#     print(color)
#     print(name) #refer to the paremeter variable 
    
# # print(color) not possible to access the function scope varibable
# greeting("rokib")


value = 10
def another():
    global value2
    value2 = 10
    value3 = 50
    def inside_function():
        nonlocal value3
        global value
        global value2
        value += 10
        value2 += 10
        value3 += 120
        print(value3)
    inside_function()
    
another()
    