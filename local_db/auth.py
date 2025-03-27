import json
import bcrypt
import transactions
import os
import utils

USER_FILE = 'users.json'
LOGGED_IN_USER_FILE = "logged_in_user.json"
logged_in_user = None 


def load_logged_in_user():
    try:
        with open(LOGGED_IN_USER_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_logged_in_user(user):
    with open(LOGGED_IN_USER_FILE, "w") as f:
        json.dump(user, f)

logged_in_user = load_logged_in_user()
users = utils.load_data(USER_FILE)




@utils.logout_required
def register():
    username = input("🔐 Enter your email: ").strip()
    password = input("🔑 Enter password: ")
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    for user in users:
        if user['username'] == username:
            print("❌ User already exits")
            return 
        
    payload = {
            'username': username,
            'password': hash.decode('utf-8')
    }
    users.append(payload)
    utils.save_db(users, USER_FILE)
    print("✅ Registration successful!")

@utils.logout_required
def login():
    global logged_in_user 
    username = input("🔐 Enter your email: ")
    password = input("🔑 Enter password: ")
    bytes_pw = password.encode('utf-8')


    for user in users:
        if user['username'] == username:
            stored_hash = user['password'].encode('utf-8') 
            if bcrypt.checkpw(bytes_pw, stored_hash):
                print("✅ Login successful!")
                logged_in_user = user 
                save_logged_in_user(user)
                transactions.run_transactions()
                return
            else:
                print("❌ Invalid password")
                return

def logout():
    global logged_in_user
    if logged_in_user:
        print(f"👋 Logged out {logged_in_user['username']}.")
        logged_in_user = None
        if os.path.exists(LOGGED_IN_USER_FILE): 
            os.remove(LOGGED_IN_USER_FILE)
    else:
        print("You are not logged in.")