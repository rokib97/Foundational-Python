major_rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

# for name, country in set(major_rivers.items()):
#     print(f'The {name} runs through {country}')

# for name in major_rivers.keys():
#     print(name)

for country in major_rivers.values():
    print(country)
