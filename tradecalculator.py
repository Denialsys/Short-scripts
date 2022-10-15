def calcBeta():
    buyFeePer = .001
    sellFeePer = .001
    cost = 0
    profit = 0
    entry = 0
    while(entry != 9999):
        try:
            entry = float(input("entry price: "))
            buyFee = entry*(1 - buyFeePer)
            sellFee = 1
        except Exception as e:
            print (f'Error calculating: {e.args}')

def calc():
    buyFeePercent = 0.0012
    sellFeePercent = .001
    profitPercent = .001
    profitPercent2 = .1
    cutLossPercent = .01
    entry = 0
    
    print(f'Parameters are as follows:')
    print(f'Buy Fee: {buyFeePercent * 100}%')
    print(f'Sell Fee: {sellFeePercent * 100}%')
    print(f'Profit target: {profitPercent * 100}%')
    print(f'Profit target 2: {profitPercent2 * 100}%')
    print(f'Cut target: {cutLossPercent * 100}% \n')
    
    while(entry != 9999):
        try:
            entry = float(input("entry price: "))
            buyFee = entry * buyFeePercent
            entry = entry - buyFee
            sellFee = (entry * (1 + profitPercent))* sellFeePercent
            sellFee2 = (entry * (1 + profitPercent2))* sellFeePercent
            profit = (entry * (1 + profitPercent)) - sellFee
            profit2 = (entry * (1 + profitPercent2)) - sellFee2
            cutLoss = entry * (1 - cutLossPercent)
            print(f'target price 1: {round(profit, 5)}')
            print(f'target price 2: {round(profit2, 5)}')
            print(f'cut loss price: {round(cutLoss, 5)}')
            print(f'Fee : {buyFee}')
            print(f'Fee 2: {sellFee2}\n\n')
        except Exception as e:
            print (f'Error calculating: {e.args}')

calc()
