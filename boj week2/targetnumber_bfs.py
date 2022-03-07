from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque() #queue 생성 왜 deque를 사용했는가? 깊이도 같이 큐에 저장?
    
    length = len(numbers)
    queue.append([-numbers[0], 0])  #+1 / depth (깊이) 처음 깊이는 0
    queue.append([+numbers[0], 0])  # -1 / depth  0
    
    while queue :
        num, depth = queue.popleft() # 큐에서 선입 선출 
        if depth+1 == length :  # 최하위 노드에서
            if num == target : answer += 1 # target 을 찾을시  answer +1
        else :
            queue.append([num - numbers[depth + 1], depth + 1])
            queue.append([num + numbers[depth + 1], depth + 1])
    
    return answer