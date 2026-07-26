import sqlite3
import matplotlib.pyplot as plt
def expense_chart():
    connection = sqlite3.connect("expense.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT category, SUM(amount) 
        FROM expenses
        GROUP BY category
    """)
    results = cursor.fetchall()  #Fetch the results

    categories = []  #Create two lists one for category and the other for total
    totals = []

    for result in results:
        categories.append(result[0])  #Fill the lists
        totals.append(result[1])

    plt.bar(categories, totals)  #Draw the chart

    plt.title("Expenses by Category")  #Add labels
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.show()  #Display the chart

    connection.close()  #Close the database

if __name__ == "__main__": expense_chart()  #Run the function
