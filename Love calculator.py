name1=input("Enter your name : ")
name2=input("Enter your favourite person name with whom you want to test using love calculator : ")

combine_string=name1.lower()+name2.lower()
t= combine_string.count('t')
r=combine_string.count('r')
u=combine_string.count('u')
e=combine_string.count('e')

l=combine_string.count('l')
o=combine_string.count('o')
v=combine_string.count('v')
e=combine_string.count('e')

total=t+r+u+e+l+o+v+e
if total<10 or total>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total>=40 and total<=50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}, no comments!")