class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        elementcount = Counter(nums)
        
        majority_elements = []
        l = len(nums) // 3
        for element, count in elementcount.items():
            if count > l:
                majority_elements.append(element)    
        return majority_elements