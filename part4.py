def stable_stock_matching(buyers_preferences, stocks_preferences):
    stable_stock = {}
    for i in buyers_preferences:
        for j in stocks_preferences:
            if i in stocks_preferences[j] and j in buyers_preferences[i]:
                if i not in stable_stock and j not in stable_stock.values():
                    stable_stock[i] = j
                    break
    return stable_stock

"""
 x = list(buyers_preferences).copy()
    y = list(stocks_preferences).copy()
    length = len(buyers_preferences)
    new_dict = {}

    while len(new_dict) != length:
        for i in range(length):
            if x[i] == stocks_preferences[y[i]][0]:
                new_dict[x[i]] = y[i]
                del buyers_preferences[x[i]]
                del stocks_preferences[y[i]]
                for l in buyers_preferences:
                    buyers_preferences[l].remove(y[i])
                for w in stocks_preferences:
                    stocks_preferences[w].remove(x[i])

"""

"""
length = len(buyers_preferences)
new_dict = {}

while len(new_dict) != length:
    for i in list(buyers_preferences):
        for l in list(stocks_preferences):
            if i == stocks_preferences[l][0]:
                new_dict[i] = l
                del buyers_preferences[i]
                del stocks_preferences[l]
                for h in buyers_preferences:
                    buyers_preferences[h].remove(l)
                for k in stocks_preferences:
                    stocks_preferences[k].remove(i)
                break
"""

"""
new_dict = {}

for i in buyers_preferences:
    for j in stocks_preferences:
        if j not in new_dict.values():
            new_dict[i] = j
            break
        else:
            newer_dict = {value: key for key,value in new_dict.items()}
            if stocks_preferences[j].index(i) < stocks_preferences[j].index(newer_dict[j]):
                new_dict[i] = j
"""


if __name__ == '__main__':
    buyers_preferences = {
        'Buyer1': ['StockA', 'StockB', 'StockC'],
        'Buyer2': ['StockB', 'StockA', 'StockC'],
        'Buyer3': ['StockA', 'StockB', 'StockC']
        }

    stocks_preferences = {
        'StockA': ['Buyer1', 'Buyer2', 'Buyer3'],
        'StockB': ['Buyer2', 'Buyer1', 'Buyer3'],
        'StockC': ['Buyer1', 'Buyer2', 'Buyer3']
    }


    print(stable_stock_matching(buyers_preferences, stocks_preferences))
