'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character.
To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":
2*3 3*2 1*5 1*1 -> 23321511

Given a positive integer n, return the nth term of the count-and-say sequence.

https://leetcode.com/problems/count-and-say
'''

class Solution:
    def __init__(self):
        self.visited = dict()
        self.visited[1] = '1'
    
    def countAndSay(self, n: int) -> str:  
        if n in self.visited: return self.visited[n]

        def helper(num_str): # 12110            
            num_str += '0'
            ans = str()
            i = 1
            temp = 1
            while i < len(num_str):
                if num_str[i] != num_str[i-1]:
                    ans += (str(temp)+num_str[i-1]) # 111221
                    temp = 1
                else:
                    temp += 1
                i += 1
            return ans

        i = 2
        while i <= n:
            self.visited[i] = helper(self.visited[i-1])
            i += 1
        return self.visited[n]

# for test
sol = Solution()
print(sol.countAndSay(4))