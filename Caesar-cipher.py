def caesar(text,shift,direction):
    end=""
    if direction=="decode":
        shift*=-1
    for char in text:
        if char in alphabet:
            pos=alphabet.index(char)
            new_pos=(pos+shift)%26
            end+=alphabet[new_pos]
            print(end)
        else:
            end+=char #space or numbers will retain
    print(f"Here the {direction} for {text} is {end}")

is_over=True
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while is_over:
    direction=input("Type 'encode' to encrypt or 'decode' to decrypt message: ").lower()
    text=input("Enter your message: ").lower()
    shift=int(input("Enter the shift number: "))
    shift=shift%26
    print(shift)
    caesar(text,shift,direction)
    restart=input("Type 'yes' if you want to go again. Otherwise type 'no' to end.\n").lower()
    if restart=="no":
        is_over=False
        print("Good Bye")

