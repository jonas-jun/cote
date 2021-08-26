'''
1/2 -> 0.5
2/3 -> 0.(6) 반복되는 부분은 () 처리

나누어 떨어질 때까지. (divmod 나머지가 0인지?)
몫은 답에 추가, 나머지는 *10 을 해줘서 다음 자리 계산으로
나눠야 하는 수의 반복이 발생하는지? 체크

https://leetcode.com/problems/fraction-to-recurring-decimal/
'''
def fractionToDecimal(numerator: int, denominator: int) -> str:
    # 부호 체크
    if numerator == 0: return '0'
    minus = False
    if numerator * denominator <0:
        minus = True
    numerator = abs(numerator)
    denominator = abs(denominator)
    
    ans = list()
    check = dict() # 반복 체크
    i = 0 # 반복 체크할 때 자리수 알아둬야 하기 때문에
    rep = False # 반복되니?
    
    while numerator > 0:
        i += 1
        a, b = divmod(numerator, denominator)
        ans.append(a)
        if not b: # 나누어 떨어진다면
            break
        if (b*10) in check: # 반복되는 경우 반복의 시작점 알아두고 break
            rep = check[b*10]
            break
        check[b*10] = i
        numerator = b*10
    
    ans = list(map(str, ans))        
    ans = '{}.{}'.format(ans[0], ''.join(ans[1:])) if not rep else '{}.{}({})'.format(ans[0], ''.join(ans[1:rep]), ''.join(ans[rep:]))
    ans = ans if ans[-1] != '.' else ans[:-1] # 3. 으로 끝나면 . 제거 후 출력
    return ans if not minus else '-'+ans

# for test
print(fractionToDecimal(10, 3))
print(fractionToDecimal(-4, 2))