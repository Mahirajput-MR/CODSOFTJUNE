import random
import string
def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars)for i in range(length))
    return password
print("Welcome to Password Generator")
password_length=int(input("enter the length of the password: "))
pass_=generate_password(password_length)
print("Your password is: ",pass_)
