from collections import defaultdict
from typing import List

def P1(nums: List, k: int):
    if sum(nums)%k != 0: return False
    
    counter = defaultdict(lambda: 0)
    for num in nums:
        counter[num % k] += 1
    if counter[0] % 2 != 0: return False
    if k % 2 == 0:
        if counter[k/2] % 2 != 0: return False
        for i in range(1, k//2):
            if counter[i] != counter[k-1]: return False
    else:
        for i in range(1, k//2+1):
            if counter[i] != counter[k-i]: return False

    return True
    
test1 = [123, 36, 54, 28, 39, 28]
test2 = [3,7,6,5,4,5]

print(P1(test1, 2))
print(P1(test2, 5))