package main

import "os"

func main() {

	file, _ := os.OpenFile("copy.txt", os.O_WRONLY, 0666)
	defer file.Close()
	_, err := file.WriteAt([]byte{0}, 3)
	if err != nil {
		return
	}

}