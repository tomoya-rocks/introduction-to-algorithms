//go:build ignore

package main

import "fmt"

type Element struct {
	data int
	next *Element
}

type Queue struct {
	size int
	head *Element
	tail *Element
}

func enqueue(q *Queue, z *Element) {
	q.size += 1

	if q.head == nil {
		q.head = z
	} else {
		q.tail.next = z
	}
	q.tail = z
}

func dequeue(q *Queue) int {
	if q.size == 0 {
		fmt.Println("queue is empty.")

		return -1
	}

	q.size -= 1

	e := q.head
	result := e.data
	q.head = e.next
	e = nil

	return result
}

func printQueue(q *Queue) {
	fmt.Printf("size = %d : ", q.size)

	p := q.head
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
	q := Queue{0, nil, nil}

	for {
		fmt.Print("1:enqueue 2:dequeue 3:print > ")
		var op int
		fmt.Scanf("%d", &op)

		switch op {
		case 1:
			fmt.Print("input data > ")
			var data int
			fmt.Scanf("%d", &data)

			z := Element{data, nil}
			enqueue(&q, &z)
		case 2:
			result := dequeue(&q)
			if result != -1 {
				fmt.Printf("result = %d\n", result)
			}
		case 3:
			printQueue(&q)
		default:
			fmt.Println("invalid operation")
		}
	}
}
