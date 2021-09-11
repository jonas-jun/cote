'''
오픈채팅방 구현
- log가 주어지면 들어왔습니다/나갔습니다 list 반환
- 최종적인 nickname을 사용하는데 nickname은 오픈챗을 나갔다가 다시 들어올 때, 그리고 변경했을 때 두 가지로 변경 가능

record	result
input: ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
return: ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

Solution
문자열 처리, Hash
1. 최종 {user: nickname} dict 만들기
2. 다시 loop을 돌면서 필요한 log들을 user dict 참고하여 구성

https://programmers.co.kr/learn/courses/30/lessons/42888
'''

def solution(record):
    users = dict()
    for rec in record:
        if rec.startswith('Leave'): continue
        users[rec.split()[1]] = rec.split()[2]
    
    answer = list()
    for rec in record:
        action, user = rec.split()[0], rec.split()[1]
        if action == 'Change': continue
        if action == 'Enter': answer.append('{}님이 들어왔습니다.'.format(users[user]))
        else: answer.append('{}님이 나갔습니다.'.format(users[user]))
    return answer

# for test
t1 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(t1))
