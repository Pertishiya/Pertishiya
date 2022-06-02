
small_pizza=15
medium_pizza=20
large_pizza=25
pepperoni_small=2
pepperoni_others=3
extra_cheese=1

size=input("Enter the size of pizza: ")
add_pepperoni=input("Do you want to add pepperoni? Y or N?: ")
add_cheese=input("Do you want extra cheese? Y or N?: ")
bill=0
if size=='S':
    bill+=small_pizza
elif size=='M':
    bill+=medium_pizza
elif size=='L':
    bill+=large_pizza
else:
    print("Invalid input")

if add_pepperoni=='Y':
    if size=='S':
        bill+=2
    else:
        bill+=3

if add_cheese=='Y':
        bill+=extra_cheese

print("Your final bill is : $ ",bill)