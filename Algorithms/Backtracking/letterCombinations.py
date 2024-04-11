class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num = { '2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno",
        '7': "pqrs", '8':"tuv", '9':"wxyz"}
        
        if(len(digits) == 0): 
            return []

        res = []
        
        def combine(digits, index, combination):
            if (len(combination) == len(digits)):
                res.append(combination)
                combination = combination[:-1]
            if (index < len(digits)):
                for c in num.get(digits[index]):
                    combine(digits, (index + 1), combination + c)
                    
                    
                
        combine(digits,0,"")
        return res
        

