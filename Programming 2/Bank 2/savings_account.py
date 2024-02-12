from account import Account


class SavingsAccount(Account):
    def __init__(self, customer):
        super().__init__(customer)

    def transfer_to(self, account, sum):
        if (self.get_balance() < sum) or (self.get_balance() == 0):
            return False
        if account.get_customer().get_id() != self.get_customer().get_id():
            return False
        self.withdraw(sum)
        account.deposit(sum)
        return True
