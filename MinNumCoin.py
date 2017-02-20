import sys

def DPChange(money, coins):
    minNumCoins = [sys.maxsize]*(money+1)
    minNumCoins[0] = 0
    for m in range(1, money+1):
        for i in range(0, len(coins)):
            if m >= coins[i]:
                if minNumCoins[m-coins[i]] + 1 < minNumCoins[m]:
                    minNumCoins[m] = minNumCoins[m-coins[i]] + 1
    return minNumCoins[money]

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        money = int(f.readline())
        coins = f.readline().split(',')
        coins = [int(c) for c in coins]

        minNumCoins = DPChange(money, coins)
        print(minNumCoins)