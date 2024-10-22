"""
get:
    price per kWh in cents,
    daily use in kWh,
    number of days in the billing period
display:
    estimated bill
"""

TARIFF_TO_COST = {11: 0.2446180, 16: 0.2176955, 21: 0.1907730,
                  26: 0.1638505, 31: 0.1369280}

print("Electricity bill estimator")
print(f"Valid Tariffs: {", ".join([str(key) for key in TARIFF_TO_COST.keys()])}")
tariff = int(input("Tariff: "))
while tariff not in TARIFF_TO_COST.keys():
    print("Invalid tariff")
    tariff = int(input("Tariff: "))
daily_usage = float(input("Enter daily use in kWh: "))
billing_period = int(input("Enter number of billing days: "))
total_price = TARIFF_TO_COST[tariff] * daily_usage * billing_period
print(f"Estimated bill: ${total_price:.2f}")
