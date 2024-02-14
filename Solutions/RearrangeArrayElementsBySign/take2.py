class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = [num for num in nums if num >= 0]
        negatives = [num for num in nums if num < 0]

        result = []
        for pos, neg in zip(positives, negatives):
            result.extend([pos, neg])

        return result
