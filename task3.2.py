import hashlib

SALT = "my_salt1"
RES1 = hashlib.sha256(SALT.encode('utf-8') + (input("Create a password: ")).encode()).hexdigest()
RES2 = hashlib.sha256(SALT.encode('utf-8') + (input("Enter password: ")).encode()).hexdigest()
if RES1 == RES2:
    print("You entered the correct password")
else:
    print("You entered the wrong password")
