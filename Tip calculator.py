#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!\n")
bill=float(input("What was the total bill? $"))
tip_percent=int(input("How much tip would you like to give in percentage? 10, 12, or 15?"))
people=int(input("How many people to split the bill?"))

tip_amount=bill*(tip_percent/100)
total_bill=bill+tip_amount
amount_per_person=total_bill/people
final_amount=round(amount_per_person,2)
print(f"Each person should pay : ${final_amount}")

