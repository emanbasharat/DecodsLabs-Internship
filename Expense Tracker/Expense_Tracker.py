total = 0

while True:
    expense = input("Enter your expense (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    expense = float(expense)
    total = total + expense

print("Total Spent:", total)
