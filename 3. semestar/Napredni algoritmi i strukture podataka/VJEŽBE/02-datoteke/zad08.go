package main

import (
	"encoding/gob"
	"fmt"
	"os"
)

type Sport struct {
	Name string
	isTeam bool
	MatchDuration int16
}

func main() {

	s1 := Sport{"waterpolo", true, 40}
	s2 := Sport{"basketball", true, 40}
	s3 := Sport{"football", true, 90}

	ss := make([]Sport, 0, 3)
	ss = append(ss, s1, s2, s3)
	fmt.Println("All sports: ", ss)

	// Serijalizacija slice-a

	fmt.Println("\nSerialization of slice in progress ...")

	nwfs, _ := os.Create("sports.gob")
	nwfs.Close()

	file, _ := os.OpenFile("sports.gob", os.O_RDWR, 0666)
	defer file.Close()
	encoder := gob.NewEncoder(file)
	err := encoder.Encode(ss)
	if err != nil {
		fmt.Println(err)
	}

	// Serijalizacija pojedinacnih objekata

	fmt.Println("\nSerialization one by one in progress ...")

	nwf, _ := os.Create("sports2.gob")
	nwf.Close()

	file2, _ := os.OpenFile("sports2.gob", os.O_RDWR, 0666)
	defer file2.Close()

	encoder2 := gob.NewEncoder(file2)
	for i := 0 ; i < len(ss) ; i++ {
		err := encoder2.Encode(ss[i])
		if err != nil {
			fmt.Println(err)
		}
	}

	// Deserijalizacija iz slice serijalizacije

	fmt.Println("\nDeserializtion of first from slice")

	decoder := gob.NewDecoder(file)
	var srs = new(Sport)
	file.Seek(0, 0)
	for {
		err = decoder.Decode(srs)
		if err != nil {
			fmt.Println(err)
			break
		}
		fmt.Println(*srs)
	}

	// Deserijalizacija iz pojedinacne serijalizacije

	fmt.Println("\nDeserialization of the first in one by one")

	decoder2 := gob.NewDecoder(file2)
	var sr = new(Sport)
	file2.Seek(0, 0)

	err = decoder2.Decode(sr)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(*sr)

	// Pravilna deserijalizacija

	fmt.Println("\nCorrect deserialization of slice")

	decoder = gob.NewDecoder(file)
	var ssd = make([]Sport, 0, 3)
	file.Seek(0, 0)
	for {
		err = decoder.Decode(&ssd)
		if err != nil {
			fmt.Println(err)
			break
		}
		fmt.Println(ssd)
	}
	for i := 0; i < len(ssd) ; i++ {
		fmt.Println(ssd[i])
	}

	fmt.Println("\nCorrect deserialization of one by one")

	decoder2 = gob.NewDecoder(file2)
	var s = new(Sport)
	file2.Seek(0, 0)
	for {
		err = decoder2.Decode(s)
		if err != nil {
			fmt.Println(err)
			break
		}
		fmt.Println(*s)
	}

}