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
    data4 = []
    R = "NO TRANSACTION"
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

        admin()

    print("ACCOUNT NOT FOUND")
    check() 
    
# THIS OPTION IS USE FOR USERS
def user():
    print("*-----------------------------------------------*")
    print("|         CLICK 1 FOR CREDIT MONEY              |")
    print("|         CLICK 2 FOR DEBIT MONEY               |")
    print("|         CLICK 3 FOR CHECK BANK DETAILS        |")
    print("|         CLICK 4 FOR CHECK PAYMENT STATEMENT   |")
    print("|         CLICK 5 FOR PAYMENT TRANSFER          |")
    print("|         CLICK 6 FOR EXIST                     |")
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
        print(" |    CHECK YOURE BANK DETAILS WITH ACCOUNT NUMBER    |")
        print("*-----------------------------------------------------*")
        detials()
    if a == "4":
        print("*-----------------------------------------------------------------*")
        print("|    CHECK YOURE BANK PAYMENT STATEMENT WITH ACCOUNT NUMBER       |")
        print("*-----------------------------------------------------------------*")
        statements()
    if a == "5":
        print("*-----------------------------------------------------*")
        print("|               WELCOME TO PAYEMENT TRANSACTION       |")
        print("|               ENTER THE ACCOUNT NUMBERS             |")
        print("*-----------------------------------------------------*")
        transaction()
        
    if a == "6":
        print("-----------------------------------------------")
        print("|         WELCOME BACK TO DASHBOARD           |")
        print("-----------------------------------------------")
        fun()
    
    else:
        print("PLEASE ENTER CORRECT OPTION")
    user()

# this function is use to credit account with using user account number to verify the user account then it will give 5 options to creadit amount.
def credit():
    data4 = []
    C = "CREDIT"
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
                        credit = "CREDIT"
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
                print(f"{num2}₹ CREDITED SUCCESSFULLY")
                print(f"NEW BALANCE : {total}₹")
                print("----------------------------------------")
                data2 = json.dumps(acc)
                os.popen(f'echo {data2} >> user_bank_DB.txt')
                os.popen(f"echo {data2} >> admin_bank_DB.txt")
                
                acc2 = {
                            "account": {
                                "ACC NO": g["account"]["ACC NO"],
                                "NAME": g["account"]["NAME"],
                                "PHONENUMBER": g["account"]["PHONENUMBER"],
                                "BALANCE": total,
                                "CREADIT" : C,
                                "DATE": str(time)
                            }
                        }
                        
                data3 = json.dumps(acc2)
                data4.append(data3)
                os.popen(f"echo {data4} >> user_history.txt")
                
                user()
                
            print("PLEASE ENTER CORRECT NUMBER\n")
            credit()
            
    print("ACCOUNT NOT FOUND")
    credit()

# this function is use to debit account with using user account number to verify the user account then it will give 5 options to debit amount.
def deb():
    data4 = []
    D = "DEBIT"
    num = input("ENTER YOUR ACCOUNT NUMBER : ")
    data = os.popen("type admin_bank_DB.txt").read()
    lines = data.splitlines()
    
    for line in reversed(lines):
        g = json.loads(line)
        if num == str(g["account"]["ACC NO"]):
            print("\n*------------------------------------*")
            print(f"{g['account']['NAME']} THIS USER FOUND")
            print("*------------------------------------*\n")
            
            amount = int(input(f"ENTER HOW MUCH MONEY YOU WANT DEBIT {g['account']['NAME']} : "))
            balance = int(g["account"]["BALANCE"])
            
            if amount > balance:
                print("\n*--------------------------------------------------------------*")
                print("|NOT ENOUGH BALANCE IN YOUR ACCOUNT PLEASE CHECK YOURE BALANCE |")
                print("*--------------------------------------------------------------*\n")
                user()

            total = balance - amount
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
            print(f"{amount}₹ DEBITED SUCCESSFULLY")
            print(f"NEW BALANCE : {total}₹")
            print("----------------------------------------")
            data2 = json.dumps(acc)
            os.popen(f'echo {data2} >> admin_bank_DB.txt')
            os.popen(f'echo {data2} >> user_bank_DB.txt')
            
            
            acc2 = {
                    "account": {
                        "ACC NO": g["account"]["ACC NO"],
                        "NAME": g["account"]["NAME"],
                        "PHONENUMBER": g["account"]["PHONENUMBER"],
                        "BALANCE": total,
                        "CREADIT" : D,
                        "DATE": str(time)
                    }
                }
                
            data3 = json.dumps(acc2)
            data4.append(data3)
            os.popen(f"echo {data4} >> user_history.txt")
            user()

    print("\nACCOUNT NOT FOUND\n")
    user()
    
def statements():
    acc = input("ENTER YOUR ACCOUNT NUMBER : ")
    data = os.popen("type user_history.txt").read()
    data1 = data.splitlines()

    if len(acc) <= 7:
        print("PLEASE ENTER CORRECT ACCOUNT NUMBER")
        print("-----------------------------------")
        statements()
        
    for line in data1:
        if acc not in line:
            print("*---------------------------------------------------------------------------------------*")
            print("|THIS ACCOUNT IS NOT HAVE ANY TRANSACTION HISTORY PLEASE CREDIT ACCOUNT IN YOURE ACCOUNT|")
            print("*---------------------------------------------------------------------------------------*")
            user()
        if acc in line:
            line1, line2, line3, line4, line5, line6 = line.split(",")
            name, num = line2.split(":")
            bal, num2 = line4.split(":")
            cre, num3 = line5.split(":")
            date, num4, num5, num6 = line6.split(":")
            num7 = num6.replace("}", "")
            num8 = num7.replace("]", "")
            print(f"\nACCOUNT HOLDER BALANCE : {num2} : {num3}")
            print(f"TIME OF TRANSACTIONS : {num4}:{num5}:{num8}\n")
            print("\n*-------------------------------------------------*")
            print(f"|THIS IS YOUR BANK HISTORY {num}|")
            print("*-------------------------------------------------*\n")

    user()
    
def details():    
    acc = input("ENTER YOUR ACCOUNT NUMBER : ")

    if len(acc) <= 7:
        print("PLEASE ENTER CORRECT ACCOUNT NUMBER")
        print("-----------------------------------")
        details()

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
    
def transaction():
    data4 = []
    data5 = []
    C = "CREDIT"
    D = "DEBIT"
    num = input("ENTER YOUR ACCOUNT NUMBER : ")
    data = os.popen("type admin_bank_DB.txt").read()
    data1 = data.splitlines()
    for line in reversed(data1):
        g = json.loads(line)
# SENDER ACCOUNT FOUND
        if num == str(g["account"]["ACC NO"]):
            print("\n*------------------------------------*")
            print(f"{g['account']['NAME']} THIS USER FOUND")
            print("*------------------------------------*\n")
            num2 = input("ENTER ACCOUNT NUMBER OF RECEIVER : ")
            
# FIND RECEIVER
            for line2 in reversed(data1):
                g1 = json.loads(line2)
                if num2 == str(g1["account"]["ACC NO"]):
                    
                    print("\n*---------------------------------------*")
                    print(f"|{g1['account']['NAME']} THIS RECEIVER FOUND|")
                    print("*-----------------------------------------*\n")
                    
                    num3 = input(f"ENTER HOW MUCH MONEY YOU WANT SENT TO {g1['account']['NAME']} : ")

                    balance = int(g["account"]["BALANCE"])

                    if int(num3) > balance:
                        print("\n*--------------------------------------------------------------*")
                        print("|NOT ENOUGH BALANCE IN YOUR ACCOUNT PLEASE CHECK YOUR BALANCE |")
                        print("*--------------------------------------------------------------*\n")
                        user()

                    total = balance - int(num3)
                    total1 = int(g1["account"]["BALANCE"]) + int(num3)

                    time = datetime.datetime.now()
                  
# SENDER SIDE DATA
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
                    print(f"{num3}₹ MONEY TRANSFER SUCCESSFULLY")
                    print(f"NEW BALANCE : {total}₹")
                    print("----------------------------------------")

                    msg = (
                        f"HEY {g1['account']['NAME']} YOU RECEIVED A PAYMENT OF "
                        f"{num3}₹ IN YOUR VERSATILE BANK ACCOUNT, "
                        f"FROM {g['account']['NAME']} AND YOUR TOTAL BALANCE IS {total1}"
                    )

                    pywhatkit.sendwhatmsg_instantly(
                        g1["account"]["PHONENUMBER"],
                        msg
                    )

                    data2 = json.dumps(acc)

                    os.popen(f'echo {data2} >> user_bank_DB.txt')
                    os.popen(f'echo {data2} >> admin_bank_DB.txt')

# SENDER HISTORY
                    acc2 = {
                        "account": {
                            "ACC NO": g["account"]["ACC NO"],
                            "NAME": g["account"]["NAME"],
                            "PHONENUMBER": g["account"]["PHONENUMBER"],
                            "BALANCE": total,
                            "DEBIT": D,
                            "DATE": str(time)
                        }
                    }
                    
                    data3 = json.dumps(acc2)
                    data4.append(data3)
                    os.popen(f'echo {data3} >> user_history.txt')
                    
                    acc3 = {
                        "account": {
                            "ACC NO": g["account"]["ACC NO"],
                            "NAME": g["account"]["NAME"],
                            "PHONENUMBER": g["account"]["PHONENUMBER"],
                            "BALANCE": total,
                            "DEBIT": D,
                            "MONEY TRANSFER": num2,
                            "TRANSFER TO": g1["account"]["NAME"],
                            "DATE": str(time)
                        }
                    }
                    data6 = json.dumps(acc3)
                    os.popen(f'echo {data6} >> transfer_history.txt')
                    
# RECEIVER SIDE DATA

                    acc4 = {
                        "account": {
                            "ACC NO": g1["account"]["ACC NO"],
                            "NAME": g1["account"]["NAME"],
                            "PHONENUMBER": g1["account"]["PHONENUMBER"],
                            "BALANCE": total1,
                            "DATE": str(time)
                        }
                    }

                    data7 = json.dumps(acc4)

                    os.popen(f'echo {data7} >> user_bank_DB.txt')
                    os.popen(f'echo {data7} >> admin_bank_DB.txt')

                    acc5 = {
                        "account": {
                            "ACC NO": g1["account"]["ACC NO"],
                            "NAME": g1["account"]["NAME"],
                            "PHONENUMBER": g1["account"]["PHONENUMBER"],
                            "BALANCE": total1,
                            "CREDIT": C,
                            "DATE": str(time)
                        }
                    }
                    
                    data8 = json.dumps(acc5)
                    data5.append(data8)
                    os.popen(f'echo {data8} >> user_history.txt')
                    
                    acc6 = {
                        "account": {
                            "ACC NO": g1["account"]["ACC NO"],
                            "NAME": g1["account"]["NAME"],
                            "PHONENUMBER": g1["account"]["PHONENUMBER"],
                            "BALANCE": total1,
                            "CREDIT": C,
                            "MONEY TRANSFER": num,
                            "TRANSFER FROM": g["account"]["NAME"],
                            "DATE": str(time)
                        }
                    }
                    data9 = json.dumps(acc6)
                    os.popen(f'echo {data9} >> transfer_history.txt')
                    user()
                    
                    
            print("PLEASE ENTER CORRECT RECEIVER ACCOUNT NUMBER\n")
            transaction()
            user()

    print("ACCOUNT NOT FOUND")
    transaction()
    
fun()