class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summax = float('-inf')
        current_sum = 0

        for i in nums:
            current_sum += i

            if current_sum > summax:
                summax = current_sum

            if current_sum < 0:
                current_sum = 0

        return summax
