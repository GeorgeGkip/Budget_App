class Category:

    def __repr__(self):
        header = self.description.center(30, "*") + "\n"
        ledger = ""
        for item in self.ledger:
            line_descr = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            ledger += "{}{}\n".format(line_descr[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.balance)
        return header + ledger + total

    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.balance = 0.0

    def deposit(self, amount, description=""):
        self.ledger.append(
            {'"amount": {}, "description": {}'.format(amount, description)})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if amount >= self.balance:
            self.ledger.append({"amount": -amount, "description": description})
            self.balance += -amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, trnsf_cat_descr):
        if self.withdraw(amount, "Transfer to {}".format(trnsf_cat_descr.description)):
            trnsf_cat_descr.deposit(
                amount, "Transfer from {}".format(self.description))
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance > amount:
            return False
        else:
            return True


def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    total = round(sum(spent_amounts), 2)
    spent_perc = list(map(lambda amount: int((amount/total)*10)))