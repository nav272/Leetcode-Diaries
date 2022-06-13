import "fmt"
func minimumTotal(triangle [][]int) int {
    for i := 1; i < len(triangle); i++ {
        for j := 0; j < len(triangle[i]); j++{
            upperLeft := 100001
            if j > 0 {
                upperLeft = triangle[i-1][j-1]
            }
            upperRight := 100001
            if j < len(triangle[i])-1 {
                upperRight = triangle[i-1][j]
            }
            triangle[i][j] += min(upperLeft, upperRight)
            fmt.Println(triangle)
        }
    }
    minimum := 100001
    for _, v := range triangle[len(triangle)-1] {
        if v < minimum {
            minimum = v
        }

                    
    }

    return minimum
}


func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
