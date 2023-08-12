sandwich_orders = ['pastrami', 'turkey club',
                   'pastrami', 'roast beef', 'pastrami', 'veggie']

finished_sandwiches = []
print("Sorry, the deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop(0)
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
