'''
graph가 주어졌을 때, strong한 graph인지 판단(strong: 모든 노드들이 연결되어 있는지?)
color 이용
'''

def strong(G):

    def dfs_helper(root):
        nonlocal G
        if root.color == 'r': return
        root.color = 'r'
        for node in G[root]:
            dfs_helper(node)
    
    for node in G:
        if node.color != 'r' and G[node]:
            dfs_helper(node)

    ans = 1
    for node in G:
        if node.color == 'g': ans = 0
    return ans

class Node:
    def __init__(self, id, color='g'):
        self.id = id
        self.color = color

g1, g2, g3, g4, g5 = Node(1), Node(2), Node(3), Node(4), Node(5)

G = dict()
G[g1] = [g2, g3]
G[g2] = []
G[g3] = [g4]
G[g4] = [g3, g2]
G[g5] = []
print(strong(G))