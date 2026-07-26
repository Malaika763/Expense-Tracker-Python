import sqlite3
import csv

def export_csv():
    #Connect to the database
    connection = sqlite3.connect("expense.db")
    cursor = connection.cursor()

    #Get all expenses
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    #Create the CSV file
    with open("expense.csv", "w", newline="") as file:

        writer = csv.writer(file)

        #Write headings
        writer.writerow(["ID", "Amount", "Category", "Description", "Date"])

        #Write all records
        writer.writerows(expenses)
        print("\nExpenses exported successfully!")

    connection.close()

if __name__ == "__main__": export_csv()


