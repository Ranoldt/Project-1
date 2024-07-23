def stable_stock_matching(buyers_preferences, stocks_preferences):
    stable_buyers = {}
    buyers = list(buyers_preferences)

    while len(buyers) != 0:
        for i in buyers:
            for j in stocks_preferences:
                if j not in stable_buyers.values():
                    stable_buyers[i] = j
                    buyers.remove(i)
                    break
                else:
                    stable_stocks = {value: key for key, value in stable_buyers.items()}
                    if stocks_preferences[j].index(i) < stocks_preferences[j].index(stable_stocks[j]):
                        stable_buyers[i] = j
                        buyers.remove(i)
                        buyers.append(stable_stocks[j])
                        break
    stable_stocks = {value: key for key, value in stable_buyers.items()}
    return stable_stocks


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
