N = int(input())
M = list(map(int, input().split()))
low=1000000
high=-1
#더 간단한 방법 
#low =min(M)
#high= max(N)
#print(low*high)
if N==1:
    print(M[0]*M[0])
else:
    for i in range(N):
        if M[i] < low:
            low =M[i]
        if M[i]>high:
            high=M[i]
    print(low*high)


