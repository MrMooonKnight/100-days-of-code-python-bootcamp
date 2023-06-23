print("Welcome To The Tip Calculator.")
bill = float(input("What was the total bill? $"))
tipPercent = float(input("What percentage of tip would you like to give? 10, 12 or 15? "))
people = float(input("How many people to split the bill? "))

tip = bill * tipPercent / 100
bill += tip
bill /= people
finalBill = round(bill,2)
print(f"Each Person Will Pay : ${finalBill}")
