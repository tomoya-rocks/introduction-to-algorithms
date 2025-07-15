package sort_algorithm

import "fmt"

func InsertionSort(data []int) {
	n := len(data)

	for j := 1; j < n; j++ {
		i := j - 1
		key := data[j]

		for ; i >= 0 && data[i] > key; i-- {
			data[i+1] = data[i]
		}

		data[i+1] = key

		fmt.Println(data)
	}
}
