import os
import sys
#import csv
import json

current_dir =os.path.dirname(os.path.abspath(sys.argv[0]))
#csv_file = os.path.join(current_dir,"bank_accounts.csv")
json_file = os.path.join(current_dir,"bank_accounts.json")

class BankAccount:
    def __init__(self, account_number, account_name, balance):
        self._account_number = account_number
        self._account_name = account_name
        #self.set_balance(balance)
        self.balance = balance
        #self.balance
    
    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance
    

    def withdraw(self,amount):
        if 0<= amount <= self._balance :
            self._balance -= amount
        else:
            print("Không đủ số dư để rút")


    def deposit(self, amount):
        if amount > 0:
            self._balance +=  amount
        else:
            print('Phải nạp số tiền lớn hơn 0')

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        if new_balance <0:
            print("Số dư không hợp lệ")

    def display(self):
        print(f" {self.account_number}             {self.account_name}        {self.balance}")

    @classmethod
    def from_json(cls, json_file):
        account = []
        with open(json_file) as file:
            data = json.load(file)
            for i in data:
                b = BankAccount(i['account_number'],i['account_name'],i['balance'])
                account.append(b)
        return account
json_accounts = BankAccount.from_json(json_file)
#print(f"{'Number' :9} {'name' :15} {'Balance':>15}")
print(f"| {'Number':9} | {'Account Name':15} | {'Balance':15} |")
print(f"|{'-' * 11}|{ '-' * 17 }|{'-' * 17}|")
for account in json_accounts:
    account.display()