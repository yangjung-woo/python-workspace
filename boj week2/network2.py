#n=3 computer [[1,1,0],[1,1,0],[0,0,1]]   return 2 연결된 네트워크 갯수
def solution(n, computers):
    temp = [] 
    for i in range(n):
        temp.append(i) # temp 에는 0 1 2 가 들어감
    for i in range(n):   #0 12
        for j in range(n): # i=0 /012 i=1 /012 i=2 /012
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:  #
                        temp[k] = temp[j]
    return len(set(temp))