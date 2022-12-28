#Exp no.7
def Quick(arr,low,high):
   if(low<high):
      m=Partition(arr,low,high) 
      Quick(arr,low,m-1)
      Quick(arr,m+1,high)
def Partition(arr,low,high):
    pivot = arr[low]  
    i=low+1
    j=high
    flag = False
    while(not flag):
        while(i<=j and arr[i]<=pivot):
            i =i+1
        while(i<=j and arr[j]>=pivot):
            j = j-1
        if(j<i):
            flag = True
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp
    return j
print("\n Program for Quick sort")
print("\n Enter elements in array:")
n = int(input())
array =[]
i=0
for i in range(n):
    print("\n Enter element in Array")
    item = int(input())
    array.append(item)    
print("original array is\n")
print(array)
Quick(array,0,n-1)
print("\n Sorted Array is")
print(array)