class Solution:
    
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        ls = ["".join(sorted(i)) for i in words]     # Time : N*S*log(S)    Space : N * S
        d = {}
        
        for i in range(len(words)) :        # Time : N
            if ls[i] in d :                 # Time : 1
                d[ls[i]].append(words[i])   # Time : 1
            else :
                d[ls[i]] = [words[i]]       # Time : 1
        
        ans = []
        for i in d.keys() :                 # Time : N
            ans.append(d[i])                # Time : N
        
        return ans
