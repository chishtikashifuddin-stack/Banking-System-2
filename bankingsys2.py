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

fun()