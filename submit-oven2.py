h, m = map(int, input().split())
n = int(input())
h=h+n//60
m=m+n%60
if  m>=60:
     h=h+1
     m=m-60

if h>=24:
 h=h-24
print(h , m)
