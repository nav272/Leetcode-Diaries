#Possibilites for each node to consider. 
# Possibility 1: Both children do not have the camera on them.
# Possibility 2: One child has the camera on itself
# Possibility 3: Either has no children or is not being monitored by the camera.

#We take 3 state variables: Has_Camera, Is_Monitored and Has_no_camera_or_is_not_monitored
class Solution: 
    def minCameraCover(self, root):
        camera=0
        def dfs(node):
            if not node:
                return 1
            left, right = dfs(node.left), dfs(node.right)
            if left == "Has_no_camera_or_is_not_monitored" or right == "Has_no_camera_or_is_not_monitored":
                camera +=1
                return "Has_camera"
            elif left == "Has_camera" or right == "Has_camera":
                return "Is_Monitored"
            else:
                return "Has_no_camera_or_is_not_monitored"
        if dfs(root) == "Has_no_camera_or_is_not_monitored":
            camera += 1
        return camera
