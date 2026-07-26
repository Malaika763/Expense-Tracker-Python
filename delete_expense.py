import sqlite3
def delete_expense():
    # Connect to the database
    connection = sqlite3.connect("expense.db")

    # Create a cursor
    cursor = connection.cursor()

    print("====== Delete Expense ======")
    # Ask the user for the expense ID
    try:
        expense_id= int(input("Enter Expense ID to delete: "))
    except ValueError:
        print("\nInvalid ID! Please enter a whole number.")
        connection.close()
        return

    # Delete the expense
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    # Save changes
    connection.commit()

    # Check whether any row was deleted
    if cursor.rowcount == 0:
        print("\n No expense found with that ID")
    else:
        print("\nExpense deleted successfully! ")

    # Close the connection
    connection.close()

if __name__ == "__main__": delete_expense()