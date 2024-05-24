print("Find k largest numbers in an array")
def klargest(arr,k):
    sorted_arr = arr.sort(reverse = True)
    for num in range(k):
        print(arr[num],end=' ')

arr = [1,4,5,3,7,34,25,100]
k=3
klargest(arr,k)
