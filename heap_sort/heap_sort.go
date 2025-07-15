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
	buildMaxHeap(data)

	fmt.Println(data)

	n := len(data) - 1
	for i := n; i >= 1; i-- {
		data[0], data[i] = data[i], data[0]

		fmt.Println(data)

		maxHeapify(data, 0, i-1)
	}
}

func buildMaxHeap(data []int) {
	n := len(data) - 1

	for i := n / 2; i >= 0; i-- {
		maxHeapify(data, i, n)
	}
}

func maxHeapify(data []int, idxOfTarget, idxOfHeap int) {
	idxOfLargest := idxOfTarget
	idxOfLeft := 2*idxOfTarget + 1
	idxOfRight := 2 * (idxOfTarget + 1)

	if idxOfLeft < idxOfHeap && data[idxOfLeft] > data[idxOfLargest] {
		idxOfLargest = idxOfLeft
	}
	if idxOfRight < idxOfHeap && data[idxOfRight] > data[idxOfLargest] {
		idxOfLargest = idxOfRight
	}

	if idxOfLargest != idxOfTarget {
		data[idxOfTarget], data[idxOfLargest] = data[idxOfLargest], data[idxOfTarget]

		maxHeapify(data, idxOfLargest, idxOfHeap)
	}
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
