inventory = {
    'device': 'phone',
    'model' : 'Samsung'
}

product = input()


if product not in inventory:
    inventory[product] = 0

print(inventory)        