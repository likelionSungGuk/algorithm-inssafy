# string = list(input())
#
# N = len(string)
# flag = 0
# def mike(k):
#     global flag
#     if k == N-1:
#         if flag == 0:
#             print(string[k], end=" ")
#             flag = 1
#         if flag == 1 and k != 0:
#             k -= 1
#             mike(k)
#         else:
#             return
#     else:
#         if flag == 0:
#             print(string[k], end=" ")
#             mike(k+1)
#         else:
#             print(string[k], end=" ")
#             k -= 1
#             if k == 0:
#                 print(string[k], end=" ")
#                 return
#             else:
#                 mike(k)
#
# mike(0)

#####4. 주사위 #####

# def perm(n, k):
#     if n == k:
#         print(bit)
#     else:
#         bit[k] = 6
#         perm(n, k + 1)
#         bit[k] = 5
#         perm(n, k + 1)
#         bit[k] = 4
#         perm(n, k + 1)
#         bit[k] = 3
#         perm(n, k+1)
#         bit[k] = 2
#         perm(n, k+1)
#         bit[k] = 1
#         perm(n, k+1)
#
#
# n = 3
# bit = [0]*n
# perm(n, 0)
import math
pi = math.pi

print(pi)
print(180/pi)