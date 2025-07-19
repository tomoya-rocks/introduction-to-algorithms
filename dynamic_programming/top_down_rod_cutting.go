//go:build ignore

package main

import (
	"fmt"
	"math"
)

func cutRod(n int, prices []int) int {
	results := make([]int, n+1)
	for i := 0; i < len(results); i++ {
		results[i] = -math.MaxInt
	}

	return cutRodInternal(n, prices, results)
}

func cutRodInternal(n int, prices, results []int) int {
	if results[n] > -math.MaxInt {
		return results[n]
	}

	result := 0
	if n > 0 {
		for i := 1; i <= n; i++ {
			result = max(results[i], prices[i]+cutRodInternal(n-i, prices, results))
		}
	}

	results[n] = result

	return result
}

func main() {
	prices := []int{0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30}

	for i := 0; i < len(prices); i++ {
		result := cutRod(i, prices)

		fmt.Printf("length = %d / result = %d\n", i, result)
	}
}
