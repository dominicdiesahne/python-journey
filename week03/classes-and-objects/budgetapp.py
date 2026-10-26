# Budget app from FreeCodeCamp.org
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        lines = ''
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"[:7]
            lines += f'{description:<23}{amount:>7}\n'
        total = f'Total: {self.get_balance():.2f}'
        return title + lines + total


def create_spend_chart(categories):
    spent = [
        sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        for cat in categories
    ]
    total_spent = sum(spent)
    percentages = [int(s / total_spent * 100) // 10 * 10 for s in spent]

    chart = 'Percentage spent by category\n'
    for level in range(100, -1, -10):
        chart += f'{level:>3}| '
        for pct in percentages:
            chart += 'o  ' if pct >= level else '   '
        chart += '\n'

    chart += '    ' + '-' * (3 * len(categories) + 1) + '\n'

    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    for i in range(max_len):
        chart += '     '
        for name in names:
            chart += (name[i] if i < len(name) else ' ') + '  '
        if i < max_len - 1:
            chart += '\n'

    return chart