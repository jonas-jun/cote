'''
코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

대기실은 5개이며, 각 대기실은 5x5 크기입니다.
거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

제한사항
places의 행 길이(대기실 개수) = 5
places의 각 행은 하나의 대기실 구조를 나타냅니다.
places의 열 길이(대기실 세로 길이) = 5
places의 원소는 P,O,X로 이루어진 문자열입니다.
places 원소의 길이(대기실 가로 길이) = 5
P는 응시자가 앉아있는 자리를 의미합니다.
O는 빈 테이블을 의미합니다.
X는 파티션을 의미합니다.
입력으로 주어지는 5개 대기실의 크기는 모두 5x5 입니다.

PSEUDO
[하나의 place를 체크하고 모든 place에 대해 답 구하기]
새로운 P에서 시작할 때 visited map을 매번 정의 정의 (X만 못 가도록) (def build_visited_map)
ans 1

dfs_helper(root, distance, first_check)
    nonlocal visited_map, ans, place
    place에서 'P'이고 첫 시작점이 아니면(first_check != 0):
        distance <=2 이면 ans = 0, return
    return

    togo는 0~4 가동 범위 내 + visited_map에서 False인 부분(O거나 P거나)
    for loc in togo:
        dfs_helper(loc, distance+1, first_check=1)

모든 p에서 시작해서 helper를 도는데 새로운 p에서 시작할 때마다 다시 visited map을 정의
ans==0으로 바뀌면 전체 함수 바로 return 0

https://programmers.co.kr/learn/courses/30/lessons/81302
'''

from typing import List
def solution(places: List[List]):

    def a_place(place):
        '하나의 대기실 체크'
        # 문제 생기면 바로 return 0
        ans = 1
        def build_visited():
            nonlocal place
            visited_map = [[False for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if place[i][j] == 'X':
                        visited_map[i][j] = True
            return visited_map
            

        def dfs_helper(root, distance, first_check):
            nonlocal place, visited_map, ans
            i, j = root[0], root[1]
            visited_map[i][j] = True
            if place[i][j] == 'P' and first_check != 0:
                if distance <= 2:
                    ans = 0
                return
            
            togo = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            def check_loc(loc):
                nonlocal visited_map
                i, j = loc[0], loc[1]
                if i < 0 or i > 4: return False
                if j < 0 or j > 4: return False
                if visited_map[i][j]:
                    return False
                return loc
            togo = list(map(check_loc, togo))

            for loc in togo:
                if loc:
                    dfs_helper(loc, distance+1, 1)
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    visited_map = build_visited()
                    dfs_helper((i,j), 0, 0)
                    if ans == 0:
                        return 0
        return 1
    
    return [a_place(place) for place in places]

# for test
t1 = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(t1))

# for insert mode