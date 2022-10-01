class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
                              
        x = str(x)                           
        isneg = x.find("-")                  

        if isneg != -1:                      
            x = x[1:]                        

        new = ""                             
        i = len(x) - 1                       
        while i >= 0:                        
            new += x[i]                      
            i -= 1                           
        x, i= 0, 0
        if isneg != -1:                      
            new = "-" + new                  

        new = int(new)                       
        if new >= 2**31-1  or new <= -2**31:   
            return 0                         

        return new                           
