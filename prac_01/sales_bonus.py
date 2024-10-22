"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

BONUS_THRESHOLD = 1000
MINOR_BONUS_RATE = 0.10
MAJOR_BONUS_RATE = 0.15

sales = float(input("Enter Sales: $"))
while sales >= 0:
    if sales < BONUS_THRESHOLD:
        bonus = sales * MINOR_BONUS_RATE
    else:
        bonus = sales * MAJOR_BONUS_RATE
    print(f"      Bonus: ${bonus:.2f}")
    sales = float(input("Total Sales: $"))
