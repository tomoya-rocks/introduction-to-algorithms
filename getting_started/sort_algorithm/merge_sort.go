package sort_algorithm

import "fmt"

func MergeSort(data []int) {
	mergeSortInternal(data, 0, len(data)-1)
}

func mergeSortInternal(data []int, idxOfStart, idxOfEnd int) {
	if idxOfStart < idxOfEnd {
		idxOfMid := (idxOfStart + idxOfEnd) / 2

		mergeSortInternal(data, idxOfStart, idxOfMid)
		mergeSortInternal(data, idxOfMid+1, idxOfEnd)

		merge(data, idxOfStart, idxOfMid, idxOfEnd)

		fmt.Println(data)
	}
}

func merge(data []int, idxOfStart, idxOfMid, idxOfEnd int) {
	dataOfFirst := make([]int, idxOfMid-idxOfStart+1)
	copy(dataOfFirst, data[idxOfStart:idxOfMid+1])
	dataOfSecond := make([]int, idxOfEnd-idxOfMid)
	copy(dataOfSecond, data[idxOfMid+1:idxOfEnd+1])

	i, j := 0, 0
	for k := idxOfStart; k <= idxOfEnd; k++ {
		if i < len(dataOfFirst) && j < len(dataOfSecond) {
			if dataOfFirst[i] < dataOfSecond[j] {
				data[k] = dataOfFirst[i]
				i += 1
			} else {
				data[k] = dataOfSecond[j]
				j += 1
			}
		} else if i < len(dataOfFirst) {
			data[k] = dataOfFirst[i]
			i += 1
		} else {
			data[k] = dataOfSecond[j]
			j += 1
		}
	}
}
