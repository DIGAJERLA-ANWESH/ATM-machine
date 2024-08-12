import time


print("insert your card")
time.sleep(2)
print("Please wait.....")

time.sleep(5)


pin=12345
balance=10000

try:
    user_pin=int(((input("Enter the Pin : "))))
except ValueError:
    print("Invalid Pin, Please Enter the Valid Pin")
    exit()


if user_pin != pin:
    print("Incorrect Pin. Access denied")
    exit()

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")


    try:
        option=int(input("Please the Your Choice : "))
    except ValueError:
        print("Invalid Input, Please enter the valid Choice")
        continue

    if option==1:
        print(f"Your Current Balance is ${balance:.2f}")

    elif option==2:
            withdraw_amount=float(input("Enter the amount to withdraw : "))
            if withdraw_amount<=0:
                print("Invalid amount. It must be greater than zero.")
            elif withdraw_amount>balance:
                print("Insufficient funds.")
            else:
                balance-=withdraw_amount   
                print(f"${withdraw_amount:.2f} has been debited from your account.")
                print(f"Your updated balance is ${balance:.2f}")
    elif option==3:
        deposit_amount=float(input("Enter the amount to deposit : "))
        if deposit_amount<=0:
            print("Invalid amount. It must be greater than zero.")
        else:
            balance+=deposit_amount
            print(f"${deposit_amount:.2f} has been credited to your account.")
            print(f"Your updated balance is ${balance:.2f}")
    elif option==4:
        print("Thank you for using our ATM. Visit again!")
        break

    else:
        print("Invalid option. Please enter a option between 1 and 4.") 


