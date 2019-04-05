import math

monthly_budget = float(input())
number_clients = int(input())
gigabytes_data = int(input())
number_hosts = int(input())
expected_uptime = float(input())

survers_needed = math.ceil(number_clients / 50)
storage_needed = math.ceil(gigabytes_data / 0.5)
hourly_cost = ((2 * survers_needed) + (0.5 * storage_needed)) * 24
hosts_cost = number_hosts * 10
montly_cost = hourly_cost * 30
total = (montly_cost + hosts_cost) * (expected_uptime / 100)

if monthly_budget >= total:
    leftover = monthly_budget - total
    print(f"Clouds Ahoy! Monthly cost: ${total:.2f} (${leftover:.2f} leftover)")
else:
    more = total - monthly_budget
    print(f"Stay Grounded! Monthly cost: ${total:.2f} (Need ${more:.2f} more)")
