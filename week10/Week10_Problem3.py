'''
Problem 3

You are at a restaurant and you get a bill for the food and another bill for the drink.
You need to get a total. Next, you want to calculate the tax using 6.2%. 
Finally, you want to add a 15% tip. 
You want to display the total for food and drink, the total after taxes have been added, and the total after the percent has also been added.
'''


def validateInput(value):

    try:
        value = float(value)
        return value
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return False

priceFood = None
priceDrink = None

while priceFood is None:
    priceFood = input("Enter the price of the food: ")
    priceFood = validateInput(priceFood)
    if isinstance(priceFood, float):
        break
    else:
        priceFood = None

while priceDrink is None:
    priceDrink = input("Enter the price of the drink: ")
    priceDrink = validateInput(priceDrink)
    if isinstance(priceDrink, float):
        break
    else:
        priceDrink = None

totalprice = priceFood + priceDrink
tax = totalprice * 0.062
totalpricetax = totalprice + tax
tip = totalpricetax * 0.15
totalpricetip = totalpricetax + tip

print()
print("Resaurant Bill")
print()
print(f"Total for food and drink: ${totalprice:,.2f}")
print(f"Total after 6.2% taxes: ${totalpricetax:,.2f}")
print(f"Total after 15% tip: ${totalpricetip:,.2f}")

print()
input("Press Enter to exit...")