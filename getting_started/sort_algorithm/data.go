package sort_algorithm

import (
	"math/rand"
)

func CreateData() []int {
	data := make([]int, 20)

	for i := 0; i < 20; i++ {
		data[i] = rand.Intn(20)
	}

	return data
}
