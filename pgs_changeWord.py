'''
1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
begin -> target으로 이 조건에 맞는 변환이 이뤄지면서 바뀔 때 그 거리는?
못 바꾼다면 return 0

예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면
"hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

sol1
BFS를 돌리는데 level 단위로 체크할 수 있도록 구조 변환
sol2
DFS를 돌리고 target이 나올 때마다 모든 path들을 체크한 후 min을 return

https://programmers.co.kr/learn/courses/30/lessons/43163
'''

def sol1(begin, target, words):
    if target not in words: return 0
    
    # build graph
    def check(w1, w2):
        ans = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]: ans += 1
        return ans == 1

    from collections import defaultdict, deque
    words.append(begin)
    graph = defaultdict(lambda: list())
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            if check(words[i], words[j]):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
    # build visited
    visited = set()
    visited.add(begin)

    # queue를 level 단위로
    queue = deque([[begin]])
    level = list()
    while queue:
        cur = queue.popleft()
        togo = list()
        for w in cur:
            togo += graph[w] # 다음 레벨의 to리o들을 list에 모으고
        togo = list(set(togo))
        temp_level = [w for w in togo if w not in visited] # 실제 valid하게 갈 곳들만 남김
        for loc in temp_level:
            visited.add(loc) # 다음 level 갈 곳들을 visit 처리
        queue.append(temp_level) # 마찬가지로 level 단위(list)로 처리
        level.append(temp_level)
        if target in temp_level: return len(level) # 다음 level 갈 곳에 target이 있으면 length 뱉어내면서 끝

def sol2(begin, target, words):
    if target not in words: return 0
    # build graph
    def check(w1, w2):
        ans = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]: ans += 1
        return ans == 1
    from collections import defaultdict, deque
    words.append(begin)
    graph = defaultdict(lambda: list())
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            if check(words[i], words[j]):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
    
    path_list = list()
    visited = set()
    def dfs_helper(root, path, visited):
        nonlocal graph, path_list, target
        path.append(root)
        if root == target:
            return path_list.append(path)
        
        visited.add(root)
        togo = graph[root]
        for loc in togo:
            if loc not in visited:
                dfs_helper(loc, path[:], visited.copy())
                
    dfs_helper(begin, list(), set())
    return min(map(len, path_list))-1

# for test
t1_b, t1_t, t1_w = 'hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]
t2_b, t2_t, t2_w = 'hit', 'cog', ["hot", "dot", "dog", "lot", "log"]

print(sol1(t1_b, t1_t, t1_w))
print(sol1(t2_b, t2_t, t2_w))

print(sol2(t1_b, t1_t, t1_w))