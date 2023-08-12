# Initialize an empty dictionary to store poll results
dream_vacation_poll = {}

# Set a flag to indicate whether the polling should continue
polling_active = True

while polling_active:
    # Prompt the user for their dream vacation
    name = input("What's your name? ")
    destination = input(
        "If you could visit one place in the world, where would you go? ")

    # Store the user's response in the dictionary
    dream_vacation_poll[name] = destination

    # Check if another user wants to participate in the poll
    another_response = input(
        "Would you like to let another person respond? (yes/no) ")
    if another_response.lower() == 'no':
        polling_active = False

# Print the poll results
print("\n--- Dream Vacation Poll Results ---")
for name, destination in dream_vacation_poll.items():
    print(f"{name} would like to visit {destination}.")
