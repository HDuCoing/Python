def makeTable(cur):
    table = []
    for nzd in range(10,101,10):
        row = [nzd]
        for currency in cur:
            currency_code = currency[0]
            exchange_rate = currency[1]
            amount = nzd*exchange_rate
            row.append(amount)
        table.append(row)
    return table


def printTable(currencies, table):
    
    codes = ["$NZ"] + [c[0] for c in currencies]
    print(*codes,sep=" \t")

    for row in table:
        cols = ["{:0.2f}".format(c) for c in row]
        print(*cols,sep=" \t")

        
            

            

cur = [['AUD', 0.96],['USD', 0.75],['Euro', 0.67],['GBP', 0.496]]
t = makeTable(cur)
printTable(cur, t)
