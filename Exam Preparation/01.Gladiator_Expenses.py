lost_fight = int(input())

helmets = [x for x in range(2, lost_fight+1, 2)]
swords = [x for x in range(3, lost_fight+1, 3)]
shields = []

for item in helmets:
    for item2 in swords:
        if item == item2:
            shields.append(item)

armors = [x for x in range(2, len(shields)+1, 2)]

helmet_price = input()
sword_price = input()
shield_price = input()
armor_price = input()

result = (
    float(helmet_price) * len(helmets)) + \
    (float(sword_price) * len(swords)) + \
    (float(shield_price) * len(shields)) + \
    (float(armor_price) * len(armors))

print(f"Gladiator expenses: {float(result):.2f} aureus")
