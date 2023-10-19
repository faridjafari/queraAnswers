N = int(input())
factorial = 1
for i in range(1, N):
    if N == 0:
        print(1)
    else: 
        factorial += factorial * i
print(factorial)
