import time
def home():
    user = input("""
    Welcome to Cosmos Corperative Society,
    1. Member Account
    2. Non_member Account
    >> """)
    if user == '1':
        from member_reg import member
        time.sleep(1)
        member()
    elif user == '2':
        from non_member_reg import non_member
        time.sleep(1)
        non_member()
    else:
        print('Invalid Input')
        time.sleep(1)
home()