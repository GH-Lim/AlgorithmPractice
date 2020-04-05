def solution(snapshots, transactions):
    answer = []
    accounts = {}
    is_checked = set()

    for account, money in snapshots:
        accounts[account] = int(money)

    for id, trans, account, money in transactions:
        if id not in is_checked:
            is_checked.add(id)
            money = int(money)
            if trans == 'SAVE':
                if account not in accounts:
                    accounts[account] = money
                else:
                    accounts[account] += money
            else:
                if account not in accounts:
                    accounts[account] = 0 - money
                else:
                    accounts[account] -= money
    for key, val in sorted(accounts.items()):
        answer.append([key, str(val)])

    return answer
a = [
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"],
  ["ACCOUNT10", "150"]
]

b = [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]

c = solution(a, b)

for i in c:
    q, w = i
    print(q, w)