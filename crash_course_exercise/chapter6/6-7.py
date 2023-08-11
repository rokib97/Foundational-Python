person = {
    "first_name": "rokib",
    "last_name": "hasan",
    "city": "Dahak, Bangladesh",
    "age": 25,

}
person2 = {
    "first_name": "saahid",
    "last_name": "rabbani",
    "city": "khulna, Bangladesh",
    "age": 22,

}
person3 = {
    "first_name": "nabila",
    "last_name": "chy",
    "city": "ctg, Bangladesh",
    "age": 27,

}

peoples = [person, person2, person3]

for people in peoples:
    print(
        f"{people['first_name']} is {people['age']} years old and lives in {people['city']}.")
