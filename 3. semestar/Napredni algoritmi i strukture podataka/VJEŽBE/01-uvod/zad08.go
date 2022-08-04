package main

import (
	"errors"
	"fmt"
	"math"
)

type Node struct {
	data interface{}
	next *Node
}

func createNode(data interface{}) Node {
	node := Node{}
	node.data = data
	node.next = nil
	return node
}

type ListInterface interface {
	addEnd(node *Node)
	addAt(index int, node *Node) error
	removeAt(index int) error
	Print()
	findNode(value interface{}) float64
}

type LinkedList struct {
	head, tail *Node
	len int
}

func createLinkedList(head *Node) LinkedList {
	lst := LinkedList{}
	lst.head = head
	lst.tail = head
	lst.len = 1
	return lst
}

func (list *LinkedList) addEnd(node *Node) {
	list.tail.next = node
	list.tail = node
	list.len += 1
	fmt.Println(list.len)
}

func (list *LinkedList) addAt(index int, node *Node) error {
	if index >= list.len {
		return errors.New("index out of range")
	}
	current := list.head
	i := 0
	for current != nil {
		if index == i+1 {
			node.next = current.next
			current.next = node
			list.len += 1
			break
		}
		current = current.next
		i++
	}
	return nil
}

func (list *LinkedList) removeAt(index int) error {
	if index < 0 {
		index += list.len
	}
	if index >= list.len {
		return errors.New("index out of range")
	}
	if index == 0 {
		list.head = list.head.next
		return nil
	}
	i := 0
	current := list.head
	for current != nil {
		//fmt.Println(index, i)
		if index == i+1 {
			if current.next == list.tail {
				list.tail = current
				current.next = nil
			} else {
				current.next = current.next.next
			}
			list.len -= 1
			break
		}
		current = current.next
		i++
	}
	list.tail = current
	return nil
}

func (list *LinkedList) findNode(value interface{}) float64 {

	current := list.head
	i := 0.0
	for current != nil {
		if value == current.data {
			return i
		}
		current = current.next
		i++
	}
	return math.Inf(1)
}

func (list LinkedList)Print() {
	fmt.Print("[")
	current := list.head
	i := -1
	for current != nil {
		fmt.Print(current.data, " ")
		current = current.next
		i++
	}
	fmt.Print("]\n")


}


func main() {

	n1 := createNode("Bojan")
	var tmp = createLinkedList(&n1)
	var lst ListInterface = &tmp
	lst.Print()

	n2 := createNode("Miloš")
	lst.addEnd(&n2)
	lst.Print()

	n3 := createNode("Milica")
	err := lst.addAt(1, &n3)
	if err != nil {
		fmt.Println("Error :", err.Error())
		return
	}
	lst.Print()

	n4 := createNode("Đole")
	lst.addEnd(&n4)
	lst.Print()

	err = lst.removeAt(3)
	if err != nil {
		fmt.Println("Error :", err.Error())
		return
	}
	lst.Print()

	fmt.Println("Miloš at index:", lst.findNode("Miloš"))
	fmt.Println("Katarina at index:", lst.findNode("Katarina"))

	n5 := createNode("Katarina")
	err = lst.addAt(5, &n5)
	if err != nil {
		fmt.Println("Error :", err.Error())
		return
	}
	lst.Print()


}
