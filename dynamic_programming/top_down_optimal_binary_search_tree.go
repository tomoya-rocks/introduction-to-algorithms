//go:build ignore

package main

import (
	"fmt"
	"math"
)

func optimalBst(p, q []float32, i, j int) float32 {
	results := make([][]float32, len(p)+1)
	for k := range results {
		results[k] = make([]float32, len(p)+1)
	}

	for k := 0; k < len(results); k += 1 {
		for l := 0; l < len(results[k]); l += 1 {
			results[k][l] = math.MaxInt
		}
	}

	return optimalBstInternal(p, q, i, j, results)
}

func optimalBstInternal(p, q []float32, i, j int, results [][]float32) float32 {
	if results[i][j] < math.MaxInt {
		return results[i][j]
	}

	result := float32(math.MaxInt)
	if j == i-1 {
		result = q[i-1]
	} else {
		w := q[i-1]
		for l := i; l <= j; l += 1 {
			w += p[l]
			w += q[l]
		}

		for r := i; r < j+1; r += 1 {
			result = min(result, optimalBstInternal(p, q, i, r-1, results)+optimalBstInternal(p, q, r+1, j, results)+w)
		}
	}

	results[i][j] = result

	return result
}

func main() {
	p := []float32{0, 0.15, 0.10, 0.05, 0.10, 0.20}
	q := []float32{0.05, 0.10, 0.05, 0.05, 0.05, 0.10}

	fmt.Print("  i |")
	for i := 0; i < len(p); i += 1 {
		fmt.Printf("%4d|", i)
	}
	fmt.Println()
	fmt.Print("p[i]|")
	for i := 0; i < len(p); i += 1 {
		fmt.Printf("%.2f|", p[i])
	}
	fmt.Println()
	fmt.Print("q[i]|")
	for i := 0; i < len(q); i += 1 {
		fmt.Printf("%.2f|", q[i])
	}
	fmt.Println()

	for diff := -1; diff < len(p)-1; diff += 1 {
		fmt.Printf("--- diff = %d ---\n", diff)

		i := 1
		for j := i + diff; j < len(p); j += 1 {
			result := optimalBst(p, q, i, j)

			fmt.Printf("(i, j) = (%d, %d) / result = %.2f\n", i, j, result)

			i += 1
		}
	}
}
