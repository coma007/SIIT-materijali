package main

import (
	"fmt"
	"crypto/sha1"
	"encoding/hex"
)

type MerkleRoot struct {
	root *Node
}

func (mr *MerkleRoot) String() string{
	return mr.root.String()
}

type Node struct {
	data []byte
	left *Node
	right *Node
}

func (n *Node) String() string {
	return hex.EncodeToString(n.data[:])
}

func Hash(data []byte) [20]byte {
	return sha1.Sum(data)
}

func main(){

}
