print("Login System")
# การรับค่าจากผู้ใช้
username = input("Username : ")
# print("Username")
# print(type(username))
password = input("Password : ")

if username.strip().lower == "admin" and password.strip().lower == "1234":
    print("Login Success")
else:
    print("Login Failed")
