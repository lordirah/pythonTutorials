import sqlite3
import datetime
import getpass
from cryptography.fernet import Fernet
import json

def login():
    print("""Password Manager Login""")
    usr_name,usr_password = register()
    username = input("Username : ")
    password = getpass.getpass("Password : ")
    if username == usr_name and password == usr_password:
        try:
            with open('data.json', 'r') as f:
                json_dict = json.load(f)
        except:
            json_dict = {}
            json_object = json.dumps(json_dict, indent = 4)
            with open("data.json", "w") as outfile:
                outfile.write(json_object)
        while True:
            menu()
            opt = int(input("Choose an option : "))
            if opt == 1:
                insert(json_dict)
            elif opt == 2:
                search(json_dict)
            elif opt == 3:
                update(json_dict)
            elif opt == 4:
                delete(json_dict)
            elif opt ==5:
                break
    else :
        print("Invalid credentials !")
        
def register():
    try:
        with open('usr.json', 'r') as f:
            usr_json = json.load(f)
            usr_name = usr_json['username']
            usr_password = decrypt(usr_json['key'], usr_json['password'])
            return usr_name,usr_password.decode('utf-8')
    except:
        usr_name = input("Enter new user name : ")
        usr_password = input("Enter new password : ")
        usr_key = generate_key()
        usr_enc_password = encrypt(usr_key, usr_password)
        usr_dict = {"username" : usr_name, "password" : usr_enc_password.decode('utf-8')\
                ,"key" : usr_key.decode('utf-8')}
        usr_json = json.dumps(usr_dict, indent = 4)
        with open("usr.json", "w") as outfile:
                outfile.write(usr_json)
        return usr_name, usr_password

def menu():
    print("""Menu
    1. Insert new password
    2. Search password
    3. Update password
    4. Delete password
    5. Exit
    """)

def generate_key():
    return Fernet.generate_key()

def encrypt(key, encrypt_txt):
    encrypt_inst = Fernet(key)
    return encrypt_inst.encrypt(encrypt_txt.encode('utf-8'))

def decrypt(key, encrypt_txt):
    decrypt_inst = Fernet(key.encode('utf-8'))
    return decrypt_inst.decrypt(encrypt_txt.encode('utf-8'))

def insert(json_dict):
    app_name = input("Enter an app name : ")
    app_user = input("Enter an username : ")
    app_pass = getpass.getpass("Enter a password : ")
    app_pass2 = getpass.getpass("Re-enter password : ")
    if app_pass == app_pass2:
        f_key = generate_key()
        f_enc_pass = encrypt(f_key, app_pass)
        try :
            next(val for key, val in json_dict.items() if app_name in key)
            print("Value available try updating !")
        except StopIteration:
            temp_dict = { app_name : [app_user, f_enc_pass.decode('utf-8'), f_key.decode('utf-8'), str(datetime.datetime.now())]}
            print(temp_dict)
            json_dict.update(temp_dict)
            json_object = json.dumps(json_dict, indent= 4)
            with open("data.json","w") as json_file:
                json_file.write(json_object)
            print("Not found ! Inserting new record")
    else :
        print("Password not matching !")

def search(json_dict):
    search_key = input("Enter a search app name : ")
    print("#############################################")
    if search_key != "":
        if search_key in json_dict:
            print("{:<8} {:<10} {:<15} {:<10}".format('AppName','UserName','Password','UpdatedDT'))
            for key, value in json_dict.items():
                if key == search_key:
                    decrypted_pass = decrypt(value[2], value[1])
                    print("{:<8} {:<10} {:<15} {:<10}".format(key, value[0], decrypted_pass.decode('utf-8'), value[3]))
        else:
            print("App not available !")
    else:
        print("{:<8} {:<10} {:<15} {:<10}".format('AppName','UserName','Password','UpdatedDT'))
        for key, value in json_dict.items():
            decrypted_pass = decrypt(value[2], value[1])
            print("{:<8} {:<10} {:<15} {:<10}".format(key, value[0], decrypted_pass.decode('utf-8'), value[3]))
    print("#############################################")

def delete(json_dict):
    app_name = input("Enter an app name to delete : ")
    json_dict.pop(app_name , 'No Key found')
    json_object = json.dumps(json_dict, indent= 4)
    with open("data.json","w") as json_file:
        json_file.write(json_object)
    print(f"Deleted {app_name} !")

def update(json_dict):
    app_name = input("Enter an app name to update : ")
    json_dict.pop(app_name, 'No Key found')
    insert(json_dict)

if __name__ == "__main__":
    login()
