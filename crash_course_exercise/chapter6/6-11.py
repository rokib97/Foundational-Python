cities = {
    "Dhaka": {
        "population": 40000000,
        "country": "Bangladesh",
        "fact": "over poluted city in the world"
    },

    "Khulna": {
        "population": 4000000,
        "country": "Bangladesh",
        "fact": "beatiful and small city in Bangladesh"
    },

    "Chittagong": {
        "population": 4000000,
        "country": "Bangladesh",
        "fact": "over flooded city in the world"
    }
}

for city_name, description in cities.items():
    print(f"\n{city_name}")
    for key, value in description.items():
        print(f"\t{key} ========= {value}")
