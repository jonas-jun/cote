'''
두 개의 맛을 조합해서 주어진 가격대를 맞추고 그 index를 오름차순으로 return

[2,1,3,5,6], money= 5
return 1, 3

Solution
(0,2), (1,1), (2,3)...으로 enumerate 후 값 기준으로 sort
양 끝에 두 개의 포인터를 두고 가운데로 좁혀가면서 합을 search

https://www.hackerrank.com/challenges/ctci-ice-cream-parlor
'''

def whatFlavors(cost, money):
    cost = sorted(enumerate(cost), key=lambda x:x[1])
    left, right = 0, len(cost)-1
    while left < right:
        cur = cost[left][1] + cost[right][1]
        if cur == money:
            ans = sorted([cost[left][0]+1, cost[right][0]+1]) # flavor starts from 1
            return ' '.join(list(map(str, ans)))
        elif cur > money: right -= 1
        else: left += 1

# for test
t1 = [1,4,5,3,2]
print(whatFlavors(t1, 4))
t2 = [7, 2, 5, 4, 11]
print(whatFlavors(t2, 12))