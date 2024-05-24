print("Tresury Map\n")

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

abc = ['a','b','c']
letter = position[0].lower()
number = position[1]
letter_index = abc.index(letter)
number_index = int(position[1])-1
map[letter_index][number_index] = 'X'


print(f"{line1}\n{line2}\n{line3}")
