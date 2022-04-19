# Coin Machine

#
# My solution for TopTal test:
#
den = (1.00, 0.50, 0.25, 0.10, 0.05, 0.01)

def getChange(money, price):

    if (price == money): return [0,0,0,0,0,0]

    change = round(money - price, 2)

    ret = [0,0,0,0,0,0]
    index = 0
    while (change > 0): #, index < len(den)):

        if (change < den[index]): 
            #print("skipping {}".format(den[index]))
            index += 1
            continue

        ret[index] += 1
        #print("ret = {}".format(ret))
        change = round(change - den[index], 2)
        #print("change = {}".format(change))

    print(list(reversed(ret)))

    return ret


#getChange(5, 0.99) # should return [1,0,0,0,0,4]
#getChange(3.14, 1.99) # should return [0,1,1,0,0,1]
#getChange(3, 0.01) # should return [4,0,2,1,1,2]
#getChange(4, 3.14) # should return [1,0,1,1,1,0]
#getChange(0.45, 0.34) # should return [1,0,1,0,0,0]


#
# Solution from https://blog.stevenlevithan.com/archives/change-dispenser
#

def getChange2(money, price):

    # Multiply by 100 to avoid floating point errors
    coins = (100, 50, 25, 10, 5, 1)

    if money == price or money < price: return None

    change = int((money*100-price*100))
    changeVec = []

    for coin in coins:
        numCoins = int(change / coin)
        change -= numCoins*coin
        print("change is {}".format(change))
        changeVec.append(numCoins)
    
    changeVec = list(reversed(changeVec))
    print(changeVec)
    return changeVec

getChange2(5, 0.99) # should return [1,0,0,0,0,4]
getChange2(3.14, 1.99) # should return [0,1,1,0,0,1]
getChange2(3, 0.01) # should return [4,0,2,1,1,2]
getChange2(4, 3.14) # should return [1,0,1,1,1,0]
getChange2(0.45, 0.34) # should return [1,0,1,0,0,0]