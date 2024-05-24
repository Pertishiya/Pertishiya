print("FizzBuzz\n")
target = 100
for num in range (1,target+1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz\n")
    elif num % 3 == 0:
          print("Fizz\n")
    elif num % 5 == 0:
          print("Buzz\n")
    else:
          print(num)
          print("\n")
