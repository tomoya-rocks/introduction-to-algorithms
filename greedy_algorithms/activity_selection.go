package main

import "fmt"

func selectActivity(s, f []int) []int {
	result := make([]int, 0)

	result = append(result, 0)
	finished := f[0]
	for idx := 1; idx < len(s); idx += 1 {
		if finished < s[idx] {
			result = append(result, idx)

			finished = f[idx]
		}
	}

	return result
}

func main() {
	s := []int{1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12}
	f := []int{4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16}

	fmt.Print("  i |")
	for i, _ := range s {
		fmt.Printf("%3d|", i)
	}
	fmt.Println()
	fmt.Print("s[i]|")
	for _, _s := range s {
		fmt.Printf("%3d|", _s)
	}
	fmt.Println()
	fmt.Print("f[i]|")
	for _, _f := range f {
		fmt.Printf("%3d|", _f)
	}
	fmt.Println()

	result := selectActivity(s, f)
	fmt.Println("activities =", result)
}
