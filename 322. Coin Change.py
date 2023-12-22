import unittest

class TestCoinChange(unittest.TestCase):
    def testNorm(self):
        self.assertEqual(coinChange([1,2,5], 11), 3)

    def testNone(self):
        pass

    def testAmountNone(self):
        pass

def coinChange(coins: list[int], amount: int) -> int:
    # Init
    minCoins = [amount + 1] * (amount + 1)

    minCoins[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)
    
    if minCoins[amount] > amount:
        return - 1
    
    return minCoins[amount]



if __name__ == "__main__":
    unittest.main()