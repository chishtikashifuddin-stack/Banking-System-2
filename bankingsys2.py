import random 
import os
import pywhatkit
import datetime
import json
print("*------------------------------------------*")
print("|        WELCOME TO VERSATILE BANK         |")
print("*------------------------------------------*\n")

#this function is use for option are you admin or user

def fun():
    print("*-------------------*")
    print("|     ADMIN (1)     |")
    print("|     USER  (2)     |")
    print("*-------------------*\n")    
    
    a = input("CHOICE THE OPTION : ")
    if a == "1":
        print("\n*-----------------------------------------*")
        print("|    WELCOME ADMIN TO VERSATILE BANK      |")
        print("| HERE ARE THE OPTION WHAT YOU WANT TO DO |")
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
    

def admin():
    print("*---------------------------------------------------*")
    print("|         CLICK 1 FOR CREATE A ACCOUNT              |")
    print("|         CLICK 2 FOR CHECK TOTAL ACCOUNT DETAILS   |")
    print("|         CLICK 3 FOR CHECK ACCOUNT DETAILS         |")
    print("|         CLICK 4 FOR EXIST                         |")
    print("*---------------------------------------------------*")
    a = input("CHOICE OPTIONS :- ")
    if a == "1":
        print("------------------------------\n")
        cre()
    if a == "2":
        print("------------------------------\n")
        total()
    if a == "3":
        print("------------------------------\n")
        check()
    if a == "4":
        print("------------------------------\n")
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
                print("----------------------------------\n")
                cre()
                
    if len(name) <= 7 or name == "":
        print("PLEASE ENTER FULL NAME")
        print("-----------------------\n")
        cre()
        
    if phone.isdigit():
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
            print(f"\nACCOUNT NUMBER OF HOLDER   : {g['account']['ACC NO']}")
            print(f"ACCOUNT HOLDER NAME        : {g['account']['NAME']}")
            print(f"ACCOUNT HOLDER PHONENUMBER : {g['account']['PHONENUMBER']}")
            print(f"ACCOUNT HOLDER BALANCE     : {g['account']['BALANCE']}\n")
            admin()
            
    print("ACCOUNT NOT FOUND")
    check()

def total():
    a = os.popen("type admin_bank_DB.txt").read()
    a1 = a.split("\n")
    total_accounts = 0
    for a2 in a1:
        if a2 != "":
            g = json.loads(a2)
            if "account" in g:
                total_accounts += 1
    print("*-------------------------------------------------------------*")
    print("|           THIS IS TOTAL ACCOUNT IN VERSATILE BANK          |")
    print("*-------------------------------------------------------------*\n")
    print(f"TOTAL ACCOUNT : {total_accounts}\n")
    admin()
    
# THIS OPTION IS USE FOR USERS
def user():
    print("*-----------------------------------------------*")
    print("|         CLICK 1 FOR CREDIT MONEY              |")
    print("|         CLICK 2 FOR DEBIT MONEY               |")
    print("|         CLICK 3 FOR CHECK DETAILS             |")
    print("|         CLICK 4 FOR CHECK PAYMENT STATEMENT   |")
    print("|         CLICK 5 FOR EXIST                     |")
    print("*-----------------------------------------------*")

    a = input("ENTER THE CORRECT OPTION : ")
    if a == "1":
        cre()
    if a == "2":
        deb()
    if a == "3":
        details()
    if a == "4":
        statement()
    if a == "5":
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

            print("----------------------------------------")
            print("|          CLICK 1 TO ADD 100₹         |")
            print("|          CLICK 2 TO ADD 200₹         |")
            print("|          CLICK 3 TO ADD 300₹         |")
            print("|          CLICK 4 TO ADD 500₹         |")
            print("|          CLICK 5 TO ADD 1000₹        |")
            print("----------------------------------------")

            num2 = input("CHOICE OPTION : ")
            old = int(g["account"]["BALANCE"])

            if num2 == "1":
                amount = 100
                new = old + amount
            if num2 == "2":
                amount = 200
                new = old + amount
            if num2 == "3":
                amount = 300
                new = old + amount
            if num2 == "4":
                amount = 500
                new = old + amount
            if num2 == "5":
                amount = 1000            
                new = old + amount
                
            time = datetime.datetime.now()
            acc = {
                "account": {
                    "ACC NO": g["account"]["ACC NO"],
                    "NAME": g["account"]["NAME"],
                    "PHONENUMBER": g["account"]["PHONENUMBER"],
                    "BALANCE": new,
                    "DATE": str(time)
                }
            }

            print("----------------------------------------")
            print(f"HEY {g['account']['NAME']}")
            print(f"{amount}₹ CREDITED SUCCESSFULLY")
            print(f"NEW BALANCE : {new}₹")
            print("----------------------------------------")
            data2 = json.dumps(acc)
            os.popen(f'echo {data2} >> user_bank_DB.txt')
            user()
            
    print("ACCOUNT NOT FOUND")
    credit()
    
fun()