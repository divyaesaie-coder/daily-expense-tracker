#QUESTION:Program to track expences,group by category and calculate total spending.
users=[]#made an empty list
n=int(input("How many entries?"))#user input
for i in range(n):#created a loop for entries
    user={
        "Amount":float(input("Enter the money:")),
        "Category":input("Enter the category(food/shopping/transport/other):")
        }#entering the data
    users.append(user)#adding it to the empty list
print(users)#printing the empty com filled list
category_total={}#created a empty dict for total amount according to category
for item in users:#its a loop again
    category=item["Category"]#importing the category from the users of the above list
    amount=item["Amount"]#importing the amount of category from the users of the above list
    if category in category_total:
        category_total[category]+=amount
    else:
        category_total[category]=amount
print(category_total)
total_expense=0
for item in users:
    total_expense+=item["Amount"]
print(total_expense)

