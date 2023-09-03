print("Welcom to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_prcnt = (
    float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
)
bill_plus_tip = bill + (bill * tip_prcnt)
people_to_split = int(input("How many people to split the bill? "))
amount_to_pay_each = round(bill_plus_tip / people_to_split, 2)
print(f"Each person should pay: ${amount_to_pay_each}")
