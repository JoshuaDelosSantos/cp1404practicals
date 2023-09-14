"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BASE_BONUS_RATE = 0.1
ADDITIONAL_BONUS_RATE = 0.05

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * BASE_BONUS_RATE
    else:
        bonus = sales * (BASE_BONUS_RATE + ADDITIONAL_BONUS_RATE)
    print(f"With {sales} sales, your bonus is {bonus:.2f}!")
    sales = float(input("Enter sales: $"))

print("Thank you for your time!")
