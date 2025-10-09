"""
LeetCode 1: Two Sum
https://leetcode.com/problems/two-sum/description/

Problem:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, return [0, 1].

Approach:
- Use hash map (`numMap`) to store numbers and their indices.
- For each element, compute its complement (`target - num`).
- If the complement exists in the map, return both indices.
- Otherwise, add the current number and index to the map.

Pattern: Hash Map / Single Pass

Complexity:
- Time: O(n) — each element is processed once
- Space: O(n) — storing up to n elements in the hash map
"""

class TwoSum:
    def two_sum(self, nums, target):
        numMap = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        return []  # No solution found

# Test the method with example input
d = [2,7,11,15] # Example input
target = 9 # Expected output: [0,1]
TwoSumInstance = TwoSum() # Create instance of the class
print(TwoSumInstance.two_sum(d, target)) # Output: [0, 1]