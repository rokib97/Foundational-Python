people_list = ["rokib", "sara", "tani"]

fav_language = {
    "shakib": "python",
    "sriti": "java",
    "rokib": "c",
    "saki": "javaScript",
    "bizli": "lua",
    "tani": "c++",
}

for name in fav_language.keys():
    if name in people_list:
        print(f"Thanks {name} for taking the poll")
    print(f"Please {name}! Hyrry up to taking the poll.")
