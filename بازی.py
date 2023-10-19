S = int(input())
A = list(map(int, input().split()))
main_list = []
for i in range(S):
    if i % 2 == 0:
        s = max(A)
        main_list.append(s)
        A.remove(s)
    else:
        d = min(A)
        main_list.append(d)
        A.remove(d)
print(' '.join(map(str, main_list)))
