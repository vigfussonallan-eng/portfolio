'''
Problem 2

Write a Python program, take in the price of 3 books, and then calculate the average price. 
You then want to test to see if the average price is greater than 100. 
If it is, you want to write out the average and the message "too expensive". 
Otherwise, you want to write out the average and a message that says "Okay".

'''

def validateInput(value):

    try:
        value = float(value)
        return value
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return False

priceBook1 = None
priceBook2 = None
priceBook3 = None

while priceBook1 is None:
    priceBook1 = input("Enter the price of the first book: ")
    priceBook1 = validateInput(priceBook1)
    if isinstance(priceBook1, float):
        break
    else:
        priceBook1 = None

while priceBook2 is None:
    priceBook2 = input("Enter the price of the second book: ")
    priceBook2 = validateInput(priceBook2)
    if isinstance(priceBook2, float):
        break
    else:
         priceBook2 = None
    

while priceBook3 is None:
    priceBook3 = input("Enter the price of the third book: ")
    priceBook3 = validateInput(priceBook3)
    if isinstance(priceBook3, float):
        break
    else:
        priceBook3 = None
    

average_price = (priceBook1 + priceBook2 + priceBook3) / 3

if average_price > 100:
    print(f"The average price is ${average_price:,.2f}. too expensive")
else:
    print(f"The average price is ${average_price:,.2f}. Okay")

print()
input("Press Enter to exit...")