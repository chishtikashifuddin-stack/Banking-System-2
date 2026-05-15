import random 
import os
import pywhatkit
import datetime
import json
print("*------------------------------------------*")
print("|        WELCOME TO VERSATILE BANK         |")
print("*------------------------------------------*\n")


def fun():
    print("*-------------------*")
    print("|     ADMIN (1)     |")
    print("|     USER  (2)     |")
    print("*-------------------*\n")    
    
    a = input("CHOICE THE OPTION : ")
    if a == "1":
        print("\n*-----------------------------------------*")
        print("|        WELCOME TO VERSATILE BANK         |")
        print("| HERE ARE THE OPTION WHAT YOU WANT TO DO  |")
        print("*-----------------------------------------*\n")
        admin()

    if a == "2":
        print("\n*-----------------------------------------*")
        print("|    WELCOME USER TO VERSATILE BANK       |")
        print("| HERE ARE THE OPTION WHAT YOU WANT TO DO |")
        print("*-----------------------------------------*\n")
        user()
    else:
        print("\n*---------------------------------------*")
        print("|    PLEASE CHOICE THE CORRECT OPTION   |")
        print("*---------------------------------------*")
    fun()
    

#this function is use for option are you admin or user
def admin():
    print("*---------------------------------------------------*")
    print("|         CLICK 1 FOR CREATE A ACCOUNT              |")
    print("|         CLICK 2 FOR CHECK ACCOUNT DETAILS         |")
    print("|         CLICK 3 FOR EXIST                         |")
    print("*---------------------------------------------------*")
    a = input("CHOICE OPTIONS :- ")
    if a == "1":
        print("------------------------------\n")
        cre()
    if a == "2":
        print("------------------------------\n")
        check()
    if a == "3":
        print("*------------------------------------*")
        print("|    WELCOME BACK TO DASHBOARD       |")
        print("*------------------------------------*")
        fun()
        
    else:
        print("PLEASE CHOICE FROM OPTIONS ")
    admin()
    
def cre():
    name = input("ENTER YOUR NAME : ")
    phone = input("ENTER YOUR PHONENUMBER : ")
    r = os.popen("type admin_bank_DB.txt").read()
    lines = r.splitlines()
    for line in lines:
        if line != "":
            record = json.loads(line)
            if record["account"]["PHONENUMBER"] == f"+91{phone}":
                print("THIS NUMBER IS ALREADY EXIST...!")
                print("--------------------------------\n")
                cre()
                
    if len(name) <= 7 or name == "":
        print("PLEASE ENTER FULL NAME")
        print("-----------------------\n")
        cre()
    if name.isdigit():
        print("---------------------------------------------------")
        print("|PLEASE ENTER ALPHABET IN NAME DIGIT IS NOT ALLOW |")
        print("---------------------------------------------------\n")
        cre()
        
    if phone.isdigit() and len(phone) == 10:
        a = f"+91{phone}"
        acc = random.randint(1000000,99999999)
        time = str(datetime.datetime.now())
        msg = f"THANK YOU {name} YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY IN VERSATILE BANK THIS IS YOUR ACCOUNT NUMBER : {acc}"
        pywhatkit.sendwhatmsg_instantly(a, msg)
        
        acc = { "account" : {
            "ACC NO": acc,
            "NAME": name,
            "PHONENUMBER": a,
            "BALANCE": 0,
            "DATE": time 
            }
        }
        
        data = json.dumps(acc)
        os.popen(f'echo {data} >> admin_bank_DB.txt')
        print("YOUR ACCOUNT IS CREATED!")
        print("------------------------------\n")
        admin()
    else:
        print("PLEASE ENTER CORRECT NUMBER!")
        print("-----------------------------\n")
        cre()


def check():
    acc = input("ENTER YOUR ACCOUNT NUMBER : ")
    if len(acc) <= 7:
        print("PLEASE ENTER CORRECT ACCOUNT NUMBER")
        print("-----------------------------------")
        check()
        
    data = os.popen("type admin_bank_DB.txt").read()
    data1 = data.splitlines()
    for line in data1:
        g = json.loads(line)
        if int(acc) == g["account"]["ACC NO"]:
            os.popen("type admin_bank_DB.txt").read()
            print("---------------------------------------------------------")
            print(f"\nACCOUNT NUMBER OF HOLDER   : {g['account']['ACC NO']}")
            print(f"ACCOUNT HOLDER NAME        : {g['account']['NAME']}")
            print(f"ACCOUNT HOLDER PHONENUMBER : {g['account']['PHONENUMBER']}")
            print(f"ACCOUNT HOLDER BALANCE     : {g['account']['BALANCE']}")
            print(f"TIME OF TRANSACTIONS : {g['account']['DATE']}\n")
            print("---------------------------------------------------------")
    admin()
    
    print("ACCOUNT NOT FOUND")
    check()
    
# THIS OPTION IS USE FOR USERS
def user():
    print("*-----------------------------------------------*")
    print("|         CLICK 1 FOR CREDIT MONEY              |")
    print("|         CLICK 2 FOR DEBIT MONEY               |")
    print("|         CLICK 3 FOR CHECK PAYMENT STATEMENT   |")
    print("|         CLICK 4 FOR EXIST                     |")
    print("*-----------------------------------------------*")

    a = input("ENTER THE CORRECT OPTION : ")
    if a == "1":
        print("*------------------------------------*")
        print(" |    WELCOME TO CREDIT OPTION        |")
        print("*-------------------------------------*")
        credit()
    if a == "2":
        print("*------------------------------------*")
        print(" |    WELCOME TO DEBIT OPTION         |")
        print("*-------------------------------------*")
        deb()
    if a == "3":
        print("*-----------------------------------------------------*")
        print(" |    CHECK YOURE BANK STATEMENT WITH ACCOUNT NUMBER  |")
        print("*-----------------------------------------------------*")
        detials()
    if a == "4":
        print("*------------------------------------*")
        print("|    WELCOME BACK TO DASHBOARD       |")
        print("*------------------------------------*")
        fun()
    else:
        print("PLEASE ENTER CORRECT OPTION")
    user()

# this function is use to credit account with using user account number to verify the user account then it will give 5 options to creadit amount.
def credit():
    num = input("ENTER YOUR ACCOUNT NUMBER : ")
    data = os.popen("type admin_bank_DB.txt").read()
    data1 = data.splitlines()
    for line in data1:
        g = json.loads(line)
        if num == str(g["account"]["ACC NO"]):
            print("\n*------------------------------------*")
            print(f"{g["account"]["NAME"]} THIS USER FOUND")
            print("*------------------------------------*\n")
            num2 = input(f"ENTER HOW MUCH MONEY YOU WANT CREDIT {g["account"]["NAME"]} : ")
            
            if num2.isdigit(): 
                data = os.popen("type admin_bank_DB.txt").read()
                data1 = data.splitlines()
                for line in data1:
                    g = json.loads(line)
                    if num == str(g["account"]["ACC NO"]):
                        total = int(g["account"]["BALANCE"]) + int(num2)                
                        time = datetime.datetime.now()
                        acc = {
                            "account": {
                                "ACC NO": g["account"]["ACC NO"],
                                "NAME": g["account"]["NAME"],
                                "PHONENUMBER": g["account"]["PHONENUMBER"],
                                "BALANCE": total,
                                "DATE": str(time)
                            }
                        }

                print("----------------------------------------")
                print(f"HEY {g['account']['NAME']}")
                print(f"{num2}₹ CREDITED SUCCESSFULLY")
                print(f"NEW BALANCE : {total}₹")
                print("----------------------------------------")
                data2 = json.dumps(acc)
                os.popen(f'echo {data2} >> user_bank_DB.txt')
                os.popen(f"echo {data2} >> admin_bank_DB.txt")
                user()

            print("PLEASE ENTER CORRECT NUMBER\n")
            credit()
            
    print("ACCOUNT NOT FOUND")
    credit()

# this function is use to debit account with using user account number to verify the user account then it will give 5 options to debit amount.
def deb():
    num = input("ENTER YOUR ACCOUNT NUMBER : ")
    data = os.popen("type admin_bank_DB.txt").read()
    data1 = data.splitlines()
    for line in data1:
        g = json.loads(line)
        if num == str(g["account"]["ACC NO"]):
            print("\n*------------------------------------*")
            print(f"{g["account"]["NAME"]} THIS USER FOUND")
            print("*------------------------------------*\n")

            num2 = input(f"ENTER HOW MUCH MONEY YOU WANT DEBIT {g["account"]["NAME"]} : ")
            if num2 > str(g["account"]["BALANCE"]):
                print("\n-------------------------------------------------------------------")
                print("YOURE ACCOUNT DONT HAVE HAS MUCH MONEY PLEASE CHECK YOURE BALANCE !")
                print("-------------------------------------------------------------------\n")
                user()
            if num2.isdigit():
                data = os.popen("type admin_bank_DB.txt").read()
                data1 = data.splitlines()
                for line in data1:
                    g = json.loads(line)
                    if num == str(g["account"]["ACC NO"]):
                        g = json.loads(line)
                        total = int(g["account"]["BALANCE"]) - int(num2)                
                        time = datetime.datetime.now()
                        acc = {
                            "account": {
                                "ACC NO": g["account"]["ACC NO"],
                                "NAME": g["account"]["NAME"],
                                "PHONENUMBER": g["account"]["PHONENUMBER"],
                                "BALANCE": total,
                                "DATE": str(time)
                            }
                        }

                print("----------------------------------------")
                print(f"HEY {g['account']['NAME']}")
                print(f"{num2}₹ CREDITED SUCCESSFULLY")
                print(f"NEW BALANCE : {total}₹")
                print("----------------------------------------")
                data2 = json.dumps(acc)
                os.popen(f'echo {data2} >> user_bank_DB.txt')
                os.popen(f"echo {data2} >> admin_bank_DB.txt")
                user()
                
            print("PLEASE ENTER CORRECT DIGIT")
            deb()
    print("ACCOUNT NOT FOUND")
    deb()
    

def details():    
    acc = input("ENTER YOUR ACCOUNT NUMBER : ")

    if len(acc) <= 7:
        print("PLEASE ENTER CORRECT ACCOUNT NUMBER")
        print("-----------------------------------")
        detials()

    data = os.popen("type admin_bank_DB.txt").read()
    data1 = data.splitlines()

    latest_acc = ""
    latest_name = ""
    latest_phone = ""
    latest_balance = ""
    latest_date = ""
    
    for line in data1:
        if line != "":
            g = json.loads(line)
            if int(acc) == g["account"]["ACC NO"]:
                latest_acc = g["account"]["ACC NO"]
                latest_name = g["account"]["NAME"]
                latest_phone = g["account"]["PHONENUMBER"]
                latest_balance = g["account"]["BALANCE"]
                latest_date = g["account"]["DATE"]

    if latest_acc != "":
        print("\n*-------------------------------------------------*")
        print(f"| THIS IS YOUR BANK DETAILS {latest_name} |")
        print("*-------------------------------------------------*\n")
        print(f"ACCOUNT NUMBER      : {latest_acc}")
        print(f"ACCOUNT HOLDER NAME : {latest_name}")
        print(f"PHONE NUMBER        : {latest_phone}")
        print(f"UPDATED BALANCE     : {latest_balance}₹")
        print(f"LAST TRANSACTION    : {latest_date}")
        print("---------------------------------------------------\n")

        user()

    print("ACCOUNT NOT FOUND")
    details()
    
    print("ACCOUNT NOT FOUND")
    detials()
fun()