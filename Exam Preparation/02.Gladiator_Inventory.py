start_inventory = input()
inventory = start_inventory.split()

data = input()

while data != 'Fight!':
    command = data.split()[0]
    equipment = data.split()[1]

    if command == 'Buy':
        if equipment not in inventory:
            inventory.append(equipment)
    elif command == 'Trash':
        if equipment in inventory:
            inventory.remove(equipment)
    elif command == "Repair":
        if equipment in inventory:
            inventory.remove(equipment)
            inventory.append(equipment)
    else:
        upgrade_item = equipment.split('-')
        if upgrade_item[0] in inventory:
            index = inventory.index(upgrade_item[0]) + 1
            inventory.insert(index, upgrade_item[0] + ':' + upgrade_item[1])

    data = input()


print(' '.join(inventory))
