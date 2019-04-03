star = input()
distance = int(input())
budget = int(input())
fuel_consumption = float(input())
gas_price = float(input())

liters_gm = fuel_consumption / 100
price_gm = liters_gm * gas_price

result = distance * price_gm

if result < budget:
    leftover = budget - result
    print(f"Off to {star} with ${leftover:.2f} for snacks")
else:
    leftover = result - budget
    print(f"Maybe another time, need ${leftover:.2f} more")
