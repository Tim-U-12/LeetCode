import unittest

class TestCoinChange(unittest.TestCase):
    def testNorm(self):
        self.assertEqual(coinChange([1,2,5], 11), 3)

    def testNone(self):
        self.assertEqual(coinChange([2], 3), -1)

    def testAmountNone(self):
        self.assertEqual(coinChange([1], 0), 0)

def coinChange(coins: list[int], amount: int) -> int:
    minCoins = (amount + 1) * [float('inf')]
    minCoins[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                minCoins[i] = min(minCoins[i], minCoins[i-coin] + 1)

    return -1 if minCoins[amount] > amount else minCoins[amount]

def recursiveCoinChange(coins: list[int], amount: int) -> int:
    pass


if __name__ == "__main__":
    unittest.main()