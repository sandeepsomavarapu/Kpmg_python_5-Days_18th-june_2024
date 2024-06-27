from random import randint
import mysql.connector

from datetime import date
import re

def validate_name(a_string):
    flag=-1
 
    while flag<0:
         matches = re.findall(r'[A-Z][a-zA-Z]{1,8}', a_string) #r'[A-Z][a-z][A-Z]{1,8}'
         if not matches:
             a_string = input("Invalid name. Please enter a name of length 10 consisting of only letters from the alphabet with the first letter capitalized.\n\n---------------:")
         else:
            return a_string
            flag=10
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
con = mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="kpmg")
cursor = con.cursor()
# cursor.execute("create table customer (fname varchar2(10) not null, lname varchar2(10) not null, phone_num number(10) not null, bal number not null, acc_num number(10) unique)")
 
#cursor.execute("create table txn (acc_num number(10), dt date not null, amount BINARY_FLOAT not null, typeoftrans varchar2(1),CONSTRAINT fk_customer_ACC_NUM FOREIGN KEY (ACC_NUM) REFERENCES customer (ACC_NUM))") 
print("Customer and Transaction tables have been created.\n\n")
flag=-1
print("**********************Welcome to Imaginary Bank**********************\n\n\n")
choice = int(input("Please enter a number to select one of the following options:\n1. Create Account\n2. Show Balance\n3. Make a Deposit\n4. Make a Withdrawal\n5. Fund Transfer Within the Bank\n6. Print Transactions for an Account Number\n7. Exit\n")) 
while(flag<0):
    if choice == 1:
        print("\nCREATE ACCOUNT\n")
        sql_query = ("SELECT * FROM customer")
        cursor.execute(sql_query)
        result = cursor.fetchall()
 
        fname = input("Please enter your first name\n")
        fname = validate_name(fname)
 
        lname = input("Please enter your last name\n")
        lname = validate_name(lname)
 
        phone_num = input("Please enter your phone number\n")
 
        bal=500
        acc_num = random_with_N_digits(5)
        print("Account number has been initialized to ", acc_num)
 
        #if record already exists, change choice to 2 for login
 
        for res in result:
            if res[0]==fname and res[1]==lname:
                choice=2
 
 
        #if there is no existing record, insert a new one
 
 
        sql = ('insert into customer (fname, lname, phone_num, bal, acc_num) values (%s, %s, %s,%s,%s) ')
      
        cursor.execute(sql, [fname, lname, phone_num, bal, acc_num])
        con.commit()
        print("User has been registered!")
 
        choice = int(input("Please enter a number to select one of the following options:\n1. Create Account\n2. Show Balance\n3. Make a Deposit\n4. Make a Withdrawal\n5. Fund Transfer Within the Bank\n6. Print Transactions for an Account Number\n7. Exit\n")) 
 
    elif choice == 7:
        print("*** Exiting Imaginary Banking Application ***\n Thank you for your business. Goodbye!")
        flag=1  
    elif choice == 2:
        print("\nSHOW BALANCE\n")
        sql_query = "SELECT * FROM CUSTOMER"
        cursor.execute(sql_query)
        results = cursor.fetchall() 
        acc_num = int(input("Please enter your account number\n")) 
        found=-1 
        for res in results:
            if res[4] == acc_num:#res[column number]
                 print("Current account balance for ", res[0], " ", res[2], "is:  ", res[3])
                 found=1
        if found <0:
            print("Account number not found")
 
        choice = int(input("Please enter a number to select one of the following options:\n1. Create Account\n2. Show Balance\n3. Make a Deposit\n4. Make a Withdrawal\n5. Fund Transfer Within the Bank\n6. Print Transactions for an Account Number\n 7. Exit\n")) 
    elif choice == 3:
        print("\nMAKE A DEPOSIT\n")
 
        acc_num = int(input("Please enter your account number\n"))
        found=-1
 
        #Does this account number exist in our records?
        sql_query = "SELECT * FROM CUSTOMER"
        cursor.execute(sql_query)
        results = cursor.fetchall() 
        for res in results:
            if res[4] == acc_num: #if there's a match
                found=1
                dep_amt = int(input("Enter the amount to be deposited\n"))
                new_amt = res[3] + dep_amt
                sql_query = ("UPDATE CUSTOMER SET BAL=%s WHERE acc_num= %s")
                cursor.execute(sql_query,[new_amt, acc_num])
                con.commit()
                trans_query=("INSERT INTO TXN(ACC_NUM, DT, AMOUNT,typeoftrans) VALUES(%s, %s, %s, %s)") #insert row in txn
                cursor.execute(trans_query, [acc_num, date.today(), dep_amt, 'DEPOSIT'])
                con.commit()
                print("A deposit of amount $", dep_amt, "to account number ", acc_num, " has been made. Your current balance is: \n$", new_amt)
                choice = int(input("Please enter a number to select one of the following options:\n1. Create Account\n2. Show Balance\n3. Make a Deposit\n4. Make a Withdrawal\n5. Fund Transfer Within the Bank\n6. Print Transactions for an Account Number\n 7. Exit\n"))
        if found<0:
            print("Account number not found\n")
            choice = int(input("Please enter a number to select one of the following options:\n1. Create Account\n2. Show Balance\n3. Make a Deposit\n4. Make a Withdrawal\n5. Fund Transfer Within the Bank\n6. Print Transactions for an Account Number\n7. Exit\n"))
    elif choice == 4:
 
        print("\nMAKE A WITHDRAWAL\n")
        #Does this account number exist in our records?
        sql_query = "SELECT * FROM CUSTOMER"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        acc_num = int(input("Please enter your account number\n"))
        found=-1
        for res in results:
            if res[4] == acc_num: #if there's a match
                found=1
                with_amt = int(input("Enter the amount to be withdrawn\n"))
 
 
                new_amt = res[3] - with_amt
 
                sql_query = ("UPDATE CUSTOMER SET BAL=%s WHERE ACC_NUM= %s")
 
                cursor.execute(sql_query,[new_amt, acc_num])
 
                trans_query=("INSERT INTO TXN(ACC_NUM, DT, AMOUNT,typeoftrans) VALUES(%s, %s, %s, %s)") #insert row in txn
 
                con.commit()
 
                cursor.execute(trans_query, [acc_num, date.today(), with_amt, 'WITHDRAWL'])
 
                con.commit()
                print("A withdrawal of amount $", with_amt, "from account number ", acc_num, " has been made. Your current balance is: \n$", new_amt)
 
                choice = int(input("Please enter a number to select one of the following options:\n1. Create Account\n2. Show Balance\n3. Make a Deposit\n4. Make a Withdrawal\n5. Fund Transfer Within the Bank\n6. Print Transactions for an Account Number\n 7. Exit\n"))
 
        if found<0:
            print("Account number not found\n")
            choice = int(input("Please enter a number to select one of the following options:\n1. Create Account\n2. Show Balance\n3. Make a Deposit\n4. Make a Withdrawal\n5. Fund Transfer Within the Bank\n6. Print Transactions for an Account Number\n7. Exit\n"))
 
    elif choice==5:
        print("\nFUND TRANSFER\n")
        sql_query = "SELECT * FROM CUSTOMER"
        cursor.execute(sql_query)
        results = cursor.fetchall()
 
 
        acc1 = int(input("Enter your account number\n"))
        acc2 = int(input("Enter the accout number you wish to transfer money to\n"))
        amt = int(input("Enter the transaction amount"))
 
        a1cnt=0
        a2cnt=0
        acc1_bal=0
        acc2_bal=0
 
 
        for res in results:
            if res[4]==acc1:
                    a1cnt=1
                    acc1_bal=res[3]
 
 
            for res in results:
                if res[4]==acc2:
                    a2cnt=1
                    acc2_bal = res[3]
 
            if a1cnt==1 and a2cnt==1: #if both account numbers are present
                #deduct amt from bal of acc1
                acc1_bal = acc1_bal-amt
                sql_query = "UPDATE CUSTOMER SET BAL= %s WHERE ACC_NUM = %s"
                cursor.execute(sql_query,[acc1_bal, acc1])
                con.commit()
 
                #add amt to bal of acc2
                acc2_bal = acc2_bal+amt
                cursor.execute(sql_query,[acc2_bal, acc2])
                con.commit()
 
                #enter a debit record in txn for acc1
                trans_query="INSERT INTO TXN(ACC_NUM, DT, AMOUNT,typeoftrans) VALUES(%s, %s,%s, %s)"
                cursor.execute(trans_query, [acc1, date.today(), amt, 'FUNDTRANSFER'])
                con.commit()
                #enter a credit record in txn for acc2
                cursor.execute(trans_query, [acc2, date.today(), amt, 'CREDIT'])
                con.commit()
                print("\n\n\nTransfer is complete. $", amt, "has been transferred from account number ", acc1, " to account number ", acc2)
                choice = int(input("Please enter a number to select one of the following options:\n1. Create Account\n2. Show Balance\n3. Make a Deposit\n4. Make a Withdrawal\n5. Fund Transfer Within the Bank\n6. Print Transactions for an Account Number\n 7. Exit\n"))
 
        if a1cnt!=1 or a2cnt!=1:
                print("One of the two account numbers provided does not exist in our system. Please try again.\n")
                choice = int(input("Please enter a number to select one of the following options:\n1. Create Account\n2. Show Balance\n3. Make a Deposit\n4. Make a Withdrawal\n5. Fund Transfer Within the Bank\n6. Print Transactions for an Account Number\n7. Exit\n"))
 
    elif choice == 6:
        print("\nPRINT TRANSACTIONS\n")
        acc_num = int(input("Please enter your account number\n"))
 
        #Does this account number exist in our records?
        sql_query = "SELECT * FROM CUSTOMER"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        found=-1
 
        for res in results:
            if res[4] == acc_num: #if there's a match
                found=1
                search_query= "SELECT * FROM TXN WHERE ACC_NUM = %s"
                cursor.execute(search_query,[acc_num])
                trans = cursor.fetchall()
                for tran in trans:
                    print(tran)
                #select all records from transaction table matching the account number
                choice = int(input("Please enter a number to select one of the following options:\n1. Create Account\n2. Show Balance\n3. Make a Deposit\n4. Make a Withdrawal\n5. Fund Transfer Within the Bank\n6. Print Transactions for an Account Number\n 7. Exit\n"))
 
        if found<0:
                print("This account number was not found in our system. Please try again.\n")
                choice = int(input("Please enter a number to select one of the following options:\n1. Create Account\n2. Show Balance\n3. Make a Deposit\n4. Make a Withdrawal\n5. Fund Transfer Within the Bank\n6. Print Transactions for an Account Number\n7. Exit\n"))


# create table customer(fname varchar(20),lname varchar(20),phone_num int,bal int,acc_num int);
# create table txn(acc_num int,dt date,amount int,typeoftrans varchar(20));