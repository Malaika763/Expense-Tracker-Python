import sqlite3
def search_expense():
    # Connect to the Database
    connection = sqlite3.connect("expense.db")
    cursor = connection.cursor()

    # Ask the user
    print("====== Search Expense ======")
    category = input("Enter category to search: ")

    cursor.execute(
        "SELECT * FROM expenses WHERE category = ?", (category, )
    )

    # Get the results
    expenses = cursor.fetchall()

    # Display the results
    if expenses:
        print("\n====== Search Results =======\n")
        for expense in expenses:
            print("ID:", expense[0])
            print("Amount:", expense[1])
            print("Category:", expense[2])
            print("Description:", expense[3])
            print("Date:", expense[4])
            print("------------------------")
    else:
        print("No expenses found.")
    connection.close()

if __name__ == "__main__": search_expense()
    