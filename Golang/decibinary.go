func minPartitions(n string) int {
	//declare the minimum number of deci-binary numbers required. 
	//With the constraints available, it will be 1, because the input will have at least one digit and which can't be 0
	minimum := 1
	for _, c:= range n{
		//check if the digit is 9
		//9 is the maximum value of any possible digit
		//e.g. 1 2 3 4 5 
		// Counter will work as 1 1 1 1 1
		//						0 1 1 1 1
		//						0 0 1 1 1 
		//						0 0 0 1 1 	
		//						0 0 0 0 1
		// here, there are 5 numbers dependent on the maximum digit value which was 5.
		// and because 9 is the highest value possible, if we reach 9 in our counter, we just return that value
		// Notice how the value of the minimum is not dependent on the length of the string.
		if minimum == 9 {
			return minimum
		}
		minimum = getMax(minimum, int(c-'0'))
	}
	return minimum
}

//To get the maximum value out of 2 integers
func getMax(a, b int) int {
	if (a > b){
		return a
	}
	return b
}
