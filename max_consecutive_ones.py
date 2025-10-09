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
class MaxConsecutiveOnes:
    def max_consecutive_ones(self, nums): # Define method
        self.nums = nums 
        max_count = count = 0 # Initialize max_count and count
        for n in self.nums:
            if n == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count
    
# Instantiate the class
solution = MaxConsecutiveOnes()

# Test the method with the three arrays
print(solution.max_consecutive_ones(a)) # Output: 3
print(solution.max_consecutive_ones(b)) # Output: 4
print(solution.max_consecutive_ones(c)) # Output: 2