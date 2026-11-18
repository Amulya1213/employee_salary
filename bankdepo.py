name = input("Enter Customer Name: ")
balance = float(input("Enter Initial Balance: "))

deposit = float(input("Enter Deposit Amount: "))
balance = balance + deposit

withdraw = float(input("Enter Withdraw Amount: "))

if balance - withdraw >= 1000:
    balance = balance - withdraw
    print("Withdrawal Successful")
else:
    print("Minimum Balance of 1000 should be maintained")

print("\nCustomer Name:", name)
print("Updated Balance:", balance)
