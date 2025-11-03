import os
import getpass
import hashlib

password = os.getenv("MY_SECRET_PASSWORD")
hashed_password = hashlib.sha256(password.encode()).hexdigest()
trial = 1


def verification():
    global trial
    user_input = getpass.getpass(f"PASSWORD({trial}/5): ")
    hashed_input = hashlib.sha256(user_input.encode()).hexdigest()
    if hashed_input != hashed_password:
        trial += 1
        if trial > 5:
            return False
        return verification()
    else:
        return True


Logged_in = verification()

if Logged_in:
    print("Log in!")
else:
    print("Out!")