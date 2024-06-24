
usr = {"usr": "123"}
customer = {}


def main():
    while True:
        print("\n1.Login 2.Register 3.Exit ")

        try:
            choice = int(input(">>"))

        except ValueError:
            print("Error")

        else:
            match choice:
                case 1:
                    if login():
                        bank()

                case 2:
                    reg()

                case 3:
                    return

                case _:
                    print("Error!")


# Register
def reg():

    user_name = input("Username: ")
    password = input("Password: ")
    c_password = input("Confirm Password: ")

    if user_name not in usr:

        if password == c_password:
            usr.update({user_name: password})  # To register new user
            print("Success, please login.")
            return

        else:
            print("Passwords didn't match. Try again.")

    else:
        print("Username already exist.")


# Login
def login():
    user_name = input("Username: ")
    password = input("Password: ")

    if user_name in usr:
        if usr.get(user_name) == password:  # To login
            print("\nWelcome ", user_name)
            return 1

        else:
            print("Incorrect password.")

    else:
        print("Incorrect username.")


def bank():

    while True:
        print("\n1.Deposit. 2.Withdraw. 3.Balance 4.Logout")

        try:
            choice = int(input(">>>"))

        except ValueError:
            print("Error!")

        else:
            match choice:
                case 1:
                    deposit()

                case 2:
                    withdraw()

                case 3:
                    balance()

                case 4:
                    return

                case _:
                    print("Error!")


# Deposit
def deposit():
    try:
        ac_no = int(input("Account Number: "))
        cash = int(input("Amount: "))

    except ValueError:
        print("Invalid!")

    else:
        if ac_no in customer:

            customer[ac_no] = customer.get(ac_no) + cash
            print("Success")

        else:
            customer[ac_no] = cash
            print("Success")


# Withdrawal
def withdraw():
    try:
        ac_no = int(input("Account Number: "))
        cash = int(input("Amount: "))

    except ValueError:
        print("Invalid!")

    else:
        if ac_no in customer:
            if customer.get(ac_no) > cash:
                customer[ac_no] = customer.get(ac_no) - cash
                print("Success")

            else:
                print("Insufficient funds")

        else:
            print("Account number not found!")


# To check balance
def balance():
    try:
        ac_no = int(input("Account Number: "))

    except ValueError:
        print("Invalid!")

    else:
        if ac_no in customer:
            print("Balance: ", customer.get(ac_no))

        else:
            print("Account number not found!")


if __name__ == '__main__':
    main()
