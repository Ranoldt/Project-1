def stable_stock_matching(buyers_preferences, stocks_preferences):
    stable_buyers = {}
    stocks = list(stocks_preferences)

    while len(stocks) != 0:
        for stock in stocks[:]:
            for buyer in buyers_preferences:
                if buyer not in stable_buyers.values():
                    stable_buyers[stock] = buyer
                    stocks.remove(stock)
                    break
                else:
                    stable_stocks = {value: key for key, value in stable_buyers.items()}
                    if buyers_preferences[buyer].index(stock) < buyers_preferences[buyer].index(stable_stocks[buyer]):
                        stable_buyers[stock] = buyer
                        stocks.remove(stock)
                        stocks.append(stable_stocks[buyer])
                        break
    return stable_buyers


"""
Time Complexity: Answer ----- O(n^4) 
    Initialization
    -creating stable_buyers dictionary is O(1).
    -creating stocks list copy of stocks_preferences is O(n) because it is dependent on the length of the list.
    
    Loops
    -The while-loop is O(n) because it depends on the length of the stocks list.
    -The first for-loop is 2n, simplified to O(n) because it copies the stocks list and iterates over it, but Big-O notation looks overall complexity.
    -The second for-loop is O(n) because buyers_preferences is the same length as stocks list.
    
    Within the loops
    -The first if-statement 'if buyer not in stable_buyers.values()' is O(n) because it iterates to the length of stable_buyers.
    -when the if-statement is True, is O(n). The 'stocks.remove(stock)' is O(n) with the other two operations being O(1) constant time.
    -when the if-statement is False, the stable_stocks dictionary comprehension is O(n) because it iterates to the length of stable_buyers.
    -The second if-statement 'if buyers_preferences[buyer].index(stock) < buyers_preferences[buyer].index(stable_stocks[buyer])' is 2n, simplified to O(n) 
        because it iterates to the length of buyers_preferences for index.
    -The operations inside the second if-statement is O(n) because 'stocks.remove(stock)' is O(n) with the other three operations being O(1) constant time.
    
    Overall complexity:
    -The initialization is O(n+1) = O(n)
    -The loops are O(n) * O(n) * O(n) = O(n^3)
    -Within the loops are 5*O(n) = O(n)
    -Loops * Within the Loops + initialization = O(n^4) + O(n), which is simplified to O(n^4).
"""

"""
Space Complexity: Answer ------ O(n^2) - Assuming input lists are included, O(n) without input lists
    Input lists:
    -buyers_preferences is O(n^2) because n buyers has a list of n preferences.
    -stocks_preferences is O(n^2) because n stocks has a list of n preferences.

    Space:
    -stable_buyers dictionary is O(n) at the worst.
    -stocks list is O(n).
    -stable_stocks dictionary is created multiple times, but it is O(n) at the worst.
    Variables (stock, buyer) is O(1).
    
    Overall:
    -if input lists are included: O(n^2) + O(n^2) + O(n) + O(n) + O(n) + O(1) = O(n^2).
    -without input lists: O(n) + O(n) + O(n) + O(1) = O(n). 
"""

# Based on the complexity of the algorithm, I think the time and space complexity may not be the best, but it can
# be considered optimal because it is polynomial rather than exponentially growing, especially with the two input lists.
# Operating with two input lists designates at the very least O(n^2), especially when looping in between.
