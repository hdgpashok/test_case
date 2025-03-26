from task_A import get_balance

def get_balance_batch():
    res = []
    with open('wallets.txt', 'r') as f:
        for line in f.readlines():
            res.append(get_balance(line.strip()))
    return res
