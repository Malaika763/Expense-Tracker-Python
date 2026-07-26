import sqlite3
from datetime import datetime

def update_expense():

    # Connect to the database
    connection = sqlite3.connect("expense.db")

    # Create a cursor
    cursor = connection.cursor()

    print("====== Update Expense ======")

    # Ask the user for the expense ID
    try:
        expense_id = int(input("Enter Expense ID to update: "))
    except ValueError:
        print("\nInvalid ID! Please enter a whole number.")
        connection.close()
        return

    # Ask for the new amount
    try:
        amount =float(input("Enter the new amount: "))
    except ValueError:
        print("\nInvalid amount! Please enter numbers only.")
        connection.close()
        return

    category = input("Enter new category: ")
    description = input("Enter new description: ")
    date = input("Enter new date (DD-MM-YYYY): ")

    # Validate the date
    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("\nInvalid date format! Please use DD-MM-YYYY.")
        connection.close()
        return

    #Update the expense
    cursor.execute("""
    UPDATE expenses
    SET amount = ?,
        category = ?,
        description = ?, 
        date = ?
    WHERE id = ?
    """, (amount, category, description, date, expense_id))

    # Save changes
    connection.commit()

    # Check if any row was updated
    if cursor.rowcount == 0:
        print("\nNo expense found with that ID. ")
    else:
        print("\nExpense updated Successfully!")

    # Close the connection
    connection.close()
if __name__ == "__main__": update_expense()