accounts = {}

def account_create():
    while True:
        while True:
            new_username = input("Input username: ")
            if new_username in accounts:
                print("This username has already been taken")
            else:
                break
        while True:
            new_password = input("Input password: ")
            confirm_password = input("Confirm your password: ")
            if new_password != confirm_password:
                print("Password does not match")
            else:
                break
        
        accounts[new_username] = new_password
        print(f"Account created successfully for {new_username}!")
        print(accounts)
          
account_create()
    
        
    