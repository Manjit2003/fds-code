def union(a,b):
    ans=a.copy()
    for i in b:
        if i not in a:
            ans.append(i)
    return ans

def intersection(a,b):
    ans=[]
    for i in a:
        if i in b:
            ans.append(i)
    return ans

def minus(a,b):
    ans=[]
    for i in a: 
        if i not in b:
            ans.append(i)
    return ans  

u = input("Enter the union list:").split(",")
b = input("Enter the badminton list:") .split(",")
c = input("Enter the cricket list:").split(",")
f = input("Enter the football list").split(",")
print("List of students who play both cricket and badminton:",intersection(b,c))
print("Number of students who play niether cricket not badminton",minus(minus(u,b),c))       
print("Number of students who play cricket and badminton",minus(intersection(c,f),b)) 