import math

# n = list(input())
# s = 0
# ai = list(map(int, input().split()))
# s = len(ai) - 1
# if int(ai[0]) > 1:
#     s = -1
# print(s)

n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(1, n+1):
    y = [round(math.dist((n, k), (i, i+1)))]
    print(''.join(map(str, y)), end=" ")



