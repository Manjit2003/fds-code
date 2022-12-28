def insertionSort(marks):
    
    for step in range(1, len(marks)):
        key = marks[step]
        j = step - 1
        while j >= 0 and key < marks[j]:
            marks[j + 1] = marks[j]
            j = j - 1
        marks[j + 1] = key
        print("\npass#", (i + 1))
        print(marks)

def shellSort(marks,n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = marks[i]
            j = i
            while j >= interval and marks[j - interval] > temp:
                marks[j] = marks[j - interval]
                j -= interval

            marks[j] = temp
        interval //= 2

        print("\npass#", (j + 1))
        print(marks)

def top_five_marks(marks):
    print("top 5 Marks are : ")
    print(*marks[:4:-1], sep=" ")


marks = []
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for", n, "students (Press ENTER after every students marks): ")
for i in range(0, n):
    ele = float(input())
    marks.append(ele)

print("The marks of", n, "students are : ")
print(marks)

flag = 1
while flag == 1:
    print("\n---------------MENU---------------")
    print("1. insertion Sort of the marks")
    print("2. shell Sort of the marks")
    ch = int(input("\n\nEnter your choice (from 1 to 3) : "))

    if ch==1:
        print("Marks of students after performing insertion Sort on the list : ")
        insertionSort(marks)
        top_five_marks(marks)
        break
    elif ch==2:
        print("Marks of students after performing shell Sort on the list :")
        shellSort(marks)
        top_five_marks(marks)

    else:
        print("\nEnter a valid choice!!")
        print("\nThanks for using this program!!")
        flag = 0
