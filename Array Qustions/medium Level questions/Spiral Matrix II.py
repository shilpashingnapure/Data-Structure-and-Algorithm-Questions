# Spiral Matrix II
# Medium
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 
# Example 1:

# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for i in range(n)]for i in range(n)]
        size = n * n
        count = 0
        a = 1
        top = 0
        bottom = n-1
        left = 0
        right = n -1
        while count < size:

            #left to right
            for i in range(left , right + 1):
                if(count < size):
                    mat[top][i] = a
                    a += 1
                    count += 1
            top += 1

            #top to bottom
            for i in range(top , bottom + 1):
                if(count < size):
                    mat[i][right] = a
                    a += 1
                    count += 1
            right -= 1

            #right  to left
            for i in range(right , left -1 , -1):
                if(count < size):
                    mat[bottom][i] = a
                    a += 1
                    count += 1
            bottom -= 1

            #bottom to top
            for i in range(bottom , top - 1 , -1):
                if(count < size):
                    mat[i][left] = a
                    a += 1
                    count += 1
            left += 1
        return mat
        