//go:build ignore

package main

import (
	"fmt"
	"math/rand"
)

func createData() []int {
	data := make([]int, 40)

	for i := 0; i < 40; i++ {
		data[i] = rand.Intn(20)
	}

	return data
}

func countingSort(data []int) {
	n := len(data)
	max := 0
	for i := 0; i < n; i++ {
		if data[i] > max {
			max = data[i]
		}
	}

	countingTable := make([]int, max+1)
	for i := 0; i < n; i++ {
		countingTable[data[i]] += 1
	}
	for i := 1; i < len(countingTable); i++ {
		countingTable[i] += countingTable[i-1]
	}
	fmt.Println("--- counting table ---")
	fmt.Println(countingTable)

	temporaryData := make([]int, len(data))
	for i := n - 1; i >= 0; i-- {
		targetData := data[i]
		idxToSet := countingTable[targetData] - 1
		temporaryData[idxToSet] = targetData
		countingTable[targetData] -= 1
	}
	fmt.Println("--- temporary data ---")
	fmt.Println(temporaryData)

	data = data[:0]
	data = append(data, temporaryData...)
}

func main() {
	data := createData()

	fmt.Println("--- before ---")
	fmt.Println(data)

	fmt.Println("--- sort ---")
	countingSort(data)

	fmt.Println("--- after ---")
	fmt.Println(data)
}
