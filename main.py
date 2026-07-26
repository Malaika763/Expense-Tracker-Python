#Importing all the function
from add_expense import add_expense
from view_expenses import view_expenses
from update_expense import update_expense
from delete_expense import delete_expense
from search_expense import search_expense
from monthly_report import monthly_report
from expense_chart import expense_chart
from budget_alert import budget_alert
from date_filter import date_filter
from export_csv import export_csv

def main():
    #Display the menu
    while True:

        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Search Expense")
        print("6. Monthly Report")
        print("7. Expense Chart")
        print("8. Budget Alert")
        print("9. Date Filter")
        print("10. Export Expenses to CSV")
        print("0. Exit")

        try:
            #Ask the user
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Choice! Please enter numbers only. ")
            continue

        #Call the correct function
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            update_expense()
        elif choice == 4:
            delete_expense()
        elif choice == 5:
            search_expense()
        elif choice == 6:
            monthly_report()
        elif choice == 7:
            expense_chart()
        elif choice == 8:
            budget_alert()
        elif choice == 9:
            date_filter()
        elif choice == 10:
            export_csv()
        elif choice == 0:
            print("\nThank you for using Expense Tracker!")
            break
        else:
            print("\nInvalid Choice! Please enter a number between 0 and 10. ")

if __name__ == "__main__": main()