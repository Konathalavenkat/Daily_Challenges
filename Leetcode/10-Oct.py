class Solution(object):
    def maxWidthRamp(self, nums):
        mono=[]
        def getmaxramp(i):
            l,r=0,len(mono)-1
            # print(l,r,r==-1,[nums[i] for i in mono])
            if(r==-1 or nums[mono[r]]>nums[i]):
                mono.append(i)
                return 0
            while(l<=r):
                mid=(l+r)//2
                if(nums[mono[mid]]<=nums[i]):
                    r=mid-1
                else:
                    l=mid+1
            # print(i,mono,(r+1))
            return i-mono[r+1]
        res=0
        n=len(nums)
        for i in range(n):
            res=max(res,getmaxramp(i))
        return res
            
        