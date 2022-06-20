//write a code for making a binary tree in go
// binary tree data structure in go

func minCameraCover(root *Treenode) int {
	camera := 0
	if minCameraCoverSub(root, &camera) == "Has_no_camera_or_camera_is_not_covered" {
		camera++
	}
	return camera
}

//Three states of a node in this binary tree
// State 0: Node has to be covered by the camera as either one of the children don't have the camera
// State 1: Node is covered by camera but does not have the camera on it
// State 2: Node is not covered by the camera and has no camera on iself

func minCameraCoverSub(root *Treenode, camera *int) string {

	if root == nil {
		return "Is_monitored"
	}
	left := minCameraCoverSub(root.Left, camera)
	right := minCameraCoverSub(root.Right, camera)

	if left == "Has_no_camera_or_is_not_monitored" || right == "Has_no_camera_or_is_not_monitored" {
		*camera++
		return "Has_camera"
	} else if left == "Has_camera" && right == "Has_camera" {
		return "Is_monitored"
	} else {
		return "Has_no_camera_or_camera_is_not_covered"
	}

}
