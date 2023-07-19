import time
import random
import sys
import mysql.connector as connection
myconn = connection.connect(host = '127.0.0.1', user = 'root', passwd = 'Oluwadamilola99$$', database = 'corperative')
cursor = myconn.cursor(buffered=True)
def member():
    acct = input("""
    1. Login
    2. Create Account
    0. Back
    >> """)
    if acct == '1':
        time.sleep(1)
        member_login()
    elif acct == '2':
        time.sleep(1)
        member_create()
    elif acct == '0':
        time.sleep(1)
        from home import home
        home()
    else:
        print('Invalid Input')
        time.sleep(1)
        member()

def member_create():
    print("""
    Create New Account
    
    Enter your Information >>""")
    val = []
    info = ('first_name', 'middle_name', 'last_name', 'gender', 'age', 'phone_number', 'address', 'pin', 'amount_contributed', 'Refund', 'Loan', 'interest', 'Email', 'passwd', 'member_ID')
    querry = 'insert into members(first_name, middle_name, last_name, gender, age, phone_number, address, pin, amount_contributed, Refund, Loan, interest, Email, passwd, member_ID) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    for x in range(15):
        if info[x] == 'member_ID':
            bInfo = random.randint(99213543, 99986432)
        elif info[x] == 'phone_number':
            bInfo = input('Enter Phone number: ')
            while len(bInfo) != 11:
                print('Invalid Phone number; Phone number must be 11 digits')
                bInfo = input('Enter Phone number: ')
        elif info[x] == 'Refund':
            bInfo = 0
        elif info[x] == 'Loan':
            bInfo = 0
        elif info[x] == 'interest':
            bInfo = 0
        elif info[x] == 'amount_contributed':
            bInfo = 0
        else:
            bInfo = input(f'Enter your {info[x]}: ')
        val.append(bInfo)
    cursor.execute(querry, val)
    myconn.commit()
    time.sleep(1)
    print(f'Dear {val[0]} {val[1]}, Your member ID is {val[14]}')
    time.sleep(2)
    member_login()

def member_login():
    email = input("""
    Login Account 
    
    Email >> """)
    passwrd = input("""
    Password >> """)
    val = (email, passwrd)
    querry = 'select * from members where email =%s and passwd =%s'
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
        print('Invalid Email or Password')
        time.sleep(1)
        member_login()

def operation():
    user = input("""
    Cosmos Corperative Society
    1. Contribute Money
    2. Get Loan
    3. Pay Loan
    0. Log Out
    >> """)
    if user == '1':
        contribute()
    elif user == '2':
        time.sleep(2)
        borrow()
    elif user == '3':
        time.sleep(2)
        pay_loann()
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

def contribute():
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
        user = input('Enter Member ID>> ')
        val = (user, )
        querry = 'select * from members where member_ID =%s'
        cursor.execute(querry, val)
        result2 = cursor.fetchone()
        if result2:
            time.sleep(2)
            print('Processing')
            time.sleep(2)
            print('Transaction Successful')
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
            2. Logout""")
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
            print('Invalid member ID')

def borrow():
    print("""
    Loan Page
    You are about to request for a Loan;
    Enter your neccessary Informations
    """)
    user = input('Member ID>> ')
    val = (user, )
    querry = 'select * from members where member_ID =%s'
    cursor.execute(querry, val)
    global result
    result = cursor.fetchone()
    if result:
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
                            society_B = result2[3] - amount
                            val2 = (society_B, 1)
                            querry = 'update treasure_account set balance =%s where ID =%s'
                            cursor.execute(querry, val2)
                            myconn.commit()
                            time.sleep(2)
                            req = input('Enter 4 digits PIN>> ')
                            pin = result[8]
                            if req == pin:
                                loan = (result[11] + amount)
                                val3 = (loan, pin)
                                querry = 'update members set Loan =%s where pin =%s'
                                cursor.execute(querry, val3)
                                myconn.commit()
                                time.sleep(2)
                                print('Processing >>>')
                                time.sleep(3)
                                print('Loan Application Successful')
                                querry = 'select sum(loan) from members'
                                val = (4, )
                                cursor.execute(querry)
                                res = cursor.fetchone()
                                out = result2[4] + amount
                                val4 = (out, 1)
                                querry1 = 'update treasure_account set money_OUT =%s where ID =%s'
                                cursor.execute(querry1, val4)
                                myconn.commit()
                                treas = result2[3] - result2[4]
                                val5 = (treas, 1)
                                querry2 ='update treasure_account set balance =%s where ID =%s'
                                cursor.execute(querry2, val5)
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
                        elif result[9] == 0:
                            time.sleep(3)
                            print(f'You have made no Contributions/Donation to the society, hence interest rate of 10% on Loaned amount')
                            time.sleep(2)
                            print('Redirecting >>>')
                            time.sleep(3)
                            print(f'Dear {result[1]} {result[3]}, you are requesting for a loan of N{amount} with an interest of 10%')
                            refund = int((amount*0.1) + (amount))
                            time.sleep(1)
                            print('processing >>>')
                            time.sleep(3)
                            print(f"""Dear {result[1]} {result[3]}, you are Eligible for a loan of N{amount} with interest of 10%.
                            Sum total of PayBack Loan is N{refund}""")
                            society_B = result2[3] - result2[4]
                            val2 = (society_B, 1)
                            querry = 'update treasure_account set balance =%s where ID =%s'
                            cursor.execute(querry, val2)
                            myconn.commit()
                            time.sleep(2)
                            req = input('Enter 4 digits PIN>> ')
                            pin = result[8]
                            if req == pin:
                                loan = (result[11] + amount)
                                val3 = (loan, pin)
                                querry = 'update members set Loan =%s where pin =%s'
                                cursor.execute(querry, val3)
                                myconn.commit()
                                time.sleep(2)
                                print('Processing >>>')
                                time.sleep(3)
                                print('Loan Application Successful')
                                querry = 'select sum(loan) from members'
                                val = (4, )
                                cursor.execute(querry)
                                res = cursor.fetchone()
                                out = result2[4] + amount
                                val4 = (out, 1)
                                querry1 = 'update treasure_account set money_OUT =%s where ID =%s'
                                cursor.execute(querry1, val4)
                                myconn.commit()
                                treas = result2[3] - result2[4]
                                val5 = (treas, 1)
                                querry2 ='update treasure_account set balance =%s where ID =%s'
                                cursor.execute(querry2, val5)
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
                                time.sleep(1)
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
                pay_loann()
            elif lo == '0':
                time.sleep(1)
                operation()
            else:
                print('Invalid Input')
    else:
        print('Record not found')

def pay_loann():
    global res
    global refund
    global userr
    global refunds
    print("""Pay Loan
    Proceed by providing necessary informations """)
    time.sleep(2)
    userr = input('Member ID>> ')
    time.sleep(1)
    uuse = input('Email>> ')
    val = (userr, uuse)
    querry = 'select * from members where member_ID =%s and email =%s'
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
            checkLoan2()
        elif res[10] == 0:
            refunds = int((res[11]*0.1) + (res[11]))
            time.sleep(3)
            print(f'Dear {res[1]} {res[3]} your outstanding loan is N{res[11]}, with an interest of 10% PayBack loan is N{refunds}')
            time.sleep(2)
            checkloan5()
        else:
            print('Unknown')
    else:
        print('Record not found')

def checkLoan2():
    back = int(input('Enter Amount>> '))
    if back == refund:
        time.sleep(2)
        print(f'{res[1]} {res[3]} Confirm PayBack amount of N{back} to Cosmos Corperative Society')
        time.sleep(2)
        pn = input('Enter 4digits PIN>> ')
        val = (pn, )
        querry = 'select * from members where pin =%s'
        cursor.execute(querry, val)
        lol = cursor.fetchone()
        if lol:
            time.sleep(2)
            print('Processing >>>')
            time.sleep(3)
            print('Transaction Successful')
        else:
            print('Invalid PIN')
        val1 = (res[11], userr)
        querry = 'update members set Refund =%s where member_ID =%s'
        cursor.execute(querry, val1)
        myconn.commit()
        interest = refund - res[11]
        val2 = (interest, pn)
        querry = 'update members set interest =%s where pin =%s'
        cursor.execute(querry, val2)
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
        checkLoan2()

def checkloan5():
    backs = int(input('Enter Amount>> '))
    if backs == refunds:
        time.sleep(2)
        print(f'{res[1]} {res[3]} Confirm PayBack amount of N{backs} to Cosmos Corperative Society')
        time.sleep(2)
        pnn = input('Enter 4digits PIN>> ')
        val3 = (pnn, )
        querry = 'select * from members where pin =%s'
        cursor.execute(querry, val3)
        loll = cursor.fetchone()
        if loll:
            time.sleep(2)
            print('Processing >>>')
            time.sleep(3)
            print('Transaction Successful')
        else:
            print('Invalid PIN')
        val0 = (res[11], userr)
        querry = 'update members set Refund =%s where member_ID =%s'
        cursor.execute(querry, val0)
        myconn.commit()
        interests = refunds - res[11]
        val4 = (interests, pnn)
        querry = 'update members set interest =%s where pin =%s'
        cursor.execute(querry, val4)
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
        checkloan5()