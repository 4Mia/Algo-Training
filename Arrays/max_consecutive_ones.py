"""
LeetCode Explore: Max Consecutive Ones
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/

Notes:
- Pattern: Sliding Window / Counting
- Approach: Increment count for each 1; reset on 0. Track maximum.
- Time: O(n), Space: O(1)
"""

# Create three arrays to test
a = [1,1,0,1,1,1]
b = [2,1,1,1,1]
c = [0,1,1,0]

# Create class to find max consecutive 1's
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1

            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans
