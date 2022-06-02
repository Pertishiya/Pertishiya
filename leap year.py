year=int(input("Enter the year to find leap year or not: "))

if year%4==0:
    if year%100!=0:
        print("Leap year")
    elif year%100==0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not a leap year")
