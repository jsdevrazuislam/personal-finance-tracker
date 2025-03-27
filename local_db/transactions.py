import auth
import utils
import uuid
import requests


TRANSACTION_FILE = 'transactions.json'
API_KEY = "YOUR_API_KEY" 
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"


def add_transaction(transactions):
    print("📌 Enter expense details:  ")
    amount = int(input("Amount: "))
    category = input("Category (Food/Transport/etc.): ")
    target_currency = input("Enter target currency (e.g., BDT, EUR, GBP): ").upper()
    date = input("Date (YYYY-MM-DD): ")
    payload = {
        'amount': convert_currency(amount, 'USD', target_currency),
        'category': category,
        'date': date,
        'id': uuid.uuid4().hex
    }
    transactions.append(payload)
    utils.save_db(transactions, TRANSACTION_FILE)
    print("✅ Expense Added Successfully! ")

def view_transactions(transactions):
    print("📌 Expense details: ")
    print("\n")
    for transaction in transactions:
        print("*" * 70)
        print(f"🔹 Id: {transaction['id']}")
        print(f"🔹 Amount: {transaction['amount']}")
        print(f"🔹 Category: {transaction['category']}")
        print(f"🔹 Date: {transaction['date']}")
    print("\n")

def update_transaction(transactions):
    id = input("Enter Your Id: ")
    transaction = utils.is_exists(transactions, id)
    if transaction:
        amount = int(input("Updated Amount: "))
        category = input("Updated Category (Food/Transport/etc.): ")
        date = input("Updated Date (YYYY-MM-DD): ")
        transaction['amount'] = amount
        transaction['category'] = category
        transaction['date'] = date
        utils.save_db(transactions, TRANSACTION_FILE)
        print("✅ Expense Updated Successfully! ")
    else:
        print("❌ Expense not found!")

def delete_transaction(transactions):
    id = input("Enter Your Id: ")
    transaction = utils.is_exists(transactions, id)
    if transaction:
        updated_list = [item for item in transactions if item['id'] != id]
        utils.save_db(updated_list, TRANSACTION_FILE)
        print("✅ Expense Deleted Successfully! ")
    else:
        print("❌ Expense not found!")

def filter_by_category(transactions):
    filter_transactions = sorted(
        transactions,
        key=lambda x: (x['category'], x['date'])
    )
    print("📌 Expense details: ")
    print("\n")
    for transaction in filter_transactions:
        print("*" * 70)
        print(f"🔹 Id: {transaction['id']}")
        print(f"🔹 Amount: {transaction['amount']}")
        print(f"🔹 Category: {transaction['category']}")
        print(f"🔹 Date: {transaction['date']}")
    print("\n")

def convert_currency(amount, from_currency, to_currency):
    response = requests.get(BASE_URL)
    data = response.json()
    
    if response.status_code == 200:
        exchange_rate = data['conversion_rates'].get(to_currency)
        if exchange_rate:
            converted_amount = amount * exchange_rate
            return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
        else:
            return "Invalid currency code!"
    else:
        return "Error fetching exchange rates!"


@utils.login_required
def run_transactions():
    transactions = utils.load_data(TRANSACTION_FILE)
    while True:
        print("📌 Choose an option:  ")
        print("1️⃣ Add Expense  ")
        print("2️⃣ View Expenses  ")
        print("3️⃣ Update Expense  ")
        print("4️⃣ Delete Expense ")
        print("5️⃣ Filter by Category  ")
        print("6️⃣ Convert Currency ")
        print("7️⃣ Logout")

        choose = input('Enter your choose: ')

        match choose:
            case '1':
                add_transaction(transactions)
            case '2':
                view_transactions(transactions)
            case '3':
                update_transaction(transactions)
            case '4':
                delete_transaction(transactions)
            case '5':
                filter_by_category(transactions)
            case '6':
                amount = int(input("Enter Amount: "))
                currentCurrency = input("Enter current currency like USD/BDT: ") 
                convertCurrency  = input("Enter convert currency like USD/BDT: ") 
                print(convert_currency(amount, currentCurrency, convertCurrency))
            case '7': 
                auth.logout()
                break
            case _:
                print('❌ Invalid Choose')
