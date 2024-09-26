"""
get:
    price per kWh in cents,
    daily use in kWh,
    number of days in the billing period
display:
    estimated bill
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator")
# unit_price = float(input("Enter cents per kWh: "))
tariff = int(input("Which tariff? 11 or 31: "))
while tariff != 11 and tariff != 31:
    print("Invalid tariff")
    tariff = int(input("Which tariff? 11 or 31: "))
daily_usage = float(input("Enter daily use in kWh: "))
billing_period = int(input("Enter number of billing days: "))
if tariff == 11:
    total_price = TARIFF_11 * daily_usage * billing_period
else:
    total_price = TARIFF_31 * daily_usage * billing_period
# total_price = unit_price * daily_usage * billing_period
print(f"Estimated bill: ${total_price:.2f}")
