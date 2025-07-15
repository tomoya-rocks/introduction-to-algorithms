package main

import (
	"fmt"
	"getting_started/sort_algorithm"
)

func main() {
	data := sort_algorithm.CreateData()

	fmt.Println(data)

	fmt.Println("--- insertion sort ---")
	sort_algorithm.InsertionSort(data)
}
