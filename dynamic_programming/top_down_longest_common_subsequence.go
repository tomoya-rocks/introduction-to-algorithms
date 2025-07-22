//go:build ignore

package main

import (
	"fmt"
	"math"
)

func common_lcs(x, y string, i, j int) int {
	results := make([][]int, max(len(x), len(y)+1))
	for i := 0; i < len(results); i += 1 {
		results[i] = make([]int, max(len(x), len(y)+1))
	}

	for i := 0; i < len(results); i += 1 {
		for j := 0; j < len(results); j += 1 {
			results[i][j] = -math.MaxInt
		}
	}

	return common_lcs_internal(x, y, i, j, results)
}

func common_lcs_internal(x, y string, i, j int, results [][]int) int {
	if results[i][j] > -math.MaxInt {
		return results[i][j]
	}

	result := -math.MaxInt
	if i == 0 && j == 0 {
		if x[i] == y[j] {
			result = 1
		} else {
			result = 0
		}
	} else if i == 0 {
		if x[i] == y[j] {
			result = 1
		} else {
			result = common_lcs_internal(x, y, i, j-1, results)
		}
	} else if j == 0 {
		if x[i] == y[j] {
			result = 1
		} else {
			result = common_lcs_internal(x, y, i-1, j, results)
		}
	} else {
		if x[i] == y[j] {
			result = common_lcs_internal(x, y, i-1, j-1, results) + 1
		} else {
			if common_lcs(x, y, i, j-1) < common_lcs(x, y, i-1, j) {
				result = common_lcs_internal(x, y, i-1, j, results)
			} else {
				result = common_lcs_internal(x, y, i, j-1, results)
			}
		}
	}

	results[i][j] = result

	return result
}

func main() {
	x := "ABCBDAB"
	y := "BDCABA"

	for i := 0; i < len(x); i += 1 {
		fmt.Printf("--- i = %d ---\n", i)
		for j := 0; j < len(y); j += 1 {
			result := common_lcs(x, y, i, j)

			fmt.Printf("(i, j) = (%d, %d) / result = %d\n", i, j, result)
		}
	}
}
