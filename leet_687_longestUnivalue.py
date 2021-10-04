'''
tree 내 같은 val을 가진 node 길이 중 가장 긴 길이를 찾아라

solution
특정 지점을 root로 하는 최대 길이를 파악
- left path + right path
left path와 right path를 각각 구해야 함
- subroot.left를 기준으로 왼쪽과 오른쪽 중 긴 쪽의 path 길이를 return
- 왼쪽 == subroot value가 같으면 +1 그렇지 않으면 0
helper함수 내에서 한번씩 max를 체크 (각 지점을 root node로 해서) -> max(max_len, left+right)

https://leetcode.com/problems/longest-univalue-path/submissions
'''

def longestUnivalPath(root) -> int:
    max_len = 0
    def helper(subroot):
        nonlocal max_len
        if not subroot: return 0
        left_len = helper(subroot.left)
        right_len = helper(subroot.right)
        if subroot.left and subroot.left.val == subroot.val: left_len += 1
        else: left_len = 0
        if subroot.right and subroot.right.val == subroot.val: right_len += 1
        else: right_len = 0

        max_len = max(max_len, (left_len+right_len)) # 각 노드를 root로 해서 최대 길이 체크해줘야 함!
        return max(left_len, right_len) # return 값은 외쪽 오른쪽 중 긴 쪽만
    helper(root)
    return max_len