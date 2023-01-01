n = int(input("Enter the number of students:"))
present, sum, min, max, absent = 0, 0, 51, -1, 0
marks = []
for i in range(n):
    temp = input("Enter marks of student "+str(i+1)+" or AB if absent:")
    marks.append(temp)
    if temp!= "AB":
        present +=1
        sum += int(temp)
        if int(temp)>max :
            max = int(temp)
        if int(temp)<min :
            min = int(temp)
    else:
        absent +=1
avg = sum / present    

print("The average score of class: ", avg)
print("Highest Score and Lowest score of class", max,"and", min)
print("count of students who were absent for the test :", absent)