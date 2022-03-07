
def building_count_left (i): #기울기가 작을때 count ++

    lowest_inc=1000000 
    count= 0
    j= i-1
    while j>=0:
        dx = i-j
        dy = building[i] - building[j]
        dydx = dy/dx

        #if (building[i]-building[j]/i-j) <lowest_inc:
        if dydx < lowest_inc:
            count+=1
            lowest_inc=dydx
        j=j-1
    return count


def building_count_rignt(i):#기울기가 클때 count ++
    highest_inc= -1000000
    count=0
    j=i+1
    while j<N:
        dx = j-i
        dy = building[j] - building[i]
        dydx = dy/dx
        #if (building[j]-building[i]/j-i) >highest_inc:
        if dydx> highest_inc:
            count+=1
            highest_inc=dydx
        j=j+1
    return count

N= int(input())
building = list(map(int, input().split()))
max_t=0
idx=0
for i in range(N):
   left=building_count_left(i)
   right=building_count_rignt(i)
   total=left+right
   if max_t<total:
       max_t=total
       idx=i
print(max_t)


