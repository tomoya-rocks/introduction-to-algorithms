//go:build ignore

package main

import (
	"fmt"
	"math"
)

func cutRod(n int, prices []int) int {
	if n == 0 {
		return 0
	}

	result := -math.MaxInt
	for i := 1; i <= n; i++ {
		result = max(result, prices[i]+cutRod(n-i, prices))
	}

	return result
}

func main() {
	prices := []int{0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30}

	for i := 0; i < len(prices); i++ {
		result := cutRod(i, prices)

		fmt.Printf("length = %d / result = %d\n", i, result)
	}
}
