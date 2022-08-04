package main

import (
	"fmt"
	"os"
)

func main() {

	var info os.FileInfo = nil
	if _, err := os.Stat("go.mod"); err != nil {
		if os.IsNotExist(err) {
			_, _ = os.Create("go.txt")
			info, _ = os.Stat("go.txt")
		}
	} else {
		info, err = os.Stat("go.mod")
		if err != nil {
			panic(err)
		}
	}
	fmt.Println("Size: ", info.Size())
	fmt.Println("Last modified: ", info.ModTime())

}