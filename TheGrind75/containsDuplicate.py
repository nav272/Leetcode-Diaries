
class Solution:
  #set method 1
    def containsDuplicateset(self, nums: List[int]) -> bool:
        return (len(set(nums)) == len(nums))
      
  #hashtables method
    def containsDuplicateset(self, nums: List[int]) -> bool:
        fastlookup = {} #hashtables in python: we are the dictiornaries
        for i in nums:
          if i not in fastlookup:
            fastlookup[i] = 1
          else:
            return True #duplicate found 
          return False
        
