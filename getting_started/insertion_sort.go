package main

import (
	"fmt"
	"math/rand"
)

func CreateData() []int {
	data := make([]int, 20)

	for i := 0; i < 20; i++ {
		data[i] = rand.Intn(20)
	}

	return data
}

func Sort(data []int) {
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

func main() {
	data := CreateData()

	fmt.Println(data)
	Sort(data)
}
