//go:build ignore

package main

import "fmt"

type Element struct {
	data int
	next *Element
}

type Stack struct {
	size int
	head *Element
}

func (s *Stack) push(z *Element) {
	s.size += 1

	z.next = s.head
	s.head = z
}

func (s *Stack) pop() int {
	if s.size == 0 {
		fmt.Println("stack is empty.")

		return -1
	}

	s.size -= 1

	e := s.head
	result := e.data
	s.head = e.next
	e = nil

	return result
}

func (s *Stack) printStack() {
	fmt.Printf("size = %d : ", s.size)

	p := s.head
	for p != nil {
		fmt.Printf("%d", p.data)
		if p.next != nil {
			fmt.Print(" -> ")
		}

		p = p.next
	}

	fmt.Println()
}

func main() {
	s := Stack{0, nil}

	for {
		fmt.Print("1:push 2:pop 3:print > ")
		var op int
		fmt.Scanf("%d", &op)

		switch op {
		case 1:
			fmt.Print("input data > ")
			var data int
			fmt.Scanf("%d", &data)

			z := Element{data, nil}
			s.push(&z)
		case 2:
			result := s.pop()
			if result != -1 {
				fmt.Printf("result = %d\n", result)
			}
		case 3:
			s.printStack()
		default:
			fmt.Println("invalid operation")
		}
	}
}
