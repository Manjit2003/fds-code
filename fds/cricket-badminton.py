#Exp no.1
SE=[1,2,3,4,5,6,7,8,9,10]
cricket=[1,2,4,6,8,9]
badminton=[1,3,4,7,8]
football=[1,2,5,6,9]
def A1():
    D=[]
    for i in cricket:
        for j in badminton:
            if i==j:
                D.append(i)
    print("1.List of students who play both cricket and badminton:",D)
def A2():
    E=[]
    for i in cricket:
        if i not in badminton:
            E.append(i)
    for j in badminton:
        if j not in cricket:
            E.append(j)
    print("2.List of students who play either cricket or badminton but not both:",E)
def A3():
    F=[]
    G=[]
    for i in cricket:
        G.append(i)
    for i in badminton:
        if i not in cricket:
            G.append(i)
    for i in SE:
        if i not in G:
            F.append(i)
    print("3.Number of students who play neither cricket nor Badminton:",F)
def A4():
    H=[]
    I=[]
    for i in cricket:
        for j in football:
            if i==j:
                I.append(i)
    for i in I:
        if i not in badminton:
            H.append(i)    
    print("4.No. of students who play cricket and football but not badminton",H)
print("Menu\n1.List of students who play both cricket and badminton\n2.List of students who play either cricket or badminton but not both\n3.Number of students who play neither cricket nor Badminton\n4.No. of students who play cricket and football but not badminton")
ch=int(input("Enter your choice:"))
if ch==1:
    A1()
elif ch==2:
    A2()
elif ch==3:
    A3()
elif ch==4:
    A4()
else:
    print("You have entered wrong choice.")
