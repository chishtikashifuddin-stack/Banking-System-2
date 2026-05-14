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
            if record["PHONENUMBER"] == f"+91{phone}":
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
        
        account = {
            "ACC NO": acc,
            "NAME": name,
            "PHONENUMBER": a,
            "BALANCE": 0,
            "DATE": time
        }
        
        data = json.dumps(account)
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
        if int(acc) == g["ACC NO"]:
            print(f"\nACCOUNT NUMBER OF HOLDER   : {g['ACC NO']}")
            print(f"ACCOUNT HOLDER NAME        : {g['NAME']}")
            print(f"ACCOUNT HOLDER PHONENUMBER : {g['PHONENUMBER']}")
            print(f"ACCOUNT HOLDER BALANCE     : {g['BALANCE']}\n")
            admin()
            
    print("ACCOUNT NOT FOUND")
    check()

fun()