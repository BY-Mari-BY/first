import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('5_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, loss = line.split()
        profit[name] = int(earning) - int(loss)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Average profit - {prof_aver:.2f}')
    else:
        print(f'Average profit - None.')
    pr = {'Average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Each companys profit - {profit}')

with open('5_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)


