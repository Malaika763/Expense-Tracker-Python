import sqlite3
def monthly_report():

    # Connect to the database
    connection = sqlite3.connect("expense.db")
    cursor = connection.cursor()

    month = input("Enter month and year (MM-YYYY): ")

    # Execute the query
    cursor.execute(
        "SELECT * FROM expenses WHERE date LIKE ?",
        ("%-" + month,)
    )

    expenses = cursor.fetchall()
    # Create the total variable
    total = 0
    # Display the report
    if expenses:
        print("\n====== Monthly Report ======\n")
        for expense in expenses:
            print("ID:", expense[0])
            print("Amount:", expense[1])
            print("Category:", expense[2])
            print("Description:", expense[3])
            print("Date:", expense[4])
            print("------------------")
            total += expense[1]
            print("Total Expenses:", total)
    else:
        print("No expenses found for this month. ")

    # Close the connection
    connection.close()

if __name__ == "__main__": monthly_report()