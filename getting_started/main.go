package main

import (
	"fmt"
	"getting_started/sort_algorithm"
)

func main() {
	data := sort_algorithm.CreateData()

	fmt.Println("--- before ---")
	fmt.Println(data)

	var op string
	fmt.Print("input sort (1:insertion sort 2:selection sort " +
		"3:bubble sort) > ")
	fmt.Scanf("%s", &op)

	switch op {
	case "1":
		sort_algorithm.InsertionSort(data)
	case "2":
		sort_algorithm.SelectionSort(data)
	case "3":
		sort_algorithm.BubbleSort(data)
	}

	fmt.Println("--- after ---")
	fmt.Println(data)
}
