

#This is a import export project.

#The main idea of this project is we are creating a Digital HUB LOG of an import export buisness.

#Step one, make a login.
#Step two, make a user interface that displays (Imports) (Exports) (Logout) (Employees) (Payroll) (income)

#make the dictionary the accounts will save to.
accounts = {}

#The Login.

#create (create account)
def create():
    create_username = input("Whats the username you would like to create?")
    create_password = input("Whats the password you would like to create for this account?")
    accounts[create_username] = create_password
    print("Your account has been created!")

#create (login)
def login():
    login_username = input("Whats your existing username?")
    login_password = input("Whats your existing password?")
    if login_username in accounts and accounts[login_username] == login_password:
        print("Correct login, you may precede.")
    else:
        print("Incorrect login.")


while True:
    login_question = input(" 'login' , 'create' 'quit' ")
    if login_question == "login":
        login()
    elif login_question == "create":
        create()
    elif login_question == "quit":
        break

###
#Thats the login done.