import sqlite3
def view_expenses():
    # Connect to the Database
    connection = sqlite3.connect("expense.db")

    # Create a cursor
    cursor = connection.cursor()

    # Read all expenses
    cursor.execute("SELECT * FROM expenses")

    # Store all rows
    expenses = cursor.fetchall()

    print("======= All Expenses =======")

    # Display expenses
    for expense in expenses:
        print("ID:", expense[0])
        print("Amount:", expense[1])
        print("Category:", expense[2])
        print("Description:", expense[3])
        print("Date:", expense[4])
    print("---------------------\n")

    # Close the connection
    connection.close()

if __name__ == "__main__": view_expenses()

