class TimeMap:

    def __init__(self):
        self.default_Dict = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.default_Dict[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        #store it in a hash table. You can't define the hashtable every time.
        if key in self.default_Dict:
            if self.default_Dict[key][0][1] > timestamp:
                return ''
            left = 0
            right = len(self.default_Dict[key]) -1 

            while left < right:
                mid = left + (right-left)//2
                if self.default_Dict[key][mid][1] >= timestamp:
                    right = mid -1
                else:
                    left = mid + 1
            
            if left <= (len(self.default_Dict[key])-1):
                if self.default_Dict[key][left][1] <= timestamp:
                    return self.default_Dict[key][left][0]
                    
                elif self.default_Dict[key][left-1][1] <= timestamp:
                    return self.default_Dict[key][left-1][0]
        else:
            return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
