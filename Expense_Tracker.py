#======Expense Tracker======

#List to store All Expenses
expense_List = []


#-----FUNCTION DEFINATIONS-----

#Function to Add a New Expense
def add_expense():
    expense_name = input("Enter a new Expense Item: ")
    date = input("Enter Date (MM DD, YYYY): ")
    category = input("Enter Category: ")
    expense_amount = float(input("Enter amount: ")) 
    description = input("Enter description(optional): ")
    expense_List.append({"Expense": expense_name, 
                         "Date": date, 
                         "Category": category, 
                         "Amount": expense_amount,
                         "Description": description})
    print()
    print("New Expense Added Successfully!!")
    print()


#Function to View All Expenses
def view_expenses():
    print("Your All Expenses: ")
    if len(expense_List) == 0:
        print("No Expenses Added yet!! ")
    else: 
        for index, expense in enumerate(expense_List, 1):
            print("No. - NAME - AMOUNT - DATE - CATEGORY - DESCRIPTION ")
            print(f"{index}. {expense['Expense']} - {expense['Amount']} - {expense['Date']} - {expense['Category']} - {expense['Description']}")
            print()
    print()


#Function to Update an Expense
def update_expense():
    index = int(input("Enter the expense number you want to update: ")) - 1

    if 0 <= index < len(expense_List):
        expense = expense_List[index]

        expense["Expense"] = input("Enter new expense name: ")
        expense["Date"] = input("Enter new date (MM DD, YYYY): ")
        expense["Category"] = input("Enter new category: ")
        expense["Amount"] = float(input("Enter new amount: "))
        expense["Description"] = input("Enter new description: ")
        print()
        print("Expense updated successfully!!")
        print()
    else:
        print("Invalid expense number!")
        print()


#Function to view Total Spending
def view_total_spending():
    total_spending = 0
    for expense in expense_List:
        total_spending = total_spending + expense['Amount']
    print(f"Total Spending:  {total_spending}")
    print()
    print("Expenses added successfully!!")
    print()


#Function to Delete an Expense
def remove_expense():
    if len(expense_List) == 0:
        print("No Expenses to Remove!")
    else:
        index = int(input("Enter the expense number you want to remove: ")) - 1
        if 0 <= index < len(expense_List):
            removed_expense = expense_List.pop(index)
            print(f"Expense Removed: {removed_expense['Expense']}")
        else:
            print("Invalid expense number!")
    print()


#Function to display a menu
def menu():
    while(True):
        print("----Main Menu----")
        print("1. Add a New Expense")
        print("2. View all Expenses")
        print("3. Update an Expense")
        print("4. View Total Spending")
        print("5. Remove an Expense")
        print("6. Exit")
        print()

        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            add_expense()
        elif choice =="2":
            view_expenses()
        elif choice == "3":
            update_expense()
        elif choice =="4":
            view_total_spending()
        elif choice =="5":
            remove_expense()
        elif choice =="6":
            print("Exiting the application....")
            print()
            exit()
        else:
            print("Invalid choice! Try again!!")
            print()


menu()
