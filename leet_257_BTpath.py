'''
all root-to-leaf paths in any order

solution
path에 본인을 append한 후
leaf를 판단할 수 있는 기준: left, right children이 모두 없다면 path를 추가
left가 있다면 helper(left, path[:])
right가 있다면 helper(right, path[:])
'''

def binaryTreePaths(root):
    ans = list()
    def dfs_helper(root1, path):
        nonlocal ans
        path.append(root1.val)
        if not root1.left and not root1.right:
            ans.append(path)
            return
        if root1.left:
            dfs_helper(root1.left, path[:])
        if root1.right:
            dfs_helper(root1.right, path[:])
    dfs_helper(root, list())
    return ['->'.join(list(map(str, path))) for path in ans] # 정답의 형태 ['1->3->5', '1->4']