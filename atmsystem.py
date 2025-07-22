def check_balance(balance):
  print(f"Your balance is {balance}")

def withdraw_money(balance, amount):
  if amount > balance:
    print("Insufficient balance")
    return balance # Return current balance if withdrawal fails
  else:
    balance -= amount
    print(f"Withdrew {amount}. Your new balance is {balance}")
    return balance # Return updated balance

def deposit_money(balance, amount):
  balance = balance + amount
  print(f"Your new balance is {balance}")
  return balance # Return updated balance


def atm ():
  balance = 15000
  print ("Welcome to the ATM")
  while True:
    print("\nChoose option")
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Exit")

    choice = input ( "Enter your choice (1-4): ")
    if choice == "1":
      check_balance(balance)

    elif choice == "2":
      try:
        amount = float(input("Enter the amount to withdraw : Rupee "))
        balance = withdraw_money(balance, amount)
      except ValueError:
        print("Invalid input. Please enter a number.")

    elif choice == "3":
      try:
        amount = float(input("Enter the amount to deposit : Rupee "))
        balance = deposit_money(balance, amount)
      except ValueError:
        print("Invalid input. Please enter a number.")

    elif choice == "4":
      print("Exiting ATM. Thank you!")
      break  # This break is now inside the while loop

    else:
      print("Invalid choice. Please enter a number between 1 and 4.")

atm()
