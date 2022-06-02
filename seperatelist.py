list=[1,2,'r','v',3.4,2.9,'wer']
int_list=[]
str_list=[]
for i in list:
    if type(i) is int or type(i) is float:
        int_list.append(i)
    else:
        str_list.append(i)

print(int_list)
print(str_list)