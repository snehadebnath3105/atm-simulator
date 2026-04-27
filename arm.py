balance = 10000
transitions = []

def show_balance():
  print(f"current Balance {balance}")

def deposit():
  global balance
  amount = float(input("Enter your deposit balance :"))
  balance = balance + amount
  transitions.append(f"deposit amount {amount}")
  print("Amount added successfully")

def withdrawl():
  global balance
  amount = float(input("Enter your withdrawl amount :"))
  if amount > balance:
    print("Amount not sufficient")
  else:
    balance = balance - amount
    transitions.append(f"withdrawl amount {amount}")
    print("Withdrawl successfully , plase collect your cash")

def statement():

  print("\n📄 Transaction Statement:")
  if not transitions:
      print("No transactions yet.")
  else:
    for t in transitions:
      print("-",t)
 



while True:
  print("ATM")
  print("1.check balance")
  print("2.deposit")
  print("3.withdrawl")
  print("4.statement")
  print("5.exit")

  choice = int(input("Enter your choice :"))

  if choice == 1:
    show_balance()
  elif choice == 2:
    deposit()
  elif choice == 3:
    withdrawl()
  elif choice == 4:
    statement()
  elif choice == 5:
    print('Thankyou for using ATM')
    break
  else:
    print("Invalid statement , Please give a valid choice...")