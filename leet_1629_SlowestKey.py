'''
releaseTimes의 element들은 각 키의 떼는 시점.
가장 오래 눌려있었던 키를 찾아라.
같은 기간 눌려있었다면 larger character로.

Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
Output: "a"
Explanation: The keypresses were as follows:
Keypress for 's' had a duration of 12.
Keypress for 'p' had a duration of 23 - 12 = 11.
Keypress for 'u' had a duration of 36 - 23 = 13.
Keypress for 'd' had a duration of 46 - 36 = 10.
Keypress for 'a' had a duration of 62 - 46 = 16.
The longest of these was the keypress for 'a' with duration 16.

Sol.
단순히 max_val을 업데이트해가는 문제.
모든 duration을 담아서 정렬하지 않고 한번에 길이&캐릭터 모두 업데이트 하면서 O(n)으로 끝내기.

https://leetcode.com/problems/slowest-key
'''


from typing import List

def slowestKey(releaseTimes: List[int], keysPressed: str) -> str:
    max_dur = releaseTimes[0]
    max_key = keysPressed[0]

    for i in range(1, len(releaseTimes)):
        cur_dur = releaseTimes[i]-releaseTimes[i-1]
        if cur_dur > max_dur:
            max_dur = cur_dur
            max_key = keysPressed[i]
        elif cur_dur == max_dur:
            max_key = max(max_key, keysPressed[i])
        else: continue
    
    return max_key

# for test
t1 = [9,29,49,50]
t1_keys = 'cbcd'

t2 = [12,23,36,46,62]
t2_keys = 'spuda'

print(slowestKey(t1, t1_keys))
print(slowestKey(t2, t2_keys))
