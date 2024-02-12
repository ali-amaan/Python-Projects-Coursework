class Account:
    def __init__(self, customer):
        self.__customer = customer
        self.__balance = 0

    def get_customer(self):
        return self.__customer

    def get_balance(self):
        return self.__balance

    def deposit(self, sum):
        self.__balance += sum

    def withdraw(self, sum):
        if self.__balance >= sum:
            self.__balance = self.__balance - sum
            return True
        return False

    def transfer_to(self, account, sum):
        return False
        # if (self.__balance < sum) or (self.__balance == 0):
        #     return False
        # self.__balance = self.__balance - sum
        # account.deposit(sum)
        # return True
