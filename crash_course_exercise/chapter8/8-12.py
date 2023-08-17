def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print("- " + ingredient)
    print("Sandwich is ready!\n")


make_sandwich("Turkey", "Lettuce", "Tomato", "Mayonnaise")
make_sandwich("Ham", "Swiss Cheese", "Mustard")
make_sandwich("Peanut Butter", "Jelly")
