class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        shash = {}
        for i in s:
            shash[i] = 1 + shash.get(i, 0)
        
        thash = {}
        for i in t:
            if i not in shash:
                return False
            else:
                thash[i] = 1 + thash.get(i,0)
        
        return thash == shash
