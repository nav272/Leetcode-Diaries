
func longestStrChain(words []string) int {
    //Key points:
//    1. sort the words by length
//    2. use a map to store the longest chain for each word
//    3. loop over the words and check if the previous word is a predecessor of the current word
//    4. if the previous word is a predecessor(i.e. it is in the map), add 1 to the longest chain of the current word
//    5. return the max of all the longest chains

    //1. sort the words by length
    sort.Slice(words, func(i, j int) bool {
        return len(words[i]) < len(words[j])
    })
    //2. use a map to store the longest chain for each word
    m := make(map[string]int)
    max := 0 // length of the longest chain 
    //3. loop over the words and check if the previous word is a predecessor of the current word
    for _, word := range words {
        length := 1
        for i := 0; i < len(word); i++ {
            if k := word[:i] + word[i+1:] +1; k > length {
                length = k
            }
    //4. if the previous word is a predecessor(i.e. it is in the map), add 1 to the longest chain of the current word
        if (length > max) {
            max = length
        }
    }
    return max
}
