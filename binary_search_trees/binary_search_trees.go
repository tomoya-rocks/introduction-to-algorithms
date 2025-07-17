package main

import (
	"fmt"
	"strings"
)

type Element struct {
	key    int
	left   *Element
	right  *Element
	parent *Element
}

type Tree struct {
	size   int
	height int
	root   *Element
}

func put(t *Tree, z *Element) {
	t.size += 1

	var x *Element = t.root
	var y *Element = nil
	for x != nil {
		y = x
		if z.key < x.key {
			x = x.left
		} else {
			x = x.right
		}
	}

	z.parent = y
	if y == nil {
		t.root = z
	} else {
		if z.key < y.key {
			y.left = z
		} else {
			y.right = z
		}
	}

	t.height = getHeight(t)
}

func contains(t *Tree, key int) *Element {
	x := t.root
	for x != nil && x.key != key {
		if key < x.key {
			x = x.left
		} else {
			x = x.right
		}
	}

	return x
}

func remove(t *Tree, z *Element) {
	t.size -= 1

	if z.left == nil {
		transplant(t, z, z.right)
	} else if z.right == nil {
		transplant(t, z, z.left)
	} else {
		y := successor(z)
		if y != z.right {
			transplant(t, y, y.right)
			y.right = z.right
			y.right.parent = y
		}

		transplant(t, z, y)
		y.left = z.left
		y.left.parent = z.parent
	}

	z = nil

	t.height = getHeight(t)
}

func successor(x *Element) *Element {
	if x.right != nil {
		p := x.right
		for p.left != nil {
			p = p.left
		}

		return p
	} else {
		p := x
		q := x.parent
		for q != nil && p == q.right {
			p = q
			q = p.parent
		}

		return q
	}
}

func transplant(t *Tree, x, y *Element) {
	if x.parent == nil {
		t.root = y
	} else if x == x.parent.left {
		x.parent.left = y
	} else {
		x.parent.right = y
	}

	if y != nil {
		y.parent = x.parent
	}
}

func printTree(t *Tree) {
	fmt.Printf("size = %d, height = %d\n", t.size, t.height)

	if t.root != nil {
		printTreeInternal(t.root, 0)
	}
}

func printTreeInternal(r *Element, spaceSize int) {
	if r.left != nil {
		printTreeInternal(r.left, spaceSize+1)
	}

	fmt.Printf("%s", strings.Repeat("    ", spaceSize))
	fmt.Printf("%d\n", r.key)

	if r.right != nil {
		printTreeInternal(r.right, spaceSize+1)
	}
}

func getHeight(t *Tree) int {
	if t.root == nil {
		return 0
	}

	return getHeightInternal(t.root)
}

func getHeightInternal(r *Element) int {
	if r == nil {
		return -1
	}

	heightOfLeft := getHeightInternal(r.left)
	heightOfRight := getHeightInternal(r.right)
	if heightOfLeft > heightOfRight {
		return heightOfLeft + 1
	} else {
		return heightOfRight + 1
	}
}

func main() {
	t := Tree{0, 0, nil}

	put(&t, &Element{8, nil, nil, nil})
	put(&t, &Element{3, nil, nil, nil})
	put(&t, &Element{10, nil, nil, nil})
	put(&t, &Element{1, nil, nil, nil})
	put(&t, &Element{6, nil, nil, nil})
	put(&t, &Element{14, nil, nil, nil})
	put(&t, &Element{4, nil, nil, nil})
	put(&t, &Element{7, nil, nil, nil})
	put(&t, &Element{13, nil, nil, nil})

	for {
		fmt.Print("1:put 2:remove 3:print 4:successor > ")
		var op int
		fmt.Scanf("%d", &op)

		switch op {
		case 1:
			fmt.Print("input key > ")
			var data int
			fmt.Scanf("%d", &data)

			z := Element{data, nil, nil, nil}
			put(&t, &z)
		case 2:
			fmt.Print("input key > ")
			var key int
			fmt.Scanf("%d", &key)

			z := contains(&t, key)
			if z == nil {
				fmt.Printf("%d is not found in the tree.\n", key)
			} else {
				remove(&t, z)
			}
		case 3:
			printTree(&t)
		case 4:
			fmt.Print("input key > ")
			var key int
			fmt.Scanf("%d", &key)

			z := contains(&t, key)
			if z == nil {
				fmt.Printf("%d is not found in the tree.\n", key)
			} else {
				succ := successor(z)
				if succ != nil {
					fmt.Printf("successor = %d\n", succ.key)
				} else {
					fmt.Println("successor is not found.")
				}
			}
		default:
			fmt.Println("invalid operation")
		}
	}
}
