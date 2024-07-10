from cryptography.fernet import Fernet 

# key +pasword + text to encrypt = randomtext
# random text + key+ passwrod =text to encrypt

'''
def write_key():
    key = Fernet.generate_key() 
    with open('key.key',"wb") as key_file:
        key_file.write(key)
        '''

def load_key():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key 

master_pwd = input("What is the master pasword? ")
key = load_key() + master_pwd.encode()
fer =Fernet(key)

def view():
    with open('password.txt','r')as f:
        for line in f.readline():
            data = line.rstrip()
            user,passw =data.split("|")
            print("User: ", user, "| password: ",
                  fer.decrypt(passw.encode()))

def add():
    name = input("Account Name: ")
    pwd= input("Password: ")

    with open('password.txt','a')as f:
         f.write(name +"|" + fer.encrypt(pwd.encode()) + "\n")


while True:
    mode =input("Would you like to add password or view exsiting password once (view, add), press q to Quit?  : ").lower()
    if mode=="q":
        break

    if mode=="view":
        view()
    elif mode =="add":
        add()
    else:
        pass