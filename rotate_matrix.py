class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in  range(len(matrix)//2):#flip the rows vertically
            matrix[i],matrix[-i-1]=matrix[-i-1],matrix[i]
        for i in range(len(matrix)):
            for j in range(i):#flip rows into columns
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]