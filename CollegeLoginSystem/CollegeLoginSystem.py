import sqlite3
import hashlib
from sqlite3 import Error

DOMAIN = "@exe-coll.ac.uk"
print(DOMAIN)
users = []

def createUser(userBase,password):
    userName = userBase+DOMAIN
    password = password
    print(userName, password)
    users.append(userName)
    print(users)

def userCheck():
    print('true')

def userLogin():
    print('test')

def userLockout():
    print('you are locked out')

print("WELCOME. PLEASE CREATE YOUR USER PROFILE! ")
firstName = input("Enter Firstname: ")
surname = input("Enter Surname: ")
password = input("Enter your password: ")
userPass = f'{password}'
userBase = f'{firstName}{surname}'
createUser(userBase,password)
userLogin()
