import auth

def main():
    while True:
        print("💰 Welcome to Personal Finance Tracker!  ")
        
        if auth.logged_in_user: 
            print("1️⃣ Transactions Dashboard") 
            print("2️⃣ Logout")
            choose = input("Enter your choose: ")

            match choose:
                case '1':
                    auth.transactions.run_transactions()
                case '2':
                    auth.logout()
                case _:
                    print("❌ Invalid choice! Try again.")
        else:
            print("1️⃣ Register")
            print("2️⃣ Login")
            print("3️⃣ Exit")
            choose = input("Enter your choose: ")

            match choose:
                case '1':
                    auth.register()
                case '2':
                    auth.login()
                case '3':
                    break
                case _:
                    print("❌ Invalid choice! Try again.")


if __name__ == '__main__':
    main()