import random 
import os
import pywhatkit
import datetime
print("*------------------------------------------*")
print("|        WELCOME TO VERSATILE BANK         |")
print("*------------------------------------------*\n")

def fun():
    print("*-------------------*")
    print("|     ADMIN (1)     |")
    print("|     USER  (2)     |")
    print("|     EXIST (3)     |")
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

    if a == "3":
        print("\n*---------------------------------------------*")
        print("|    THANK YOU VISITING TO VERSATILE BANK     |")
        print("*---------------------------------------------*\n")
        return
        
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
    fun()
    
def cre():
    name = input("ENTER YOUR NAME : ")
    phone = input("ENTER YOUR PHONENUMBER : ") 
    r = os.popen("type admin_bank_DB.txt").read()
    
    r = r.splitlines()
    for r1 in r:
        if phone in r1 or phone == "":
            print("THIS NUMBER IS ALREADY EXIST...!")
            print("----------------------------------\n")
            fun()
    if len(name)<=7 or name == "":
        print("PLEASE ENTER FULL NAME\n")
        print("-----------------------\n")
        cre()
        
    if phone.isdigit():
        a = f"+91{phone}"
        acc = random.randint(1000000,99999999)
        time = datetime.datetime.now()
        msg = f"THANK YOU {name} YOURE ACCOUNT HAS BEEN CREATED SUCESSFULLY IN VERSATILE BANK THIS IS YOURE ACCOUNT NUMBER : {acc}"
        pywhatkit.sendwhatmsg_instantly(a,msg)
        c = f"ACC NO:{acc},NAME:{name},PHONENUMBER:{a},BALANCE:0,DATE:{time}"
        json.dumps(c)
        d =os.popen (f"echo {c} >> admin_bank_DB.txt")
        print("YOUR ACCOUNT IS CREATED ! ")
        print("------------------------------\n")
        fun()
    else:
        print("PLEASE ENTER CORRECT NUMBER!\n")
        print("-----------------------------\n")
        cre()
fun()