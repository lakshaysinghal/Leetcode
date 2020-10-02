class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        int_max = 2**31
        numCoins = [0]+[int_max]*(amount)
        
        for coin in coins:
            if coin < amount:
                numCoins[coin]=1
        for i in range(1,amount+1):
            for coin in coins:
                if coin < i:
                    numCoins[i]=min(numCoins[i],1+numCoins[i-coin])
            
        return numCoins[amount] if numCoins[amount]!=int_max else -1

'''
Time    - O(amount*N)
Space   - O(amount)
'''