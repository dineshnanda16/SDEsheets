class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        gen = []
        if numRows > 0:
            gen.append([1])
        if numRows > 1 :
            gen.append([1,1])           
        if numRows > 2:
            for i in range(3, numRows+1):
                new = [j for j in range(i)] 
                new[0] = 1 
                new[-1] = 1
                for k in range(1,len(new)-1):
                    new[k] = gen[-1][k-1] + gen[-1][k]
                gen.append(new)
        return gen        
        

""" pascals triangle is a mathematical concept with a formula nCr = n!/(r!*(n-r)!)
 where n is the row number and r is the column number"""