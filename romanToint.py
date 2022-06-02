def romanToInt(roman):
    my_dict={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    num=0
    for i in range(len(roman)):
        if i>0 and my_dict[roman[i]]>my_dict[roman[i-1]]:
            num=my_dict[roman[i]]-num
        else:
            # print(i)
            num += my_dict[roman[i]]
            i += 1
    return num


print(romanToInt('II'))
print(romanToInt('IV'))
print(romanToInt('XI'))