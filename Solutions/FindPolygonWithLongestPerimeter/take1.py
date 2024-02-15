class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort() 
        perimeter = 0
        temp_sum = nums[0] + nums[1]

        for i in range(2, len(nums)):
            if temp_sum > nums[i]:
                if temp_sum + nums[i] > perimeter:
                    perimeter = temp_sum + nums[i]
            temp_sum += nums[i]

        return perimeter if perimeter != 0 else -1