
def dfs(computers, visited, start):
        stack = [start]
        while stack:  # 탈출 언제? 더이상 연결한된 노드가 없다면 
            j = stack.pop() # 가장최근 방문한 노드 stack 에서 pop 
            if visited[j] == 0:  #j 를 방문을 안했어용 
                visited[j] = 1   # j는 이제 방문했다
            # 모든컴퓨터 연결을 탐색하며 만약 s방문하지 않았다면 stack에 추가 
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:  # 방문안햇는데 연결이 되어있다??
                    stack.append(i) # 스택에 추가 

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    
    for i in range(n):
        if visited[i] ==0: ## 방문하지 않았을때 
            dfs(computers, visited, i) # 만약 더이상 연결된 node가 없어서 백트래킹 될때 종료  
            answer +=1 
        i+=1
        #방문 했던 노드이면 실행 종료  
    return answer