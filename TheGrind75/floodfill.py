class Solution:
    def floodfill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image
        value = image[sr][sc]
        Solution.colorfill(image, sr, sc, color, value)
        return image
     #depth first search algorithm
    def colorfill(image, sr, sc, color, value):
        if(sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != value):
            return
        
        image[sr][sc] = color
        #top
        Solution.colorfill(image, sr-1, sc, color, value)
        #right
        Solution.colorfill(image, sr, sc+1, color, value)
        #bottom
        Solution.colorfill(image, sr+1, sc, color, value)
        #left
        Solution.colorfill(image, sr, sc-1, color, value)
