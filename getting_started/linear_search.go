//go:build ignore

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

func search(data []int, key int) int {
	for i := 0; i < len(data); i++ {
		if data[i] == key {
			return i
		}
	}

	return -1
}

func main() {
	data := createData()

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
