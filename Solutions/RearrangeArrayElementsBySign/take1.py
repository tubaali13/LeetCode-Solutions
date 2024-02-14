class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        result = []
        positiveIndex = 0
        negativeIndex = 0

        for i in range(0, len(nums), 2):
            while(nums[positiveIndex] < 0 and positiveIndex < len(nums)):
                positiveIndex += 1
            while(nums[negativeIndex] >= 0 and negativeIndex < len(nums)):
                negativeIndex += 1
            result.append(nums[positiveIndex])
            positiveIndex += 1
            result.append(nums[negativeIndex])
            negativeIndex += 1
        
        return result

                
        