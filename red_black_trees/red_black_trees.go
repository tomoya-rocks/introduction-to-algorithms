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
	color  int // 0:red, 1:black
}

type Tree struct {
	size   int
	height int
	root   *Element
}

var sentinel *Element

func nilElement() *Element {
	if sentinel == nil {
		sentinel = &Element{-1, nil, nil, nil, 1}
	}

	return sentinel
}

func (t *Tree) put(z *Element) {
	t.size += 1

	var x *Element = t.root
	var y *Element = nilElement()
	for x != nilElement() {
		y = x
		if z.key < x.key {
			x = x.left
		} else {
			x = x.right
		}
	}

	z.parent = y
	z.left = nilElement()
	z.right = nilElement()
	if y == nilElement() {
		t.root = z
	} else {
		if z.key < y.key {
			y.left = z
		} else {
			y.right = z
		}
	}

	t.fixAfterInsertion(z)

	t.height = t.getHeight()
}

func (t *Tree) rotateLeft(x *Element) {
	y := x.right
	x.right = y.left
	if y.left != nilElement() {
		y.left.parent = x
	}

	y.parent = x.parent
	if x.parent == nilElement() {
		t.root = x
	} else if x == x.parent.left {
		x.parent.left = y
	} else {
		x.parent.right = y
	}

	y.left = x
	x.parent = y
}

func (t *Tree) rotateRight(x *Element) {
	y := x.left
	x.left = y.right
	if y.right != nilElement() {
		y.right.parent = x
	}

	y.parent = x.parent
	if x.parent == nilElement() {
		t.root = x
	} else if x == x.parent.left {
		x.parent.left = y
	} else {
		x.parent.right = y
	}

	y.right = x
	x.parent = y
}

func (t *Tree) fixAfterInsertion(z *Element) {
	for z.parent.color == 0 {
		if z.parent == z.parent.parent.left {
			y := z.parent.parent.right
			if y.color == 0 {
				// case 1
				z.parent.color = 1
				y.color = 1
				z.parent.parent.color = 0
				z = z.parent.parent
			} else {
				if z == z.parent.right {
					// case 2
					z = z.parent
					t.rotateLeft(z)
				}

				// case 3
				z.parent.color = 1
				z.parent.parent.color = 0
				t.rotateRight(z.parent.parent)
			}
		} else {
			y := z.parent.parent.left
			if y.color == 0 {
				// case 1
				z.parent.color = 1
				y.color = 1
				z.parent.parent.color = 0
				z = z.parent.parent
			} else {
				if z == z.parent.left {
					// case 2
					z = z.parent
					t.rotateRight(z)
				}

				// case 3
				z.parent.color = 1
				z.parent.parent.color = 0
				t.rotateLeft(z.parent.parent)
			}
		}
	}

	t.root.color = 1
}

func (t *Tree) contains(key int) *Element {
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

func (t *Tree) remove(z *Element) {
	t.size -= 1

	if z.left == nil {
		t.transplant(z, z.right)
	} else if z.right == nil {
		t.transplant(z, z.left)
	} else {
		y := t.successor(z)
		if y != z.right {
			t.transplant(y, y.right)
			y.right = z.right
			y.right.parent = y
		}

		t.transplant(z, y)
		y.left = z.left
		y.left.parent = z.parent
	}

	z = nil

	t.height = t.getHeight()
}

func (t *Tree) successor(x *Element) *Element {
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

func (t *Tree) transplant(x, y *Element) {
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

func (t *Tree) printTree() {
	fmt.Printf("size = %d, height = %d\n", t.size, t.height)

	if t.root != nilElement() {
		t.printTreeInternal(t.root, 0)
	}
}

func (t *Tree) printTreeInternal(r *Element, spaceSize int) {
	if r.left != nilElement() {
		t.printTreeInternal(r.left, spaceSize+1)
	}

	fmt.Printf("%s", strings.Repeat("    ", spaceSize))
	fmt.Printf("%d(", r.key)
	if r.color == 0 {
		fmt.Print("RED)")
	} else {
		fmt.Print("BLACK)")
	}
	fmt.Println()

	if r.right != nilElement() {
		t.printTreeInternal(r.right, spaceSize+1)
	}
}

func (t *Tree) getHeight() int {
	if t.root == nilElement() {
		return 0
	}

	return t.getHeightInternal(t.root)
}

func (t *Tree) getHeightInternal(r *Element) int {
	if r == nilElement() {
		return -1
	}

	heightOfLeft := t.getHeightInternal(r.left)
	heightOfRight := t.getHeightInternal(r.right)
	if heightOfLeft > heightOfRight {
		return heightOfLeft + 1
	} else {
		return heightOfRight + 1
	}
}

func main() {
	t := Tree{0, 0, nilElement()}

	for {
		fmt.Print("1:put 2:remove 3:print 4:successor > ")
		var op int
		fmt.Scanf("%d", &op)

		switch op {
		case 1:
			fmt.Print("input key > ")
			var data int
			fmt.Scanf("%d", &data)

			z := Element{data, nil, nil, nil, 0}
			t.put(&z)
		case 2:
			fmt.Print("input key > ")
			var key int
			fmt.Scanf("%d", &key)

			z := t.contains(key)
			if z == nil {
				fmt.Printf("%d is not found in the tree.\n", key)
			} else {
				t.remove(z)
			}
		case 3:
			t.printTree()
		case 4:
			fmt.Print("input key > ")
			var key int
			fmt.Scanf("%d", &key)

			z := t.contains(key)
			if z == nil {
				fmt.Printf("%d is not found in the tree.\n", key)
			} else {
				succ := t.successor(z)
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
