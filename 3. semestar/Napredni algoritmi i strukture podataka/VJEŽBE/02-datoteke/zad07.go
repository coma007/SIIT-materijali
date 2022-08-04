package main

import (
	"encoding/binary"
	"fmt"
	"os"
)

type Triangle struct {
	Edge1, Edge2, Edge3 float32
}

func main() {

	t1 := Triangle{3, 4, 5}
	t2 := Triangle{2, 2, 3}
	t3 := Triangle{4, 4, 7}
	t4 := Triangle{5, 5, 7}
	t5 := Triangle{3, 2, 4}

	ts := make([]Triangle, 0, 3)
	ts = append(ts, t1, t2, t3, t4, t5)
	fmt.Println("All triangles: ", ts)

	nwf, _ := os.Create("triangles.binary")
	nwf.Close()

	file, err := os.OpenFile("triangles.binary", os.O_RDWR, 0666)
	defer file.Close()
	if err != nil {
		panic(err.Error())
	}
	defer file.Close()

	for i := 0; i < len(ts); i++ {
		err := binary.Write(file, binary.LittleEndian, ts[i])
		if err != nil {
			return
		}
	}

	nwt := &Triangle{}
	file.Seek(12, 0)
	err = binary.Read(file, binary.LittleEndian, nwt)
	if err != nil {
		panic(err.Error())
	}
	fmt.Println("Second triangle before change: ", *nwt)

	nwt.Edge1 *= 2
	nwt.Edge2 *= 2
	nwt.Edge3 *= 2
	fmt.Println("Second triangle after change: ", *nwt)
	file.Seek(12, 0)
	err = binary.Write(file, binary.LittleEndian, nwt)

	triangles := make([]Triangle, 0, 2)
	for i := len(ts) - 2; i < len(ts) ; i++ {
		file.Seek(int64(i*12), 0)
		tr := &Triangle{}
		err = binary.Read(file, binary.LittleEndian, tr)
		if err != nil {
			panic(err.Error())
		}
		triangles = append(triangles, *tr)
	}

	fmt.Println("Last two triangles: ", triangles)



}