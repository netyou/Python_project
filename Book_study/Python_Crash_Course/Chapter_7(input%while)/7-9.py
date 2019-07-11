sandwich_orders = ['applepai', 'bananapai', 'tomotapai', 'pastrami', 'pastrami', 'pastrami']
print("Pastrami has been sold out！")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_wandwiches = []
while sandwich_orders:
    FOOD = sandwich_orders.pop()
    print("I made your " + FOOD)
    finished_wandwiches.append(FOOD)
for i in finished_wandwiches:
    print(i)