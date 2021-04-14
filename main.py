class Budget:
    def __init__(self, account):
        self.account = account
        self.amount = 0

    def deposit(self, amount):
        self.amount += amount
        print(f'Deposit of {amount} naira is succcessful')

    def withdraw(self, amount):
        if amount > self.amount:
            print(f'insufficient funds available\n current balance is {self.get_balance()}')
            return
        else:
            self.amount -= amount
            print(f'Withdrawal of {amount} naira is succcessful')

    def get_balance(self):
        # print(f'Current account balance is {self.amount}')
        return self.amount

    def transfer_funds(self, amount, account):

        if amount > self.amount:
            print(f'Cannot complete transaction as {self.account} account has insufficient funds')
        else:
            print(f'Transfering {amount} naira from {self.account} to {account.account} account ....')
            self.amount -= amount
            account.amount = amount
            print("Transaction completed successfully")


def init():
    main_account.deposit(5000)

    print("Welcome to Budget App")
    print(f'Your main Account Balance is {main_account.get_balance()}')

    print()  # new line
    print("Please select an option:")
    print("\t1 - deposit funds")
    print("\t2 - withdraw from account")
    print("\t3 - Show Account Balance")
    print("\t4 - Transfer Funds to Account")
    selected_action = int(input('enter command:\t'))

    if selected_action == 1:
        deposit()

    elif selected_action == 2:
        withdraw()
    elif selected_action == 3:
        main_account.get_balance()
    elif selected_action == 4:
        transfer_funds()
    else:
        print("invalid action, please try again")


def deposit():
    dep_amount = int(input('Enter amount to deposit:\t'))
    if dep_amount < 1:
        print('invalid amount')
        return

    main_account.deposit(dep_amount)


def withdraw():
    main_account.withdraw(int(input('Enter amount to withdraw:\t')))


def transfer_funds():
    # create account to transfer funds
    account_name = input("enter name of new account:\t")
    account_name = Budget(account_name)
    print(f"Account {account_name.account} has been created sussefully")

    amount = int(input('enter amount to transfer:\t'))
    main_account.transfer_funds(amount, account_name)
    print(f"Balance of {account_name.account} is {account_name.get_balance()}")
    print(f"Balance of main account is {main_account.get_balance()}")


main_account = Budget('main')
init()
