'''
Number of Pairs of Strings With Concatenation Equal to Target
Medium

Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

 

Example 1:

Input: nums = ["777","7","77","77"], target = "7777"
Output: 4
Explanation: Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"

'''
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        c = 0
        n = len(nums) 
        for i in range(n):
            a = nums[i]
            for j in range(n):
                if i!= j:
                    Cont = a + nums[j]
                    c += Cont == target
                    
        return c