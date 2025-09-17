from cryptography.fernet import Fernet
key=Fernet.generate_key()
cipher=Fernet(key)
cusername='user123'
cpassword='pass123'.encode()
epassword=cipher.encrypt(cpassword)
username=input("Enter your username: ")
password=input("Enter your password: ").encode()
if(username==cusername and password==cipher.decrypt(epassword)):
     print('Authentication Successful!')
else:
    print('Authentication Failed!')