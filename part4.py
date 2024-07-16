def stable_stock_matching(buyers_preferences, stocks_preferences):
    stable_stock = {}
    for i in buyers_preferences:
        for j in stocks_preferences:
            if i in stocks_preferences[j] and j in buyers_preferences[i]:
                if i not in stable_stock and j not in stable_stock.values():
                    stable_stock[i] = j
                    break
    return stable_stock

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
