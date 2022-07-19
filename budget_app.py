def truncate(n):
    multipler = 10
    return int(n * multipler) / multipler


def get_totals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawals()
        breakdown.append(category.get_withdrawals())
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded


def create_spend_chart(categories):
    result = 'Percentage spent by category \n'
    i = 100
    totals = get_totals(categories)
    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o  "
            else:
                cat_spaces += "   "
        result += str(i).rjust(3) + "|" + cat_spaces + ("\n")
        i -= 10

    dashes = "-" + "---"*len(categories)
    names = []
    x_axis = ""
    for category in categories:
        names.append(category.category)

    maxi = max(names, key=len)

    for x in range(len(maxi)):
        name_str = "      "
        for name in names:
            if x >= len(name):
                name_str += "   "
            else:
                name_str += name[x] + "  "

        if x != len(maxi) - 1:
            name_str += "\n"

        x_axis += name_str

    result += dashes.rjust(len(dashes) + 4) + "\n" + x_axis

    return result


class Category:

    def __init__(self, category):
        self.balance = 0
        self.ledger = []
        self.category = category

    def __str__(self):
        title = f'{self.category:*^30}\n'
        items = ''
        total = 0

        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + \
                f"{item['amount']:>7.2f}" + '\n'
            total += item['amount']

        output = title + items + 'Total: ' + str(total)
        return output

    def check_funds(self, amount):
        deposits = 0
        withdrawals = 0
        for item in self.ledger:
            if item['amount'] < 0:
                withdrawals += item['amount']
            else:
                deposits += item['amount']

        if amount + (-1 * withdrawals) > deposits:
            return False
        else:
            return True

    def get_balance(self):
        deposits = 0
        withdrawals = 0
        for item in self.ledger:
            if item['amount'] < 0:
                withdrawals += item['amount']
            else:
                deposits += item['amount']
        balance = deposits - (-1 * withdrawals)
        return balance

    def deposit(self, amount, description=''):
        self.balance += amount
        item = {'amount': amount, 'description': description}
        self.ledger.append(item)
        print(self.ledger)

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            item = {'amount': amount * -1, 'description': description}
            self.ledger.append(item)
            print(True)
            return True
        else:
            print(False)
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            payer_item = {'amount': amount * -1,
                          'description': f'Transfer to {category.category}'}
            self.ledger.append(payer_item)
            category.balance += amount
            payee_item = {'amount': amount,
                          'description': f'Transfer from {self.category}'}
            category.ledger.append(payee_item)
            print(True)
            return True
        else:
            print(False)
            return False

    # Spending chart
    def get_withdrawals(self):
        total_withdrawals = 0
        for item in self.ledger:
            if item['amount'] < 0:
                total_withdrawals += item['amount']
        return total_withdrawals


food = Category('Food')
clothing = Category('Clothing')
auto = Category('Auto')

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())

food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

categories = [food, clothing, auto]

print(create_spend_chart(categories))
