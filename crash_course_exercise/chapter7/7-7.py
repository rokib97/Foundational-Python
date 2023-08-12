# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)


sandwich_orders = ['ham and cheese', 'turkey club',
                   'roast beef', 'tuna salad', 'veggie']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
