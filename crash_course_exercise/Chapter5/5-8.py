users = ["admin", "adult", "female", "male", "minor"]

for value in users:
    if value == "admin":
        print(f"Hello {value},would you like to see a status report?")
    print(f"Hello {value}, thank you for log in again!")