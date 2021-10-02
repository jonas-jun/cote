# leet_111. minimum depth
def minDepth(root):
    if not root: return 0
    ans = float('inf')
    def dfs_helper(start, depth):
        nonlocal ans
        if not start: return
        depth += 1
        if not start.left and not start.right:
            ans = min(ans, depth)
            return
        dfs_helper(start.left, depth)
        dfs_helper(start.right, depth)
    dfs_helper(root, 0)
    return ans

# leet_104, maximum depth
def maxDepth(root):
    if not root: return 0
    ans = 0
    def dfs_helper(start, depth):
        nonlocal ans
        if not start: return
        depth += 1
        if not start.left and not start.right:
            ans = max(ans, depth)
            return
        dfs_helper(start.left, depth)
        dfs_helper(start.right, depth)
    dfs_helper(root, 0)
    return ans

