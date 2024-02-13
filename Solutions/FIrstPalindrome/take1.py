class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for word in words:
            count = 0
            for index in range(int(len(word)/2)):
                if(word[index] == word[len(word) - index  - 1]):
                    count += 1
                else:
                    break
            print(count)
            if(int(len(word)/2) == count):
                return word
        return ""
