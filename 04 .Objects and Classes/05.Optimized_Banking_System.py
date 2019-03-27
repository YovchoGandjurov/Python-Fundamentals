class BankAccount:
    def __init__(self, bank, accountName, accountBalance):
        self.bank = bank
        self.accountName = accountName
        self.accountBalance = accountBalance

accounts = []
inp = input()

while inp != "end":
    data = inp.split(" | ")
    curr_account = BankAccount(data[0], data[1], float(data[2]))
    accounts.append(curr_account)

    inp = input()

sorted_acc = sorted(accounts, key=lambda order: (-order.accountBalance,
                                                 len(order.bank)))

for item in sorted_acc:
    print(f"{item.accountName} -> {item.accountBalance:.2f} ({item.bank})")
