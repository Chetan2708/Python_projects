
import os 

print("**********************************************************************************")
print("\t\t\tWelcome User!\t\t\t")
print("**********************************************************************************")
print(" Choose your language from the following  1 , 2 or 3 :")
print("1. English")
print("2. Hindi")
print("3. Other")
bank_pin = 2708
bank_amount = 10000
newbalance = bank_amount
lang_ch = int(input(" Choose language: \n "))
count = 1
while count:
    os.system("cls")
    if lang_ch == 1:
        print("CHOOSE YOUR OPTIONS")
        print("1.Balance enquiry")
        print("2.Cash withdrawl ")
        print("3.Pin change")
        print("4.Deposit cash")
        print("5.Mini statement")
        print("6.Exit")
        x = int(input(" Choose your option: "))
        if x == 1:
            print(" Bank balance ")
            user_pin = int(input("Please enter your pin:"))
            if user_pin == bank_pin:
                print(f"The avaialable balance is{bank_amount} ")
            else:
                print(" Invalid pin")
            input("Press enter to continue...")
        elif x == 2:
            print("Withdraw cash ")
            user_pin = int(input("Enter your pin: "))
            if user_pin == bank_pin:
                user_amt = int(input("Please enter the amount you want to withdraw: "))
                if user_amt <= 0:
                    print("Invalid amount")
                if user_amt <= newbalance:
                    newbalance -= user_amt
                    print(f"Balance : {newbalance}")
                else:
                    print(" Not enough balance")
            else:
                print("Invalid pin ")
            input("press enter to continue...")
        elif x == 3:
            print(" Change pin ")
            user_pin = int(input("Enter your pin: "))
            if user_pin== bank_pin:
                new_pin = int(input("Enter new pin: "))
                neww_pin = int(input("Confirm new pin: "))
                if neww_pin == new_pin:
                   bank_pin = new_pin
                   print("Pin changed successfully! %d" % bank_pin)
                else:
                    print("Both pins are different!")
            else:
                print("wrong pin")
            input("press enter to continue...")
        elif x==4:
            print("Add money to bank")
            user_pin = int(input("Enter your pin: "))
            if user_pin == bank_pin:
                user_amount = int(input("Enter the amount of money youwant to add: "))
                if user_amount <= 0:
                    print("Invalid amount")
                else:    
                    newbalance +=user_amount
                    print(f"Money added successfully to your account {newbalance}")
            else:
                print("wrong pin")
            input("press enter to continue...")    
        elif x == 5:
            print(" Check mini statement ")
            if newbalance >bank_amount:
                 print("The amount of new balance after credit:  %d" % newbalance)
            elif newbalance < bank_amount:
                    print("The amount of new balance after debit:  %d" % newbalance) 
            elif newbalance == bank_amount:
                    print("The amount of new balance is : %d" % newbalance)
            else:
                print("Wrong pin")        
            input("press enter to continue...")
        elif x == 6:
            count = 0 
            print(" Exited ")
        else:
            print(" You have chosen wrong option") 
            input("Press enter to continue...")
    elif lang_ch == 2:
        break
    elif lang_ch == 3:
       break
    else:
        print("You have no other options available")
        break
