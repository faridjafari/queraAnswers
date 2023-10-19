S = list(map(int, input().split()))
A = list(map(int, input().split()))
n = S[0]
k = S[1]
j = max(A)
C = j - k
count = 0
for i in range(n):
    if A[i] < C:
        current_count = C - A[i]
        count += current_count
    else:
        pass
print(count)
