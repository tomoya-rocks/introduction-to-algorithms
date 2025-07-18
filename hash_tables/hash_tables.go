package main

import "fmt"

type Element struct {
	key  int
	next *Element
	prev *Element
}

type Hashtable struct {
	bucketSize int
	table      []*Element
}

func (ht *Hashtable) put(z *Element) {
	hashVal := calculateHashValue(ht, z.key)

	if ht.table[hashVal] != nil {
		ht.table[hashVal].prev = z
	}
	z.next = ht.table[hashVal]
	ht.table[hashVal] = z
}

func (ht *Hashtable) contains(key int) *Element {
	hashVal := calculateHashValue(ht, key)

	for p := ht.table[hashVal]; p != nil; p = p.next {
		if p.key == key {
			return p
		}
	}

	return nil
}

func (ht *Hashtable) remove(z *Element) {
	hashVal := calculateHashValue(ht, z.key)

	if z.next != nil {
		z.next.prev = z.prev
	}
	if z.prev != nil {
		z.prev.next = z.next
	} else {
		ht.table[hashVal] = z.next
	}
	z = nil
}

func (ht *Hashtable) printHashtable() {
	for i := 0; i < ht.bucketSize; i++ {
		fmt.Printf("%d : ", i)

		for p := ht.table[i]; p != nil; p = p.next {
			fmt.Printf("%d", p.key)
			if p.next != nil {
				fmt.Print(" -> ")
			}
		}
		fmt.Println()
	}
}

func calculateHashValue(ht *Hashtable, key int) int {
	return key % ht.bucketSize
}

func main() {
	ht := Hashtable{13, nil}
	ht.table = make([]*Element, ht.bucketSize)

	for i := 1; i <= 100; i++ {
		z := Element{i, nil, nil}
		ht.put(&z)
	}

	for {
		fmt.Print("1:put 2:remove 3:print > ")
		var op int
		fmt.Scanf("%d", &op)

		switch op {
		case 1:
			fmt.Print("input key > ")
			var data int
			fmt.Scanf("%d", &data)

			z := Element{data, nil, nil}
			ht.put(&z)
		case 2:
			fmt.Print("input data > ")
			var data int
			fmt.Scanf("%d", &data)

			z := ht.contains(data)
			if z == nil {
				fmt.Printf("%d is not found in the hash table.\n", data)
			} else {
				ht.remove(z)
			}
		case 3:
			ht.printHashtable()
		default:
			fmt.Println("invalid operation")
		}
	}
}
