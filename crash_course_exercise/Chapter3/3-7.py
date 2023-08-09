members = ["saki", "sahakib", "Papi"]
print("welcome to the Dinner party " + members[0] + ".")
print("welcome to the Dinner party " + members[1] + ".")
print("welcome to the Dinner party " + members[2] + ".")
print("\nUnfortunately! My Friend " + members[1] + " can't make it today!\n")
members[1] = "Jesia"
print("welcome to the Dinner party " + members[0] + ".")
print("welcome to the Dinner party " + members[1] + ".")
print("welcome to the Dinner party " + members[2] + ".")

print("\nI have Found A Big Dinner Table, Time To invite More Peoples\n")

members.insert(0,"Shafia")
members.insert(2,"chaity")
members.append("Sriti")
print("\n")
print("welcome to the Dinner party " + members[0] + ".")
print("welcome to the Dinner party " + members[1] + ".")
print("welcome to the Dinner party " + members[2] + ".")
print("welcome to the Dinner party " + members[3] + ".")
print("welcome to the Dinner party " + members[4] + ".")
print("welcome to the Dinner party " + members[-1] + ".")
print("\nSorry ! I can invite only two people for now\n")

first_person = members.pop()
print("Sorry " + first_person + " can't invite you!")
second_person = members.pop(-1)
print("Sorry " + second_person + " can't invite you!")
third_person = members.pop(-1)
print("Sorry " + third_person + " can't invite you!")
fourth_person = members.pop(-1)
print("Sorry " + fourth_person + " can't invite you!")

print("\n\nYour are still invited: " + members[0])
print("Your are still invited: " + members[1])

del members[0]
del members[0]
print("\nNo more people to invite the party ! Game Over!😢")