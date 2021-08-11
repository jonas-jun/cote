'''
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system,
convert it to the simplified canonical path.
In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level,
and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem,
any other format of periods such as '...' are treated as file/directory names.

Input: path = "/home/"
Output: "/home"

Input: path = "/a/./b/../../c/"
Output: "/c"

PSEUDO
deque를 사용
/로 split 후 각 dir에 loop:
    '.'이거나 아무것도 없을 때는 continue
    '..'일 때는 deque.pop()
    나머지는 deque.append()

'/' + '/'.join(deque)를 return
'''

from collections import deque
def sol_1(path: str):
    pool = path.split('/')
    queue = deque()
    for dir in pool:
        if not dir: continue
        if dir == '.': continue
        if dir == '..':
            if queue: queue.pop()
            else: continue
        else: queue.append(dir)

    return '/' + '/'.join(queue)


# for test
t1 = "/home//foo/"
t2 = "/a/./b/../../c/"
t3 = "/../"
t4 = "/a//b////c/d//././/.."

print(sol_1(t1))
print(sol_1(t2))
print(sol_1(t3))
print(sol_1(t4))

# for insert mode