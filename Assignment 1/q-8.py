import hashlib
def hash_password(password):
   hashlib.sha1(password.encode()).hexdigest()
susername = "user1"
spassword_hash = hash_password("mypassword")
input_username = input("Enter username: ")
input_password = input("Enter password: ")
input_password_hash = hash_password(input_password)
if input_username == susername and input_password_hash == spassword_hash:
      print("Authentication successful!")
else:
      print("Authentication failed!")