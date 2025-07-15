//go:build ignore

package main

import (
	"fmt"
)

func search(data []int, key int) int {
	idxOfStart := 0
	idxOfEnd := len(data) - 1

	for idxOfStart <= idxOfEnd {
		idxOfMid := (idxOfStart + idxOfEnd) / 2
		if data[idxOfMid] == key {
			return idxOfMid
		} else if data[idxOfMid] < key {
			idxOfStart = idxOfMid + 1
		} else {
			idxOfEnd = idxOfMid - 1
		}
	}

	return -1
}

func main() {
	data := make([]int, 20)
	for i := 0; i < 20; i++ {
		data[i] = 2 * i
	}

	fmt.Println(data)

	fmt.Print("input search key > ")
	var key int
	fmt.Scanf("%d", &key)

	result := search(data, key)
	if result != -1 {
		fmt.Printf("result = %d\n", result)
	} else {
		fmt.Printf("%d is not found.", key)
	}
}
