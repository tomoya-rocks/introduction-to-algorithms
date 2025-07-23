//go:build ignore

package main

import (
	"fmt"
	"math"
)

func optimalBst(p, q []float32) ([][]float32, [][]int, [][]float32) {
	results := make([][]float32, len(p)+1)
	roots := make([][]int, len(p)+1)
	w := make([][]float32, len(p)+1)

	for k := range results {
		results[k] = make([]float32, len(p)+1)
		roots[k] = make([]int, len(p)+1)
		w[k] = make([]float32, len(p)+1)
	}

	for i := 0; i < len(results); i += 1 {
		for j := 0; j < len(results); j += 1 {
			results[i][j] = float32(math.MaxInt)
		}
	}

	for i := 1; i <= len(p); i += 1 {
		results[i][i-1] = q[i-1]
		w[i][i-1] = q[i-1]
	}

	for diff := 0; diff < len(p); diff += 1 {
		i := 1
		for j := i + diff; j < len(p); j += 1 {
			w[i][j] = w[i][j-1] + p[j] + q[j]

			for r := i; r < j+1; r += 1 {
				if results[i][j] > results[i][r-1]+results[r+1][j]+w[i][j] {
					results[i][j] = results[i][r-1] + results[r+1][j] + w[i][j]
					roots[i][j] = r
				}
			}

			i += 1
		}
	}

	return results, roots, w
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

	results, roots, w := optimalBst(p, q)
	for diff := -1; diff < len(p)-1; diff += 1 {
		fmt.Printf("--- diff = %d ---\n", diff)

		i := 1
		for j := i + diff; j < len(p); j += 1 {
			fmt.Printf("(i, j) = (%d, %d) / result = %.2f w = %.2f ", i, j, results[i][j], w[i][j])
			if j != i-1 {
				fmt.Printf("root = %d", roots[i][j])
			}
			fmt.Println()

			i += 1
		}
	}
}
