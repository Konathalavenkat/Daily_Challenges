class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        d={0:1}
        res=0
        curr=0
        for i in arr:
            curr+=i
            if(curr-tar in d):
                res+=d[curr-tar]
            d[curr]=d.get(curr,0)+1
        return res