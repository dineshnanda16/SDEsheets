class Solution:
    
    def repeatedNumber(self, A):
        ans = set()
        repeated = 0
        for i in A:
            if i in ans:
                repeated = i
            ans.add(i)
        
        l = len(A)
        sum_natural = l * (l + 1) // 2
        actual_sum = sum(ans)
        missing = sum_natural - actual_sum
        
        return [repeated,missing]