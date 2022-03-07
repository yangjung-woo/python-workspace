#n=3 computer [[1,1,0],[1,1,0],[0,0,1]]   return 2 연결된 네트워크 갯수

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]  # visited  초기화  방문 스택
    for start in range(n): # start 현재방문 노드 
        if visited[start] == False:
            DFS(n, computers, start, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer

def DFS(n, computers, start, visited):
    visited[start] = True
    for i in range(n):  # i= 0 1 2 
        if visited[i] ==False and computers[start][i] == 1: # 아직 방문 안한 노드 i 에서 computer와 연결되어 있을때 DFS(i탐색)
            visited= DFS(n,computers,i,visited)


    return visited

