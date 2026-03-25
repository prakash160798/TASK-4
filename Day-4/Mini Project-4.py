users = {
    "admin": "1234",
    "ravi": "pass123",
    "sita": "welcome"
}
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users:
        if users[username] == password:
            print(" Login Successful!")
        else:
            print(" Incorrect Password")
    else:
        print(" Username not found")
print("===== Login System =====")
login()