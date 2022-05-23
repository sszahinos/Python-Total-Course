COMMISSION = 0.13

name = input("Worker's name: ")
sales = float(input("Sales amount: "))
worker_commision = sales * COMMISSION

print(f"{name}'s commission is {round(worker_commision, 2)}€,"
      f" having a total amount of {round(worker_commision + sales, 2)}€")
