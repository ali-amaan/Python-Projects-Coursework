from personal_account import PersonalAccount
from savings_account import SavingsAccount


class Bank:
    def __init__(self, name):
        self.__name = name
        self.__customers = []
        self.__accounts = []

    def get_name(self):
        return self.__name

    def get_customers(self):
        return self.__customers

    def get_customers_by_name(self, name):
        search_result = []
        for customer_instance in self.__customers:
            if customer_instance.get_name() == name:
                search_result.append(customer_instance)
        return search_result

    def get_customer_by_id(self, id):
        for customer_instance in self.__customers:
            if customer_instance.get_id() == id:
                return customer_instance

    def add_savings_account(self, customer):
        if customer in self.__customers:
            new_account = SavingsAccount(customer)
            self.__accounts.append(new_account)
            return new_account
        return None

    def add_personal_account(self, customer):
        if customer in self.__customers:
            new_account = PersonalAccount(customer)
            self.__accounts.append(new_account)
            return new_account
        return None

    def add_customer(self, customer):
        if customer not in self.__customers:
            self.__customers.append(customer)

    def remove_customer(self, customer):
        for customer_instances in self.__customers:
            if customer_instances == customer:
                self.__customers.remove(customer_instances)

    def get_accounts(self, customer):
        accounts_list = []
        for account_instance in self.__accounts:
            if account_instance.get_customer() == customer:
                accounts_list.append(account_instance)
        return accounts_list
