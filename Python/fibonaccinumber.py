class Solution:
    def fib(self, n: int) -> int:
        answer = {}
        answer[0] = 0
        answer[1] = 1
        if n > 1: 
            for i in range(2, n+1):
                answer[i] = (answer[i-1] + answer[i-2])
        return answer[n]
