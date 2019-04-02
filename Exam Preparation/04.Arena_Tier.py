gladiator_pool = {}
data = input()

while data != 'Ave Cesar':

    if len(data.split(' -> ')) == 3:

        data = data.split(' -> ')
        name = data[0]  
        technique = data[1]
        skill = int(data[2])

        if name not in gladiator_pool:
            gladiator_pool[name] = {technique: skill}
        else:
            if technique not in gladiator_pool[name]:
                gladiator_pool[name].update({technique: skill})
            else:
                if skill > gladiator_pool[name][technique]:
                    gladiator_pool[name][technique] = skill
    else:
        data = data.split(' vs ')
        gladiator1 = data[0]
        gladiator2 = data[1]

        if gladiator1 in gladiator_pool and gladiator2 in gladiator_pool:
            for item, value in gladiator_pool[gladiator1].items():
                if item in gladiator_pool[gladiator2] and \
                        value > gladiator_pool[gladiator2][item]:
                    del gladiator_pool[gladiator2]

    data = input()

sorted_gladiators = sorted(gladiator_pool.items(), key=lambda kvp: kvp[0])
total_skill = {}

for key, value in gladiator_pool.items():
    for x in value:
        if key not in total_skill:
            total_skill[key] = value[x]
        else:
            total_skill[key] = total_skill[key] + value[x]

total_skill = sorted(total_skill.items(), key=lambda x: (-x[1], x[0]))

for item in total_skill:
    print(f"{item[0]}: {item[1]} skill")
    current_sorting = sorted(gladiator_pool[item[0]].items(),
                             key=lambda x: (-x[1], x[0]))
    for i in current_sorting:
        print(f"- {i[0]} <!> {i[1]}")
