//source: https://leetcode.com/problems/longest-consecutive-sequence/discuss/440446/Go-golang-O(n)-clean-solution

func longestConsecutive(nums []int) int {
   if len(nums) == 0 {
        return 0
   }
    
    // longest represents the length of the longest consecutive elements sequence.
    longest := 1
    
    // set represents the set of numbers (removes duplicates).
    set := make(map[int]bool, len(nums))
    
    // add the numbers to the set.
    // O(n)
    for _, v := range nums {
        set[v] = true
    }
    
    // iterate through the set to find the longest consecutive sequence.
    for _, v := range nums {
        // if the previous number does not exist,
        // the current number represents the first number in a consecutive sequence.
        if !set[v-1] {

            // determine the length of the current consecutive sequence.
            current := 1
            v++
            for set[v] {
                current++
                v++
            }
            
            // set the longest consecutive sequence.
            if current > longest {
                longest = current
            }
        }
    }
    
    return longest
}
