package main

import (
	"fmt"
	"math"
)

func cutRod(prices []int) ([]int, []int) {
	results := make([]int, len(prices)+1)
	slices := make([]int, len(prices)+1)

	results[0] = 0
	for j := 1; j < len(prices); j++ {
		result := -math.MaxInt
		for i := 0; i < j+1; i++ {
			if result < prices[i]+results[j-i] {
				result = prices[i] + results[j-i]
				slices[j] = i
			}
		}

		results[j] = result
	}

	return results, slices
}

func printOptimalStrategy(n int, slices []int) {
	rest := n

	fmt.Print("(")

	for rest > 0 {
		fmt.Printf("%d", slices[rest])
		if rest-slices[rest] > 0 {
			fmt.Print(" + ")
		}
		rest -= slices[rest]
	}

	fmt.Print(")")
}

func main() {
	prices := []int{0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30}

	results, slices := cutRod(prices)
	for i := 0; i < len(prices); i++ {

		fmt.Printf("length = %d / result = %d ", i, results[i])
		if i != 0 {
			printOptimalStrategy(i, slices)
		}
		fmt.Println()
	}
}
