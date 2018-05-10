class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=='':
            return []
        res = []
        num_dict =  {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
        self.helper(digits, res, -1, '', num_dict)
        return res
        
    def helper(self, digits, res, curIdx, tmp, num_dict):
        if curIdx==len(digits)-1:
            res.append(tmp)
            return 
        
        num = digits[curIdx+1]
        for char in num_dict[num]:
            self.helper(digits, res, curIdx+1, tmp+char, num_dict)
