def partition(arr,low,high):
    i=low-1
    pi=arr[high]
    for j in range(low,high):
        if arr[j]<=pi:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quicksort(arr,low,high):
    if low<high:
        piv=partition(arr,low,high)
        quicksort(arr,low,piv-1)
        quicksort(arr,piv+1,high)
if __name__ == "__main__":
    
        a=input()
        a=a.split()
        a=[int(x) for x in a]
        quicksort(a,0,len(a)-1)
        print(a)
