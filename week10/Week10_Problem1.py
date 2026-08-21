'''
Problem 1 
Write a Python program to handle the following. 
Enter your pay per hour. 
Enter your desired income for the week. 
How many hours are you going to have to work to meet your desired income? 
Answers need to accommodate decimals. Display the answer.
'''

def validateInput(value):

    try:
        value = float(value)
        return value
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return False

pay_per_hour=None
desired_income=None

while pay_per_hour == None:
    pay_per_hour = input("Enter your pay per hour: ")
    pay_per_hour = validateInput(pay_per_hour)
    if isinstance(pay_per_hour, float):
        break
    else:
        pay_per_hour = None

while desired_income == None:
    desired_income = input("Enter your desired income for the week: ")
    desired_income = validateInput(desired_income)
    if isinstance(desired_income, float):
        break
    else:
        desired_income = None

hours_needed = desired_income / pay_per_hour

print(f"You need to work {hours_needed:,.2f} hours to meet your desired income of ${desired_income:,.2f}.")

if hours_needed > 24*7:
    print("Warning: The max hours per week for an individual is 168 hours working 24x7.")
    print(f"You will need to increase your pay rate to ${desired_income / (24*7):,.2f} per hour to meet your desired income of ${desired_income:,.2f}.")

print()
input("Press Enter to exit...")