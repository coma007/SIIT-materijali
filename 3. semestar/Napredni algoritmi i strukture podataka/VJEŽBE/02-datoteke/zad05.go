package main

import (
	"os"
)

func main() {

	info, err := os.Stat("copy.txt")
	if err != nil {
		panic(err)
	}
	file, _ := os.OpenFile("copy.txt", os.O_WRONLY, 0666)
	defer file.Close()
	position, _ := file.Seek(info.Size()/2, 0)
	_, err = file.WriteAt([]byte{10, 21, 103, 15}, position)
	if err != nil {
		return
	}

}
