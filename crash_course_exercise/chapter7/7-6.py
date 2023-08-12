prompt = "\nPlease Enter Your Pizza Toppings name? "
prompt += "\n write quit to quit the pormpt "

is_active = True
while is_active:
    message = input(prompt)
    if message == "quit":
        is_active = False
    else:
        print(message)
