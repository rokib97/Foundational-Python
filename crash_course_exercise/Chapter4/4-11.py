foods = ["pizza", "burger", "pasta"]

# for food in foods:
#     print(f"I like {food}.")
# else:
#     print("I really love Pizza!")
    
friends_foods = foods[:]
# friends_foods = foods.copy()
# friends_foods = list(foods)

foods.append("noodles")
friends_foods.append("fruits")

print("My Favourite Foods are: ")
for food in foods:
    print(food)
    
print("\nMy Friends Favourite Foods are: ")
for food in friends_foods:
    print(food)