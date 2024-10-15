class Solution:
    def minimumSteps(self, s: str) -> int:
        res=0
        ones=0 
        for i in s:
            if(i=='1'):
                ones+=1
            else:
                res+=ones
        return res