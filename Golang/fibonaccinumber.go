func fib(N int) int {
	fib := make([]int, 31)
	if N < 2 { return N }
	fib[0] = 0
	fib[1] = 1
	for i := 2; i <= N; i++ { fib[i] = fib[i-1] + fib[i-2] }
	return fib[N]
}
