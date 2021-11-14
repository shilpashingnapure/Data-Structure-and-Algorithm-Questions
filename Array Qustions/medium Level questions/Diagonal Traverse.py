'''
Diagonal Traverse (like zig zag)
Medium

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

'''
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        if(m == 1 or n == 1):return sum(mat,[])
        ans = []
        for i in range(n):
            d = i + 0
            lst = self.findigonal(d , mat)
            if len(ans) % 2 == 0:
                ans.append(lst[::-1])
            else:
                ans.append(lst)
        
        for i in range(1,m):
            d = i + n-1
            lst = self.findigonal(d , mat)
            if len(ans) % 2 == 0:
                ans.append(lst[::-1])
            else:
                ans.append(lst)
        
        return sum(ans,[])
        
    def findigonal(self , d , mat):
        lst = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(i+j) == d:
                    lst.append(mat[i][j])
        return lst