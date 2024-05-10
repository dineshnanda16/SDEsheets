class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n1,n2=len(matrix),len(matrix[0])
        row,column = ([0]*n1),([0]*n2)
        for i in range(n1):
            for j in range(n2):
                if matrix[i][j]==0:
                    row[i],column[j]=1,1

        for i in range(n1):
            for j in range(n2):
                if row[i] or column[j]:
                    matrix[i][j]=0

""" This is a brute force solution, here first loop ensures to make the row
and column which is zero then that coloumn and row is made one in the matrix
"""
""" then second loop is used to make the matrix zero if the row or column is true"""