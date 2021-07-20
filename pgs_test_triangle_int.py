'''
Programers level test
Question & Solution

input: n = 4

[1]
[2,9]
[3,10,8]
[4,5,6,7]

return [1,2,9,3,10,8,4,5,6,7]

https://velog.io/@jonas-jun/pgs%EC%82%BC%EA%B0%81%ED%98%95%EB%B0%B0%EC%B9%98
'''

def sol(n):

    tri = list()
    for i in range(1, n+1):
        tri.append([False]*i)

    num = 1
    i, j = 0, 0
    for k in range(n, 0, -3):
        if k >= 1:
            for _ in range(k):
                tri[i][j] = num
                num += 1
                i += 1
        i -= 1 
        j += 1
        if k-1 >= 1:
            for _ in range(k-1): 
                tri[i][j] = num
                num += 1
                j += 1
        i -= 1
        j -= 2 
        if k-2 >= 1:
            for _ in range(k-2): 
                tri[i][j] = num
                num += 1
                i -= 1
                j -= 1
        i += 2
        j += 1
    
    ans = list()
    for list1 in tri:
        ans += list1
    return ans

print(sol(4))
print(sol(6))