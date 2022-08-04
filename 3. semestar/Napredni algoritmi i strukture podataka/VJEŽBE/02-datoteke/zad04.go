package main

import (
	"fmt"
	"os"
)

func readByte(filename string, position int64) byte {

	file, _ := os.OpenFile(filename, os.O_RDONLY, 0666)
	defer file.Close()

	num, _ := file.Seek(position, 0)
	bytes := make([]byte, 1)
	_, _ = file.ReadAt(bytes, num)
	fmt.Println(fmt.Sprintf("%x", bytes[0]))

	return bytes[0]

}

func main() {

	n, m := readByte("copy.txt", 5), readByte("copy.txt", 3)
	fmt.Println("Sum n + p =", n + m)

}
