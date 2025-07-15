//go:build ignore

package main

import (
	"fmt"
	"math/rand"
	"sort"
)

func createData() []int {
	data := make([]int, 100)

	for i := 0; i < 100; i++ {
		data[i] = rand.Intn(100)
	}

	return data
}

func bucketSort(data []int) {
	n := len(data)
	max := 0
	for i := 0; i < n; i++ {
		if data[i] > max {
			max = data[i]
		}
	}

	bucket := make([][]int, max/10+1)

	for i := 0; i < n; i++ {
		bucket[data[i]/10] = append(bucket[data[i]/10], data[i])
	}

	fmt.Println("--- bucket beore sort ---")
	for i := 0; i < len(bucket); i++ {
		fmt.Printf("%d : %v\n", i, bucket[i])
	}

	for i := 0; i < len(bucket); i++ {
		sort.Ints(bucket[i])
	}

	fmt.Println("--- bucket after sort ---")
	for i := 0; i < len(bucket); i++ {
		fmt.Printf("%d : %v\n", i, bucket[i])
	}

	data = data[:0]
	for i := 0; i < len(bucket); i++ {
		data = append(data, bucket[i]...)
	}
}

func main() {
	data := createData()

	fmt.Println("--- before ---")
	fmt.Println(data)

	fmt.Println("--- sort ---")
	bucketSort(data)

	fmt.Println("--- after ---")
	fmt.Println(data)
}
