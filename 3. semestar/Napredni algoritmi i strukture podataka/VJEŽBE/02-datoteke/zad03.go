package main

import (
	"fmt"
	"io"
	"os"
)

func main() {

	file, _ := os.OpenFile("copy.txt", os.O_RDONLY, 0666)
	bytes := make([]byte, 3)
	_, err := io.ReadFull(file, bytes)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(bytes))

}
