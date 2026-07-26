import sqlite3
def budget_alert():

    connection = sqlite3.connect("expense.db")  #Connect to the database
    cursor = connection.cursor()

    print("====== Budget Alert ======")

    # Ask the user for the budget
    try:
        budget = float(input("Enter your monthly budget: "))  #Ask the user for their budget
    except ValueError:
        print("\nInvalid budget! Please enter numbers only.")
        connection.close()
        return 

    cursor.execute("SELECT SUM(amount) FROM expenses")  #Calculates the total spending

    total = cursor.fetchone()[0]  #Get result (one total only)

    if total is None:
        total = 0  #Handle the empty database

    if total > budget:  #Compare budget and spending
        print("\n Budget exceeded!")
        print("Budget:", budget)
        print("Spent:", total)
        print("Exceeded by:", total - budget)
    else:
        print("\n Budget is under control!")
        print("Budget:", budget)
        print("Spent:", total)
        print("Remaining:", budget - total)

    connection.close()

if __name__ == "__main__": budget_alert()






