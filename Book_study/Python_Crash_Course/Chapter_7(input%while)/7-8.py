sandwich_orders = ['applepai', 'bananapai', 'tomotapai']
finished_wandwiches = []
while sandwich_orders:
    FOOD = sandwich_orders.pop()
    print("I made your " + FOOD)
    finished_wandwiches.append(FOOD)
for i in finished_wandwiches:
    print(i)