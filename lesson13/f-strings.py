person = "rokib"
coins = 3

# print("\n" + person + " has " + str(coins) + " coins" + " left")

# message = "\n%s has %s coins left" %(person,coins)
# message = "\n{} has {} coins left".format(person,coins)
# message = "\n{1} has {0} coins left".format(person,coins)
# message = "\n{person} has {coins} coins left".format(person=person,coins=coins)

# print(message)

# player = {"person":"Dave", "coins":3}
# message = "\n{person} has {coins} coins left".format(**player)


# message = f"\n{person} has {coins} coins!"
# message = f"\n{person} has {coins * 2} coins!"
# message = f"\n{person.lower()} has {coins * 2} coins!"


# player = {"person":"Dave", "coins":3}
# message = f"\n{player['person']} has {coins * 2} coins!"
# print(message)


# you can pass formatting options 

num = 10
# print(f"\n2.25 times {num} is {2.25 * num:.2f}")
for num in range(1,11):
    print(f"{num}  devided by 4.25 is {num / 4.25:.2%}")