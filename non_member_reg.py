import time
import random
import sys
import mysql.connector as connection
myconn = connection.connect(host = '127.0.0.1', user = 'root', passwd = 'Oluwadamilola99$$', database = 'corperative')
cursor = myconn.cursor()
def non_member():
    acct = input("""
    1. Login
    2. Create Account
    0. Back
    >> """)
    if acct == '1':
        time.sleep(1)
        non_member_login()
    elif acct == '2':
        time.sleep(1)
        non_member_create()
    elif acct == '0':
        time.sleep(1)
        from home import home
        home()
    else:
        print('Invalid Input')
        time.sleep(1)
        non_member()

def non_member_create():
    print("""
    Create New Account
    
    Enter your Information >>""")
    val = []
    info = ('first_name', 'middle_name', 'last_name', 'gender', 'age', 'phone_number', 'address', 'pin', 'amount_contributed', 'Refund', 'Loan', 'interest', 'email', 'passwd', 'user_ID')
    querry = 'insert into non_members(first_name, middle_name, last_name, gender, age, phone_number, address, pin, amount_contributed, Refund, Loan, interest, email, passwd, user_ID) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    for x in range(15):
        if info[x] == 'user_ID':
            bInfo = (f'NON/{random.randint(22001, 22999)}')
        elif info[x] == 'phone_number':
            bInfo = input('Enter Phone Number: ')
            while len(bInfo) != 11:
                print('Invalid Phone number; Phone number must be 11 digits')
                bInfo = input('Enter Phone Number: ')
        elif info[x] =='amount_contributed':
            bInfo = 0
        elif info[x] =='Refund':
            bInfo = 0
        elif info[x] =='Loan':
            bInfo = 0
        elif info[x] == 'interest':
            bInfo = 0
        else:
            bInfo = input(f'Enter your {info[x]}: ')
        val.append(bInfo)
    cursor.execute(querry, val)
    myconn.commit()
    time.sleep(1)
    print(f'Dear {val[0]} {val[1]}, Your User ID is {val[14]}')
    time.sleep(2)
    non_member_login()

def non_member_login():
    email = input("""
    LOGIN ACCOUNT
    
    Email >> """)
    passwrd = input("""
    Password >> """)
    val = (email, passwrd)
    querry = 'select * from non_members where email =%s and passwd =%s'
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        time.sleep(1)
        print('Processing > > >')
        time.sleep(2)
        print('LOG IN SUCCESSFUL')
        time.sleep(2)
        operation()
    else:
        print('Invalid Input')
        time.sleep(1)
        non_member_login()

def operation():
    user = input("""
    Cosmos Corperative Society
    1. Contribute Money
    2. Get Loan
    3. Pay Loan
    0. Log Out
    >> """)
    if user == '1':
        time.sleep(2)
        contributee()
    elif user == '2':
        time.sleep(2)
        borrow()
    elif user == '3':
        time.sleep(2)
        pay_loan()
    elif user == '0':
        time.sleep(2)
        print('Logout Successful')
        from home import home
        time.sleep(2)
        home()
    else:
        print('Invalid Input')
        time.sleep(1)
        operation()

def contributee():
    account = input('Account Number>> ')
    while len(account) != 10:
        print('Invalid Account number; Account number must be 10 digits')
        account = input('Account Number>> ')
    amount = int(input('Amount>> '))
    vall = (account, )
    querry2 = "SELECT * from treasure_account where account_number = %s"
    cursor.execute(querry2, vall) 
    result = cursor.fetchone()
    if result:
        time.sleep(2)
        print(f'Confirm Amount N{amount}, Beneficiary {result[1]}')
        time.sleep(2)
        user = input('Enter User ID>> ')
        val = (user, )
        querry = 'select * from non_members where user_ID =%s'
        cursor.execute(querry, val)
        result2 = cursor.fetchone()
        if result2:
            time.sleep(2)
            print('Processing')
            time.sleep(2)
            print('Transaction Successful')
            treB = (result[5] + amount)
            vallll = (treB, 1)
            querry = 'update treasure_account set balance =%s where ID =%s'
            cursor.execute(querry, vallll)
            myconn.commit()
            newBalance = (result[3] + amount)
            val = (newBalance, account)
            querry = 'update treasure_account set money_IN =%s where account_number =%s'
            cursor.execute(querry, val)
            myconn.commit()
            newestBalance = (result2[9] + amount)
            val = (newestBalance, user)
            querry = 'update non_members set amount_contributed =%s where user_ID =%s'
            cursor.execute(querry, val)
            myconn.commit()
            yee = input("""
            1. Perfrom another Operation
            2. Logout
            >> """)
            if yee == '1':
                time.sleep(2)
                operation()
            elif yee == '2':
                time.sleep(2)
                print('Logout Successful')
                from home import home
                time.sleep(2)
                home()
            else:
                print('Invalid Input')
                time.sleep(1)
                yee = input("""
            1. Perfrom another Operation
            2. Logout
            >> """)
        else:
            print('Invalid User ID')

def borrow():
    print("""
    Loan Page
    You are about to request for a Loan;
    Enter your neccessary Informations
    """)
    user = input('User ID>> ')
    val = (user, )
    querry = 'select * from non_members where user_ID =%s'
    cursor.execute(querry, val)
    global result
    result = cursor.fetchone()
    if result:
        time.sleep(1)
        print('Processing >>>')
        time.sleep(2)
        print(f'Dear {result[1]} {result[3]}, you are requesting a loan with Cosmos Corperative Society')
        if result[11] == 0:
            amount = int(input('Amount>> '))
            val1 = (1, )
            querry = 'select * from treasure_account where ID =%s'
            cursor.execute(querry, val1)
            global result2
            result2 = cursor.fetchone()
            if result2:
                if (result2[5] != 0) and (result2[5] > amount):
                    time.sleep(2)
                    print('verifying >>>')
                    if amount < result2[5]:
                        time.sleep(2)
                        print('Processing >>>')
                        if result[9] != 0:
                            time.sleep(3)
                            print(f'Dear {result[1]} {result[3]}, you are requesting for a loan of N{amount} with an interest of 5%')
                            refund = int((amount*0.05) + (amount))
                            time.sleep(2)
                            print('Processing >>>')
                            time.sleep(3)
                            print(f"""Dear {result[1]} {result[3]}, you are Eligible for a loan of N{amount} with interest of 5%.
                            Sum total of PayBack Loan is N{refund}""")
                            time.sleep(2)
                            req = input('Enter 4 digits PIN>> ')
                            pin = result[8]
                            if req == pin:
                                loan = (result[11] + amount)
                                val3 = (loan, pin)
                                querry = 'update non_members set Loan =%s where pin =%s'
                                cursor.execute(querry, val3)
                                myconn.commit()
                                time.sleep(2)
                                print('Processing >>>')
                                time.sleep(2)
                                print('Loan Application Successful')
                                treas = (result2[3] - result2[4])
                                val5 = (treas, 1)
                                querry2 ='update treasure_account set balance =%s where ID =%s'
                                cursor.execute(querry2, val5)
                                myconn.commit()
                                out = result2[4] + amount
                                val4 = (out, 1)
                                querry1 = 'update treasure_account set money_OUT =%s where ID =%s'
                                cursor.execute(querry1, val4)
                                myconn.commit()
                                time.sleep(2)
                                yee = input("""
                                1. Perfrom another Operation
                                2. Logout
                                >> """)
                                if yee == '1':
                                    operation()
                                elif yee == '2':
                                    time.sleep(1)
                                    print('Logout Successful')
                                    sys.exit()
                                else:
                                    print('Invalid Input')
                                    time.sleep(1)
                                    yee = input("""
                                1. Perfrom another Operation
                                2. Logout
                                >> """)
                            else:
                                print('Invalid PIN')
                                time.sleep(2)
                                borrow()
                        elif result[9] == 0:
                            time.sleep(3)
                            print(f'You have made no Contributions/Donation to the society, hence interest rate of 10% on Loaned amount')
                            time.sleep(2)
                            print('Redirecting >>>')
                            time.sleep(3)
                            print(f'Dear {result[1]} {result[3]}, you are requesting for a loan of N{amount} with an interest of 10%')
                            refund = int((amount*0.1) + (amount))
                            time.sleep(2)
                            print('Processing >>>')
                            time.sleep(3)
                            print(f"""Dear {result[1]} {result[3]}, you are Eligible for a loan of N{amount} with interest of 10%.
                            Sum total of PayBack Loan is N{refund}""")
                            time.sleep(2)
                            req = input('Enter 4 digits PIN>> ')
                            pin = result[8]
                            if req == pin:
                                loan = (result[11] + amount)
                                val3 = (loan, pin)
                                querry = 'update non_members set Loan =%s where pin =%s'
                                cursor.execute(querry, val3)
                                myconn.commit()
                                time.sleep(2)
                                print('Loan Application Successful')
                                treas = (result2[3] - result2[4])
                                val5 = (treas, 1)
                                querry2 ='update treasure_account set balance =%s where ID =%s'
                                cursor.execute(querry2, val5)
                                myconn.commit()
                                out = result2[4] + amount
                                val4 = (out, 1)
                                querry1 = 'update treasure_account set money_OUT =%s where ID =%s'
                                cursor.execute(querry1, val4)
                                myconn.commit()
                                time.sleep(2)
                                yee = input("""
                                1. Perfrom another Operation
                                2. Logout
                                >> """)
                                if yee == '1':
                                    operation()
                                elif yee == '2':
                                    time.sleep(2)
                                    print('Logout Successful')
                                    from home import home
                                    time.sleep(2)
                                    home()
                                else:
                                    print('Invalid Input')
                                    time.sleep(1)
                                    yee = input("""
                                1. Perfrom another Operation
                                2. Logout
                                >> """)
                            else:
                                print('Invalid PIN')
                                time.sleep(2)
                                borrow()
                        else:
                            print('Unknown')
                    elif (amount == result2[5]) and (amount > result2[5]):
                        print("""Application Denied !!
                        Kindly request for a LESSER AMOUNT""")
                        time.sleep(1)
                        borrow()
                else:
                    print("""Application Denied !!
                    Kindly request for a LESSER AMOUNT""")
                    time.sleep(1)
                    borrow()
            else:
                print('Unknown')
                time.sleep(1)
                borrow()
        elif result[11] != 0:
            print(f'Dear {result[1]} {result[3]}, you have an oustanding Loan, hence Application denied.')
            time.sleep(2)
            lo = input("""
            1. Pay Loan
            0. Back
            >> """)
            if lo == '1':
                time.sleep(1)
                pay_loan()
            elif lo == '0':
                time.sleep(1)
                operation()
            else:
                print('Invalid Input')
    else:
        print('Record not found')

def pay_loan():
    global res
    global user
    global refund
    global refunds
    print("""Pay Loan
    Proceed by providing necessary informations """)
    time.sleep(2)
    user = input('User ID>> ')
    time.sleep(1)
    uuse = input('Email>> ')
    val = (user, uuse)
    querry = 'select * from non_members where user_ID =%s and email =%s'
    cursor.execute(querry, val)
    res = cursor.fetchone()
    if res:
        time.sleep(2)
        print('Verifying >>>')
        time.sleep(2)
        print('Processing >>>')
        if res[10] != 0:
            refund = int((res[11]*0.05) + (res[11]))
            time.sleep(3)
            print(f'Dear {res[1]} {res[3]} your outstanding loan is N{res[11]}, with an interest of 5% PayBack loan is N{refund}')
            time.sleep(2)
            checkLoann2
        elif res[10] == 0:
            refunds = int((res[11]*0.1) + (res[11]))
            time.sleep(2)
            print(f'Dear {res[1]} {res[3]} your outstanding loan is N{res[11]}, with an interest of 10% PayBack loan is N{refunds}')
            time.sleep(2)
            checkLoann5()
        else:
            print('Unknown')
    else:
        print('Record not found')

def checkLoann2():
    req = input("""
    0. Request Account Number
    00. Exit
    >> """)
    if req == '0':
        time.sleep(1)
        print('Processing >>>')
        val = (1, )
        querry = 'select * from treasure_account where ID =%s'
        cursor.execute(querry, val)
        acc = cursor.fetchone()
        if acc:
            time.sleep(3)
            print(f'ACCOUNT NUMBER: {acc[2]}')
            time.sleep(2)
            back = int(input('Enter Amount>> '))
            if back == refund:
                time.sleep(2)
                print(f'{res[1]} {res[3]} Confirm PayBack amount of N{back} to {acc[1]}')
                time.sleep(2)
                pn = input('Enter 4digits PIN>> ')
                val = (pn, )
                querry = 'select * from non_members where pin =%s'
                cursor.execute(querry, val)
                lol = cursor.fetchone()
                if lol:
                    time.sleep(2)
                    print('Processing >>>')
                    time.sleep(3)
                    print('Transaction Successful')
                else:
                    print('Invalid PIN')
                ba = (acc[5] + back)
                val10 = (ba, 1)
                querry = 'update treasure_account set balance =%s where ID =%s'
                cursor.execute(querry, val10)
                myconn.commit()
                aba = (acc[3] + back)
                valla = (aba, 1)
                querry = 'update treasure_account set money_IN =%s where ID =%s'
                cursor.execute(querry, valla)
                myconn.commit()
                val1 = (res[11], user)
                querry = 'update non_members set Refund =%s where user_ID =%s'
                cursor.execute(querry, val1)
                myconn.commit()
                interest = refund - res[11]
                val2 = (interest, pn)
                querry = 'update non_members set interest =%s where pin =%s'
                cursor.execute(querry, val2)
                myconn.commit()
                loan = (refund - back)
                val (loan, user)
                querry = 'update non_members set Loan =%s where user_ID =%s'
                cursor.execute(querry, val)
                myconn.commit()
                time.sleep(2)
                yee = input("""
                1. Perfrom another Operation
                2. Logout
                >> """)
                if yee == '1':
                    time.sleep(2)
                    operation()
                elif yee == '2':
                    time.sleep(2)
                    print('Logout Successful')
                    from home import home
                    time.sleep(2)
                    home()
                else:
                    print('Invalid Input')
                    time.sleep(1)
                    yee = input("""
                1. Perfrom another Operation
                2. Logout
                >> """)
            else:
                print(f'You are to PayBack total of N{refund}')
                time.sleep(1)
                checkLoann2()
    elif req == '00':
        time.sleep(2)
        operation()
    else:
        print('Invalid Input')
        time.sleep(1)
        checkLoann2()

def checkLoann5():
    req = input("""
    0. Request Account Number
    00. Exit
    >> """)
    if req == '0':
        time.sleep(1)
        print('Processing >>>')
        val = (1, )
        querry = 'select * from treasure_account where ID =%s'
        cursor.execute(querry, val)
        acc = cursor.fetchone()
        if acc:
            time.sleep(3)
            print(f'ACCOUNT NUMBER: {acc[2]}')
            time.sleep(2)
            backs = int(input('Enter Amount>> '))
            if backs == refunds:
                time.sleep(2)
                print(f'{res[1]} {res[3]} Confirm PayBack amount of N{backs} to {acc[1]}')
                time.sleep(2)
                pnn = input('Enter 4digits PIN>> ')
                val3 = (pnn, )
                querry = 'select * from non_members where pin =%s'
                cursor.execute(querry, val3)
                loll = cursor.fetchone()
                if loll:
                    time.sleep(2)
                    print('Processing >>>')
                    time.sleep(3)
                    print('Transaction Successful')
                else:
                    print('Invalid PIN')
                ba = (acc[5] + backs)
                val10 = (ba, 1)
                querry = 'update treasure_account set balance =%s where ID =%s'
                cursor.execute(querry, val10)
                myconn.commit()
                aba = (acc[3] + backs)
                valla = (aba, 1)
                querry = 'update treasure_account set money_IN =%s where ID =%s'
                cursor.execute(querry, valla)
                myconn.commit()
                val0 = (res[11], user)
                querry = 'update non_members set Refund =%s where user_ID =%s'
                cursor.execute(querry, val0)
                myconn.commit()
                interests = refunds - res[11]
                val4 = (interests, pnn)
                querry = 'update non_members set interest =%s where pin =%s'
                cursor.execute(querry, val4)
                myconn.commit()
                loan = (refunds - backs)
                val = (loan, user)
                querry = 'update non_members set Loan =%s where user_ID =%s'
                cursor.execute(querry, val)
                myconn.commit()
                time.sleep(2)
                yeee = input("""
                1. Perfrom another Operation
                2. Logout
                >> """)
                if yeee == '1':
                    time.sleep(2)
                    operation()
                elif yeee == '2':
                    time.sleep(2)
                    print('Logout Successful')
                    from home import home
                    time.sleep(2)
                    home()
                else:
                    print('Invalid Input')
                    time.sleep(1)
                    yeee = input("""
                1. Perfrom another Operation
                2. Logout
                >> """)
            else:
                print(f'You are to PayBack total of N{refunds}')
                time.sleep(1)
                checkLoann5()
    elif req == '00':
        time.sleep(2)
        operation()
    else:
        print('Invalid Input')
        time.sleep(1)
        checkLoann5()