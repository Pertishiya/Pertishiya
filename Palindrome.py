print("Palindrome")
name1 = input("Enter your name: ")
if name1.lower() == name1.lower()[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
