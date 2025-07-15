package sort_algorithm

import "fmt"

func SelectionSort(data []int) {
	n := len(data)

	for i := 0; i < n-1; i++ {
		idx_of_min := i
		for j := i + 1; j < n; j++ {
			if data[j] < data[idx_of_min] {
				idx_of_min = j
			}
		}

		if idx_of_min != i {
			data[i], data[idx_of_min] = data[idx_of_min], data[i]
		}

		fmt.Println(data)
	}
}
