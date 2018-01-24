class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v_list=[]
        v_index=[]
        vowels =["a","e","i","o","u","A","E","I","O","U"]
        for i, c in enumerate(s):
        	if c in vowels:
        		v_list.append(c)
        		v_index.append(i)


        v_inverse=v_list[::-1]
       
        s=list(s)
     	for i, c in enumerate(v_index):
            print(s[c])
            print(v_inverse[i])
            s[c]=v_inverse[i]
        
        s="".join(s)
        

     	return s
