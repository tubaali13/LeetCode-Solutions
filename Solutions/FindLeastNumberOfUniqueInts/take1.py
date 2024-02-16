class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr.sort()

        countArr = []
        currElement = -1
        for i in range(len(arr)):
            if(currElement != arr[i]):
                countArr.append(1)
                currElement = arr[i]

            else:
                countArr[len(countArr)-1]+=1
        countArr.sort()
        for i in range(len(countArr)):
            if(k - countArr[i] >= 0):
                k -= countArr[i]
                countArr[i] = 0
                if(k == 0):
                    return len(countArr) - i - 1
            else:
                return len(countArr) - i 