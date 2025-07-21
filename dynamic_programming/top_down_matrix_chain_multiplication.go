//go:build ignore

package main

import (
	"fmt"
	"math"
)

func matrixChainOrder(p []int, i, j int) int {
	if i == j {
		return 0
	}

	result := math.MaxInt
	for k := i; k < j; k++ {
		result = min(result, matrixChainOrder(p, i, k)+matrixChainOrder(p, k+1, j)+p[i]*p[k+1]*p[j+1])
	}

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
