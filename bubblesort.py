def bubblesort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

if __name__ == "__main__":
    a=input() 
    a=a.split()
    a=[int(x) for x in a]
    print(bubblesort(a))

