'''
Sort the Matrix Diagonally
Medium


A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

'''

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m == 1 or n == 1:
            return mat

        #col
        columns = []
        for col in range(1,n):
            l = []
            for row in range(n - col):
                if row < m:
                    c = mat[row][row+col]
                    l.append(c)
            columns.append(sorted(l))

        for col in range(1,n):
            for row in range(n - col):
                if row < m:
                    mat[row][row+col] = columns[col-1][row]


        #row
        rows = []
        for row in range(1,m):
            l = []
            for col in range(m - row):
                if col < n:
                    c = mat[row+col][col]
                    l.append(c)
            rows.append(sorted(l))

        for row in range(1,m):
            for col in range(m - row):
                if col < n:
                    mat[row+col][col] = rows[row-1][col]

        #middle dignoal
        if n > 2:
            mid = []
            for i in range(m):
                mid.append(mat[i][i])
            mid.sort()
            for i in range(m):
                mat[i][i] = mid[i]
        
        return mat