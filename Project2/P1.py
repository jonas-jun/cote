"""
**Instruction**
Please see instruction document.

"""
import re

def P1(path: str):
    '''
    1. 모든 '//'를 '/'로 바꾼다.
    2. '/'기준으로 split
    3. stack을 만들어서 붙여주고, ..가 나오면 하나를 제거한다.(stack이 비어있지 않은 경우에만) .이 나오면 continue
    4. 마지막에 '/'를 join하여 stack --> str을 만들고 앞에 '/'을 붙여서 return
    '''

    path = re.sub('//', '/', path)
    path = path.split('/')
    stack = list()
    for p in path:
        if not p: continue
        if p == '.': continue
        if p != '..':
            stack.append(p)
        else:
            if stack: stack.pop()
    return '/'+'/'.join(stack)

print(P1('/home//foo/'))
print(P1('/a/./b/../../c/'))