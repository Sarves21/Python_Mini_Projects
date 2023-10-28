#Tip Calculator
bill = float(input("Enter the total bill amount "))
tip = int(input("How much tip would you like to give?"))
tip_as_percent = tip / 100
people = int(input("How many people are there to split the bill amount?"))
total_tip_amount = bill * tip_as_percent
total_amount = bill + total_tip_amount
bill_per_person = total_amount/people
final_amount = round(bill_per_person,2)
print(f"Each person should pay : {final_amount}")
