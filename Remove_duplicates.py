print("Remove duplicates")

def remove_duplicate(arr):
    #seen = set()
    unique_arr=[]
    for num in arr:
        if num not in unique_arr:
            #seen.add(num)
            unique_arr.append(num)
    return unique_arr
    
arr=[1,2,1,2,2,7,7,4,4,5,5]
print(remove_duplicate(arr))
