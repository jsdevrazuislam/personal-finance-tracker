import auth
import json

def login_required(func):
    def wrapper(*args, **kwargs):
        if auth.logged_in_user:
            return func(*args, **kwargs)
        else:
            print("🚫 You must be logged in to perform this action.")
    return wrapper

def logout_required(func):
    def wrapper(*args, **kwargs):
        if not auth.logged_in_user:
            return func(*args, **kwargs)
        else:
            print("🚫 You must be logged out to perform this action.")
    return wrapper

def load_data(FILE):
        try:
            with open(FILE, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return [] 

def save_db(data, FILE):
    try:
        with open(FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print("❌ Database Save Error ", e)

def is_exists(data, id):
    return next((item for item in data if item['id'] == id), None)

