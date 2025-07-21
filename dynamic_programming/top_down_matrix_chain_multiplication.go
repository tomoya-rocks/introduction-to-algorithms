//go:build ignore

package main

import (
	"fmt"
	"math"
)

func matrixChainOrder(p []int, i, j int) int {
	results := make([][]int, j+1)
	for i := range results {
		results[i] = make([]int, j+1)
	}

	for i := 0; i < len(results); i += 1 {
		for j := 0; j < len(results); j += 1 {
			if i != j {
				results[i][j] = math.MaxInt
			}
		}
	}

	return matrixChainOrderInternal(p, i, j, results)
}

func matrixChainOrderInternal(p []int, i, j int, results [][]int) int {
	if results[i][j] < math.MaxInt {
		return results[i][j]
	}

	result := math.MaxInt
	if i == j {
		result = 0
	} else {
		for k := i; k < j; k++ {
			result = min(result, matrixChainOrderInternal(p, i, k, results)+matrixChainOrderInternal(p, k+1, j, results)+p[i]*p[k+1]*p[j+1])
		}
	}

	results[i][j] = result

	return result
}

func main() {
	p := []int{30, 35, 15, 5, 10, 20, 25}

	for diff := 0; diff < len(p)-1; diff = diff + 1 {
		fmt.Printf("--- diff = %d ---\n", diff)

		i := 0
		for j := i + diff; j < len(p)-1; j += 1 {
			result := matrixChainOrder(p, i, j)

			fmt.Printf("(i, j) = (%d, %d) / result = %d\n", i, j, result)

			i += 1
		}
	}
}
