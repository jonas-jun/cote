'''
여러 번 매매를 할 수 있다고 할 때 최대 수익은?
한 시점에서 팔고 또 바로 살 수는 없다.
하나를 갖고 있는 상태에서 또 더 살 수는 없다.

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time.
You must sell before buying again.

sol_1은 재귀 방식
sol_2는 상승분들을 다 더해주는 방식 (이해가 필요함)
[1,2,3,4]에서 2에서 팔게 되면 2->3의 상승분은 벌지 못하게 되지만. 이 코드에서는 2->3 상승분도 더해줌. (1->3 상승분을 버는 것이라 생각)


https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
'''

def sol_1(prices): # wrong answer
    
    def helper(buy, start):
        nonlocal prices
        if start >= len(prices)-1:
            return max(0, prices[start] - prices[buy])

        for idx in range(start, len(prices)-1):
            if prices[idx] <= prices[buy]:
                buy = idx
            else:
                sell = (prices[idx]-prices[buy]) + helper(idx+1, idx+1)
                hold = helper(buy, idx+1)
                return max(sell, hold)
        
        return 0
    return helper(0, 0)

def sol_2(prices):
    ans = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            ans += prices[i]-prices[i-1]
    return ans


'''
한번의 매매로 최대로 낼 수 있는 이익은?
'''

def one_transaction(prices):

    buy = prices[0]
    profit = 0

    for idx in range(1, len(prices)):
        if prices[idx] <= buy:
            buy = prices[idx]
        else:
            profit = max(profit, prices[idx]-buy)
    
    return profit

# for test

from time_check import check
t1 = [7,1,5,3,6,4,5,8,7,9]
t2 = [1,2,3,4,5]
t3 = [7,6,4,3,1]
print('case 1')
print(check(sol_1, t1))
print(check(sol_2, t1))
print('case 2')
print(check(sol_1, t2))
print(check(sol_2, t2))
print('case 3')
print(check(sol_1, t3))
print(check(sol_2, t3))

print('one_transaction')
print(one_transaction(t1))
print(one_transaction(t2))
print(one_transaction(t3))