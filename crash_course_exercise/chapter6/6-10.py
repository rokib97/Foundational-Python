friends_info = {
    "shakib": [10, 52, 30, 25],
    "rakib": [71, 252, 12, 0, 48],
    "hasi": [69, 96, 59, 79, 63,],
    "dalia": [23, 14, 45, 78, 62],
    "shakiya": [99, 120, 44, 65, 23],
    "saki": [69, 69, 69, 69],
    "monir": [120, 1520, 458, 25, 255]
}

for name, numbers in friends_info.items():
    print(f"\n{name}'s favourite numbers are: ")
    for number in numbers:
        print(number)
