inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] = ['seashell', 'strange berry', 'lint']
inventory["backpack"].remove("dagger")
inventory["gold"] = 550
for i, j in inventory.items():
    print(i, j)
