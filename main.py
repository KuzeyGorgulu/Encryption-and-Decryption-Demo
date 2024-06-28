#Librarys
from cryptography.fernet import Fernet

#Creating the crypting key 

"""
(NOTE:If you created your `key.key` file at first with `write_key` function, you don't need to use this function anymore. 
Using it again will make you create a second `key.key` file which may cause problems.)

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

#listing passwords function
def list():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data =line.rstrip()
            user, passw = data.split("|")
            print("User: ", user,",", "Password: ", fer.decrypt(passw.encode()).decode())

#Creating passwords function
def new():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

#Inputting user for creating or listing
while True:
    mode = input("Would you want to create a new password or list the existing passwords? Press q to quit. (new,list,q)").lower()
    if mode == "q":
        break
    
    if mode == "new":
        new()
    elif mode == "list":
        list()
    else:
        print("Invalid input. Please try again.")
        continue
