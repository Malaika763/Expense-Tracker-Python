import sqlite3
def date_filter():

    connection = sqlite3.connect("expense.db")  #Connect to the database
    cursor = connection.cursor()

    date = input("Enter date (DD-MM-YYYY): ")  #Ask the user

    cursor.execute("""
        SELECT * 
        FROM expenses
        WHERE date = ?
    """, (date,))  #Execute the SQL Query

    expenses = cursor.fetchall()  #Fetch the results

    if expenses:  #Check if the records exist

        print(f"\n====== Expenses on {date} ======\n")  #Display them
        for expense in expenses:
            print("ID:", expense[0])
            print("Amount:", expense[1])
            print("Category:", expense[2])
            print("Description:", expense[3])
            print("Date:", expense[4])

        print("-----------------------")
    else:
        print("no expenses found for this date.")

    connection.close()

if __name__ == "__main__": date_filter()





