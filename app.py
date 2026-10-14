import random
BankData={}

def createAccount():
    print(' user want to create a new account..')
    print("--------------CREATE NEW ACCOUNT---------------")
    print("give me this information")
    name=input("enter your name:-")
    mobile_no=int(input("enter your mobile number:-"))
    Adhar_no=int(input("enter your adhhar number:-"))
    age=int(input("enter your age:-"))
    amount=int(input('enter your amount:-'))
    account_no=random.randint(1000,9999)
    
    BankData[account_no]={
        'name':name,
        'mobile_no':mobile_no,
        'Adhar_no':Adhar_no,
        'age':age,
        'amount':amount,
        'account_no':account_no
    }
    print("==========ACCOUNT CREATED SUCCESSFULLY===========")
    print('account no:-',BankData[account_no]['account_no'])
    
def depositeMoney():
    print(' user want to deposite money..')
    acc_no=int(input('Enter your account number:-'))
    if  acc_no in BankData:
        amount=(int(input("enter yout deposite money:->")))
        BankData[acc_no]['amount']=BankData[acc_no]['amount']+amount
        print('=====DEPOSITE MONEY SUCCESSFULLY=====')
        print('total money is:-',BankData[acc_no]['amount'] )
    else:
        print("account not found..")  
        
        
    
def banckStatement():
    print(' user want to check bank statement..')
    acc_no=int(input('enter your account number:-'))
    if acc_no in BankData:
        print('bankdata---->>>',BankData)
        print('-----BANK HOLDER DETAILS-----')
        print('name:-',BankData[acc_no]['name'])
        print('mobile_no:-',BankData[acc_no]['mobile_no'])
        print('Adhar_no:-',BankData[acc_no]['Adhar_no'])
        print('amount:-',BankData[acc_no]['amount'])
        print('savings:-',BankData[acc_no]['amount'])
    else:
        print("account not found.....")
    
    
    
def updateDetails():
    print(" user want to update details")
    acc_no=int(input('enter your account number:-'))
    if acc_no in BankData:
        print('==========SELECT OPTION===========')
        print('1.update name:')
        print('2.mobile number:') 
        print('3.adhar card number:')
        print('4.age')   
        choice=int(input('plz select your choice:-'))
        if choice==1:
            print('user want to update name..')
            Newname=input('enter your new name:-')
            BankData[acc_no]['name']=Newname
            print('-------------update your name sucessfully---------------')
            print( 'newname:=',BankData[acc_no]['name'])
        elif choice==2:
            print("user want to  update mobile number..")
            Newmobilenum=input('enter your new mobilenum:-')
            BankData[acc_no]['mobile_no']=Newmobilenum
            print('-------------update your mobilenumber sucessfully---------------')
            print( 'newmobileno:=',BankData[acc_no]['mobile_no'])
        elif choice==3:
            print('user want to update adharcard number..')
            
            newAdhar_no=input('enter your new adhar card number:-')
            BankData[acc_no]['Adhar_no']=newAdhar_no
            print('-------------update your adhar no sucessfully---------------')
            print( 'newAdhar_no:=',BankData[acc_no]['Adhar_no'])
        elif choice==4:
            print("user want to update age")
            
            newAge=input('enter your new age number:-')
            BankData[acc_no]['age']=newAge
            print('-------------update your new age sucessfully---------------')
            print( 'newAdhar_no:=',BankData[acc_no]['age'])
        
def widthrowMoney():
    print("user want to widthrow money")
    acc_no=int(input('enter your account number'))
    if acc_no in BankData:
        amount=(int(input('enter your widthrow money:-')))
        BankData[acc_no]['amount']=BankData[acc_no]['amount']-amount
        print('=== money widthrow successfully ===')
        print('total amount is :-',BankData[acc_no]['amount'])
    else:
        print('account not found')
def exit():
    print(" thanks for visit")

while True:
    print("----------------------------------------------")
    print("-------------WELCOME TO THE BANK--------------")
    print("----------------------------------------------")

    print("1.create a new account..")
    print("2.deposite money..")
    print("3.check bank statement..")
    print("4.update details..")
    print("5.widthrow money..")
    print("6.exit")


    choice=int(input("enter your choice.."))

    if choice==1:
        createAccount()
    elif choice==2:
        depositeMoney()
    elif choice==3:
        banckStatement()
    elif choice==4:
        updateDetails()
    elif choice==5:
        widthrowMoney()
    elif choice==6:
        exit()
    else:
         print("Enter Valid Choice..")