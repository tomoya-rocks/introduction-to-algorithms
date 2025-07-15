package main

import (
	"fmt"
	"math/rand"
)

func createData() []int {
	data := make([]int, 20)

	for i := 0; i < 20; i++ {
		data[i] = rand.Intn(20)
	}

	return data
}

func sort(data []int) {
	quickSort(data, 0, len(data)-1)
}

func quickSort(data []int, idxOfStart, idxOfEnd int) {
	if idxOfStart < idxOfEnd {
		idxOfPartition := partition(data, idxOfStart, idxOfEnd)

		quickSort(data, idxOfStart, idxOfPartition-1)
		quickSort(data, idxOfPartition+1, idxOfEnd)
	}
}

func partition(data []int, idxOfStart, idxOfEnd int) int {
	pivot := data[idxOfEnd]

	i := idxOfStart
	for j := idxOfStart; j < idxOfEnd; j++ {
		if data[j] < pivot {
			data[i], data[j] = data[j], data[i]
			i += 1
		}
	}

	data[i], data[idxOfEnd] = data[idxOfEnd], data[i]

	fmt.Println(data)

	return i
}

func main() {
	data := createData()

	fmt.Println("--- before ---")
	fmt.Println(data)

	fmt.Println("--- sort ---")
	sort(data)

	fmt.Println("--- after ---")
	fmt.Println(data)
}
