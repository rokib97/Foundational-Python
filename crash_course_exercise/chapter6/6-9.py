favorite_places = {
    "rokib": ["India", "china", "indonesia"],
    "rakib": ["USA", "bhutan", "maldives"],
    "hasan": ["Pakistan", "germany", "finland"]
}


for name, places in favorite_places.items():
    print(f"\n{name}'s fav places are: ")
    for country in places:
        print(f"\t{country.title()}")
