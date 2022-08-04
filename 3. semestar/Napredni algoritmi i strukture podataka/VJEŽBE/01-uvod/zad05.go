package main

import "fmt"

type Student struct {
	fname, lname, index string
}

func changeIndex(s *Student, i string) {
	s.index = i
}


func main() {

	var me = Student{"Milica", "Sladaković", "SV 18/2020"}
	fmt.Println(me)

	changeIndex(&me, "SV 57/2020")
	fmt.Println(me)


}
