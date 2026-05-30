stored_username = "admin"
stored_password = "1234"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Login Failed")
