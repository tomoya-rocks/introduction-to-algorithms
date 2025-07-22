//go:build ignore

package main

import (
	"fmt"
	"math"
)

func common_lcs(x, y string) ([][]int, [][]int) {
	results := make([][]int, max(len(x), len(y))+1)
	directions := make([][]int, max(len(x), len(y))+1)
	for i := 0; i < len(results); i += 1 {
		for j := 0; j < len(results); j += 1 {
			results[i] = make([]int, max(len(x), len(y))+1)
			directions[i] = make([]int, max(len(x), len(y))+1)
		}
	}

	result := -math.MaxInt
	for i := 0; i < len(x); i += 1 {
		for j := 0; j < len(y); j += 1 {
			if i == 0 && j == 0 {
				if x[i] == y[j] {
					result = 1
					directions[i][j] = 0
				} else {
					result = 0
					directions[i][j] = 1
				}
			} else if i == 0 {
				if x[i] == y[j] {
					result = 1
					directions[i][j] = 0
				} else {
					result = results[i][j-1]
					directions[i][j] = 1
				}
			} else if j == 0 {
				if x[i] == y[j] {
					result = 1
					directions[i][j] = 0
				} else {
					result = results[i-1][j]
					directions[i][j] = 2
				}
			} else {
				if x[i] == y[j] {
					result = results[i-1][j-1] + 1
					directions[i][j] = 0
				} else {
					if results[i-1][j] < results[i][j-1] {
						result = results[i][j-1]
						directions[i][j] = 1
					} else {
						result = results[i-1][j]
						directions[i][j] = 2
					}
				}
			}

			results[i][j] = result
		}
	}

	return results, directions
}

func printOptimalStrategy(directions [][]int, x string, i, j int) {
	if i < 0 || j < 0 {
		return
	} else {
		switch directions[i][j] {
		case 0:
			printOptimalStrategy(directions, x, i-1, j-1)
			fmt.Printf("%c", x[i])
		case 1:
			printOptimalStrategy(directions, x, i, j-1)
		case 2:
			printOptimalStrategy(directions, x, i-1, j)
		}
	}
}

func main() {
	x := "ABCBDAB"
	y := "BDCABA"

	results, directions := common_lcs(x, y)
	for i := 0; i < len(x); i += 1 {
		fmt.Printf("--- i = %d ---\n", i)
		for j := 0; j < len(y); j += 1 {
			fmt.Printf("(i, j) = (%d, %d) / result = %d ", i, j, results[i][j])

			if results[i][j] > 0 {
				fmt.Print("(")
				printOptimalStrategy(directions, x, i, j)
				fmt.Print(")")
			}
			fmt.Println()
		}
	}
}
