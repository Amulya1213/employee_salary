name = input("Enter Customer Name: ")
balance = float(input("Enter Initial Balance: "))

deposit = float(input("Enter Deposit Amount: "))
balance = balance + deposit

withdraw = float(input("Enter Withdraw Amount: "))
balance = balance - withdraw

print("\nCustomer Name:", name)
print("Updated Balance:", balance)