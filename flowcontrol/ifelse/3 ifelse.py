correct_username="admin"
correct_password="12345"

username=input("Enter username: ")
password=input("Enter password: ")

if username==correct_username and password==correct_password:
    print("Login successful")
else:
    print("Invalid credentials")
