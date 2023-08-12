while True:
    age = int(input("Whats your age? "))
    if age < 3:
        print(f"Your ticket is free because your age is {age}")
        break
    elif age >= 3 or age <= 12:
        print(f"Your ticket is $10 because your age is {age}")
        break
    else:
        print(f"Your ticket is $15 because your age is {age}")
        break
