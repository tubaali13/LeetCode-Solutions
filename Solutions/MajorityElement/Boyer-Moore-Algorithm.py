class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        currentElement = -1

        for i in range(len(nums)):
            if(count == 0):
                currentElement = nums[i]
            if(nums[i] == currentElement):
                count = count + 1
            else:
                count = count-1
        return currentElement