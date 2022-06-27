class Solution:
    def minPartitions(self, n):
        #It will at least be a single digit number as specified in the constraints of the problem:
        minimum = 1
        for i in n:
          #The minimum deci-binary number will depend on the individual digits and if any digit in the string is 9, we have reached the maximum value possible for the digits. We just return the number 9 as we don't need to check further values in the string.
            if minimum ==9:
                return minimum
            minimum = max(minimum, int(i))
        return minimum
