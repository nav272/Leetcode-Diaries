class Solution:
    def findAnagrams(self, s, p):
        n = len(s)
        required = len(p)
        if required > n:
            return []
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        alphabetsHash = {}
        for i in alphabets:
            alphabetsHash[i] = hash(i)
        left = 0
        start = len(p)-1
        end = len(s)
        answer = []
        hashp = sum(map(hash,p))
        #print(hashp)
        current = sum(map(hash, s[:len(p)-1]))
        for right in range(start, end):
            current += alphabetsHash[s[right]]
            if current == hashp:
                answer.append(left)
            current -= alphabetsHash[s[left]]
            left +=1
        return answer
