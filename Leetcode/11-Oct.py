class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arr=[]
        for i,val in enumerate(times):
            arr.append([val[0],1,i])
            arr.append([val[1],0,i])
        arr.sort()
        seats=[i for i in range(len(times))]
        heapq.heapify(seats)
        d={}
        for time,Or,friend in arr:
            if(friend==targetFriend):
                return heapq.heappop(seats)
            elif(Or==1):
                d[friend]=heapq.heappop(seats)
            else:
                heapq.heappush(seats,d[friend])
        return -1