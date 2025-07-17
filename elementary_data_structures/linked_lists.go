//go:build ignore

package main

import "fmt"

type Element struct {
	data int
	next *Element
	prev *Element
}

type List struct {
	size int
	head *Element
	tail *Element
}

func append(l *List, z *Element) {
	l.size += 1

	if l.head == nil {
		l.head = z
	} else {
		l.tail.next = z
	}
	z.prev = l.tail
	l.tail = z
}

func contains(l *List, data int) *Element {
	for p := l.head; p != nil; p = p.next {
		if p.data == data {
			return p
		}
	}

	return nil
}

func remove(l *List, z *Element) {
	l.size -= 1

	if z.next != nil {
		z.next.prev = z.prev
	} else {
		l.tail = z.prev
	}
	if z.prev != nil {
		z.prev.next = z.next
	} else {
		l.head = z.next
	}
	z = nil
}

func printList(l *List) {
	fmt.Printf("size = %d\n", l.size)

	fmt.Println("--- from head to tail ---")
	for p := l.head; p != nil; p = p.next {
		fmt.Printf("%d", p.data)
		if p.next != nil {
			fmt.Print(" -> ")
		}
	}
	fmt.Println()

	fmt.Println("--- from tail to head ---")
	for p := l.tail; p != nil; p = p.prev {
		fmt.Printf("%d", p.data)
		if p.prev != nil {
			fmt.Print(" <- ")
		}
	}
	fmt.Println()
}

func main() {
	l := List{0, nil, nil}

	for {
		fmt.Print("1:append 2:remove 3:print > ")
		var op int
		fmt.Scanf("%d", &op)

		switch op {
		case 1:
			fmt.Print("input data > ")
			var data int
			fmt.Scanf("%d", &data)

			z := Element{data, nil, nil}
			append(&l, &z)
		case 2:
			fmt.Print("input data > ")
			var data int
			fmt.Scanf("%d", &data)

			z := contains(&l, data)
			if z == nil {
				fmt.Printf("%d is not found in the list.\n", data)
			} else {
				remove(&l, z)
			}
		case 3:
			printList(&l)
		default:
			fmt.Println("invalid operation")
		}
	}
}
