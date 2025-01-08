class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) in numSet:
                continue

            length = 0
            while (n+length) in numSet:
                length += 1
            longest = max(longest, length)
            
        return longest