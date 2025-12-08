"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10^-5 will be accepted.

EXAMPLE 1
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

EXAMPLE 2
Input: nums = [5], k = 1
Output: 5.00000

Constraints
n == nums.length
1 <= k <= n <= 105
-10^4 <= nums[i] <= 10^4

Notes:
- Pattern: Sliding Window
- Approach: 
- Time: O(n) as we iterate over the given nums array once
- Space: O(1) - constant extra space used

"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]
            
        ans = curr
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)
            
        return ans / k
