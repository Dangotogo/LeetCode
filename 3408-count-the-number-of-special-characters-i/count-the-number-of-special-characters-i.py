class Solution:
    def numberOfSpecialChars(self, word):
        st = set(word)

        count = 0

        for ch in range(ord('a'), ord('z') + 1):
            lower = chr(ch)
            upper = chr(ch).upper()

            if lower in st and upper in st:
                count += 1

        return count