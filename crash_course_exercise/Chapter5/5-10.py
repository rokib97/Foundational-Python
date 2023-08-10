current_user = ["saki", "sajib", "shafia", "rokib","tonmoy"]
new_user = ["mezba", "toky", "milton","shafia","saki"]

for value in new_user:
    if value in current_user:
        print(f"{value} will need to enter a new username.")
    else:
        print(f"username {value} is vailable")