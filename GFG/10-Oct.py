class Solution:
    def maxDistance(self, arr):
        d={}
        res=0
        for i,val in enumerate(arr):
            if(val in d):
                res=max(res,i-d[val])
            else:
                d[val]=i
        return res