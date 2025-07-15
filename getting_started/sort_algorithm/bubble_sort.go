package sort_algorithm

import "fmt"

func BubbleSort(data []int) {
	n := len(data)

	for i := n - 1; i >= 0; i-- {
		isSwapped := false
		for j := 0; j < i; j++ {
			if data[j+1] < data[j] {
				isSwapped = true
				data[j], data[j+1] = data[j+1], data[j]
			}
		}

		if !isSwapped {
			break
		}

		fmt.Println(data)
	}
}
