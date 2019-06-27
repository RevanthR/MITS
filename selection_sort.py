def selection_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

if __name__ == "__main__":
    a=input() 
    a=a.split()
    a=[int(x) for x in a]
    print(selection_sort(a))

