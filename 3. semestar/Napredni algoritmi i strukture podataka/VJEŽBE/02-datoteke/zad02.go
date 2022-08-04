package main

import (
	"fmt"
	"io"
	"os"
)

func createFile(filename string) *os.File{

	file, err := os.Create(filename)
	if err != nil {
		panic(err)
	}

	return file
}

func report(bytes int, filename string) {
	fmt.Printf("\nWrote %d bytes into file %s", bytes, filename)
}

func main() {

	var filename = "new.txt"
	file := createFile(filename)
	file.Close()
	file, _ = os.OpenFile(filename, os.O_WRONLY, 0666)
	towrite := []byte("Hello world !")
	bytesw, _ := file.Write(towrite)
	err := file.Close()
	if err != nil {
		panic(err)
	}
	report(bytesw, filename)

	var copyn = "copy.txt"
	file, _ = os.Open(filename)
	copyf := createFile(copyn)
	bytesc, _ := io.Copy(copyf, file)
	err = copyf.Close()
	if err != nil {
		panic(err)
	}
	err = file.Close()
	if err != nil {
		panic(err)
	}
	report(int(bytesc), copyn)

	err = os.Remove(filename)
	if err != nil {
		panic(err)
	}
}
