class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        longest = 1
        for i in range(len(s)):
            words = set()
            for j in range(len(s)-i):
                if s[j] in words:
                    longest = len(words) if len(words) > longest else longest
                    break
                words.add(s[j])
            longest = len(words) if len(words) > longest else longest
        return longest

    def lengthOfLongestSubstring_v2(self, s):
        i = 0
        longest = 1
        index = dict()
        while i<len(s):
            if s[i] not in index.keys():
                index[s[i]] = i
                i = i + 1
            else:
                longest = len(index) if len(index) > longest else longest
                i = index[s[i]] + 1
                index.clear()
        longest = len(index) if len(index) > longest else longest
        return longest

    def lengthOfLongestSubstring_v3(self, s):
        if not s:
            return 0
        index = dict()
        index[s[0]] = 0
        i = 1
        j = 0
        max_len = 1
        while i<len(s):
            if s[i] in index and j <= index[s[i]]:
                if i-j > max_len:
                    max_len = i-j
                j = index[s[i]] + 1
            index[s[i]] = i
            i = i + 1
        if i-j > max_len:
            max_len = i-j
        return max_len

def main():
    solution = Solution()
    words = 'abcdefghijkabc'
    print solution.lengthOfLongestSubstring(words)
    print solution.lengthOfLongestSubstring_v2(words)
    print solution.lengthOfLongestSubstring_v3(words)

if __name__ == '__main__':
    main()
