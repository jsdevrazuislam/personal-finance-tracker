# Personal Finance Tracker (CLI App)

## 📌 Project Overview
The **Personal Finance Tracker** is a Command-Line Interface (CLI) application built with Python. It allows users to manage their personal finances effectively by tracking income, expenses, and balance. The app also provides basic authentication and handles API calls for exchange rates (if required). Error handling is implemented to ensure smooth user experience.

## 🚀 Features
- **User Authentication** (Sign-up & Login)
- **Income & Expense Tracking**
- **Categorization of Transactions**
- **Balance Overview**
- **Export Transactions to JSON File**
- **API Integration for Currency Exchange (Optional)**
- **Error Handling for User Inputs**

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/jsdevrazuislam/personal-finance-tracker
cd personal-finance-tracker
```

### 2️⃣ Create & Activate Virtual Environment
```sh
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```sh
python app.py
```

## 📖 Usage
1. **Sign Up or Log In** to access the finance tracker.
2. **Add Income or Expenses** with details like category, amount, and date.
3. **View Transactions** with a summary of total income, expenses, and balance.
4. **Export Transactions** as a JSON file.
5. **(Optional) Check Currency Exchange Rates** using an API.

## 🔥 Example Usage
```sh
Welcome to Personal Finance Tracker!
1. Login
2. Sign Up
Enter choice: 2
Enter username: john_doe
Enter password: ********
Sign-up successful! Now login.
```

## 📌 Dependencies
- `Python 3.x`
- `requests` (for API calls)
- `json` (for data storage)

## ❗ Error Handling
- Invalid input formats
- Handling API failures
- Preventing duplicate users

## 🏆 Contribution
Feel free to fork the repository, create a new branch, and submit a pull request! 🚀

## 📜 License
This project is licensed under the **MIT License**.

---
👨‍💻 Developed by **Your Name** | [GitHub Profile](https://github.com/jsdevrazuislam)

