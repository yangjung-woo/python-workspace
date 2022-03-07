def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == False:
            BFS(n, computers, i, visited)
            answer += 1
    return answer

def BFS(n, computers, start, visited):
    visited[start] = True
    queue = []   #방문기록용 queue 선언    ex) queue={0 1 2}  0,1,2를 방문 했다
    queue.append(start)     # 현재 시작 노드 번호를 queue 에 저장 
    while len(queue) != 0: #방문 기록이 있다면 
        start = queue.pop(0)   
        visited[start] = True
        for connect in range(n): # 주변 컴퓨터들이랑 연결 되어있는지 탐색 
            if connect != start and computers[start][connect] == 1:  # 자신이 아닌 다른 컴퓨터와 연결되어있다 
                if visited[connect] == False: #게다가 아직 방문 안한 노드이다
                    queue.append(connect) # 방문기록에 저장 