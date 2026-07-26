import sqlite3
from datetime import datetime

def add_expense():
    # Connect to the database
    connection = sqlite3.connect("expense.db")

    # Create a cursor
    cursor = connection.cursor()

    print("====== Add Expense ======")

    # Get expense details from the user
    try:
        amount= float(input("Enter expense amount: "))
    except ValueError:
        print("\nInvalid amount! Please enter numbers only.")
        connection.close()
        return

    category= input("Enter category: ").strip()
    if category == "":
        print("\nCategory cannot be empty.")
        connection.close()
        return

    description= input("Enter description: ").strip()
    if description == "":
        print("\nDescription cannot be empty.")
        connection.close()
        return

    date= input("Enter date (DD-MM-YYYY): ")

    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("\nInvalid date format! Please use DD-MM-YYYY.")
        connection.close()
        return

    # Insert the expense into the database
    cursor.execute("""
    INSERT INTO expenses (amount, category, description, date)
    VALUES(?, ?, ?, ?)
    """, (amount, category, description, date))

    # Save changes
    connection.commit()

    print("\nExpense Added Successfully!")

    # Close the database
    connection.close()

if __name__ == "__main__": add_expense()
