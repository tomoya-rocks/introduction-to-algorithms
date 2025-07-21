//go:build ignore

package main

import (
	"fmt"
	"math"
)

func matrixChainOrder(p []int) ([][]int, [][]int) {
	results := make([][]int, len(p))
	thresholds := make([][]int, len(p))
	for i := range results {
		results[i] = make([]int, len(p))
		thresholds[i] = make([]int, len(p))
	}

	for i := 0; i < len(p)-1; i += 1 {
		results[i][i] = 0
		thresholds[i][i] = i
	}

	for diff := 1; diff < len(p)-1; diff += 1 {
		i := 0
		for j := i + diff; j < len(p)-1; j += 1 {
			result := math.MaxInt
			for k := i; k < j; k += 1 {
				if result > results[i][k]+results[k+1][j]+p[i]*p[k+1]*p[j+1] {
					result = results[i][k] + results[k+1][j] + p[i]*p[k+1]*p[j+1]
					thresholds[i][j] = k
				}
			}

			results[i][j] = result

			i += 1
		}
	}

	return results, thresholds
}

func printOptimalStrategy(thresholds [][]int, i, j int) {
	if i == j {
		fmt.Printf("A%d", thresholds[i][j])
	} else {
		fmt.Print("(")
		printOptimalStrategy(thresholds, i, thresholds[i][j])
		printOptimalStrategy(thresholds, thresholds[i][j]+1, j)
		fmt.Print(")")
	}
}

func main() {
	p := []int{30, 35, 15, 5, 10, 20, 25}

	results, thresholds := matrixChainOrder(p)
	for diff := 0; diff < len(p)-1; diff = diff + 1 {
		fmt.Printf("--- diff = %d ---\n", diff)

		i := 0
		for j := i + diff; j < len(p)-1; j += 1 {
			fmt.Printf("(i, j) = (%d, %d) / result = %d ", i, j, results[i][j])
			if i != j {
				printOptimalStrategy(thresholds, i, j)
			}
			fmt.Println()

			i += 1
		}
	}
}
