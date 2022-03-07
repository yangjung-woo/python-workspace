answer = 0
#number
def DFS(idx, numbers, target, value): 
    global answer # answer 을 전역변수로 선언
    N = len(numbers)  
    if (idx==N):  # 최 하위 노드에 도착!
        if(target==value): # 찾았다! 
            answer+=1  #  +1
            return
        else:
            return    # 없는데요?  그냥 종료

    DFS(idx+1,numbers,target,value+numbers[idx]) # +1 즉 왼쪽으로
    DFS(idx+1,numbers,target,value-numbers[idx])# -1 즉 오른쪽으로 
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer