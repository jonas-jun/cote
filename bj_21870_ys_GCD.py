'''
def 최대공약수

if 길이가 1이면 return 그대로 (재귀 끝)
if 길이가 2이면 return 둘의 합

최대공약수(list[:mid]) + 재귀함수(list[mid:])과 재귀함수(list[:mid]) + 최대공약수(list[mide:]) 중 큰 쪽을 return
'''
from math import gcd
import sys

def custom_gcd(list1):
    start = list1[0]
    for i in range(1, len(list1)):
        start = gcd(start, list1[i])
    return start

def sol(list1):
    
    def helper(list2):
        if len(list2) == 1:
            return list2[0]
        if len(list2) == 2:
            return sum(list2)
        mid = len(list2)//2
        left_gcd, right_gcd = custom_gcd(list2[:mid]), custom_gcd(list2[mid:])
        return max((left_gcd + helper(list2[mid:])), (helper(list2[:mid]) + right_gcd))
        
    return helper(list1)

n = int(input())
input_list = list(map(int, sys.stdin.readline().split()))
print(sol(input_list))

# for insert mode