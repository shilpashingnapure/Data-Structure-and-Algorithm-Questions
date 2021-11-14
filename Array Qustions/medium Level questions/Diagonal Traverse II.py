'''
Diagonal Traverse II
Medium

Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.
 

Example 1:



Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
Example 2:



Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
Example 3:

Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
Output: [1,4,2,5,3,8,6,9,7,10,11]
Example 4:

Input: nums = [[1,2,3,4,5,6]]
Output: [1,2,3,4,5,6]

'''
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j in d:
                    d[i+j].insert(0,nums[i][j])
                else:
                    d[i+j] = [nums[i][j]]
        res = []
        for i in sorted(d):
            res.extend(d[i])
        return res
                    
    
         