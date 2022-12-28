#Exp no.3
Books=[]
for i in range(int(input("Enter number of books:"))):
    name=input(f"Enter name of book{i+1}:")
    price=input(f"Enter the price of book{i+1}:")
    Books.append({"name":name,"price":int(price)})
print(Books)

#remove duplicate entries
for index,i in enumerate(Books):
    for index2,j in enumerate(Books):
        if index!=index2:
            if i["name"]==j["name"]:
                Books.pop(index)
print("Books with Unique names:")
print(Books)

#Display in ascending order
Books.sort(key=lambda x:x["price"])
print("sorted:")
print(Books)

#cost more than 500
for Book in Books:
    if Book["price"]>500:
        print(f"{Book['name']} has price more than 500")

#cost less than 500
new_list=[]
for Book in Books:
    if Book in Books:
        if Book["price"]<500:
            print(f"{Book['name']} has price less than 500")
    new_list.append(Book)

