package main

import (
	"bufio"
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"log"
	"os"
	"strings"
)

func makeStopWords() map[string]bool{
	stopWords := []string{"A", "About", "Actually", "Almost", "Also", "Although" ,"Always","Am","An","And","Any","Are",
		"As","At","Be","Became" ,"Become","But","By","Can","Could","Did","Do","Does","Each","Either","Else","For",
		"From","Had","Has","Have","Hence" ,"How","I","If","In","IS","IT","ITS","JUST","MAY","MAYBE","Me","Might",
		"Mine","Must","My","Neither","Nor","Not","Of","Oh","Ok","When","Where", "Whereas","Wherever","Whenever",
		"Whether","Which","While","Who","Whom","Whoever","Whose", "Why", "Will","With", "Within", "Without",
		"Would", "Yes", "Yet", "You", "Your"}
	stopWordsMap := make(map[string]bool)
	for _, word := range stopWords {
		stopWordsMap[strings.ToUpper(word)] = true
	}
	return stopWordsMap
}

type SimHash struct {
	stopWords map[string]bool
}

func (*SimHash) Hemingway(t1 Text, t2 Text) int {
	arr1 := t1.arr
	arr2 := t2. arr
	arr := make([]int, 256, 256)

	for i := 0; i < 256; i++ {
		arr[i] = arr1[i] ^ arr2[i]
	}

	res := 0
	for _, v := range arr {
		if v == 1 {
			res++
		}
	}
	return res
}

func CreateSimHash() SimHash{
	stopWords := makeStopWords()
	return SimHash{stopWords}
}

type Text struct {
	arr []int
}

func CreateText (filename string, sh SimHash) Text {
	words := ParseText(filename, sh)
	hashed := HashWords(words)
	arr := SumHashs(hashed)
	return Text{arr}
}

func ParseText(filename string, sh SimHash) map[string]int {
	all := make(map[string]int)
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanWords)
	for scanner.Scan() {
		if sh.stopWords[scanner.Text()] == false {
			all[strings.ToUpper(scanner.Text())] += 1
		}
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return all
}

func HashWords(words map[string]int) map[int]string {

	hash := make(map[int]string)
	for word, _ := range words {
		hash[words[word]] = ToBinary(GetMD5Hash(word))
	}
	return hash
}

func SumHashs(hashs map[int]string) []int {

	arr := make([]int, 256, 256)
	for sig, hash := range hashs {
		for i := 0; i < len(hash); i++ {
			if hash[i] == '1' {
				arr[i] += sig
			} else {
				arr[i] -= sig
			}
		}
	}
	for i, val := range arr {
		if val > 0 {
			arr[i] = 1
		} else {
			arr[i] = 0
		}
	}
	return arr
}

func GetMD5Hash(text string) string {
	hash := md5.Sum([]byte(text))
	return hex.EncodeToString(hash[:])
}

func ToBinary(s string) string {
	res := ""
	for _, c := range s {
		res = fmt.Sprintf("%s%.8b", res, c)
	}
	return res
}
//
//func main() {
//	//fmt.Println((GetMD5Hash("hello")))
//	//fmt.Println(len(ToBinary(GetMD5Hash("hello"))))
//
//	sh := CreateSimHash()
//	t1 := CreateText("sim-hash/tekst1.txt", sh)
//	t2 := CreateText("sim-hash/tekst2.txt", sh)
//	t3 := CreateText("sim-hash/tekst3.txt", sh)
//	t4 := CreateText("sim-hash/tekst4.txt", sh)
//	fmt.Println(sh.Hemingway(t1, t2))
//	fmt.Println(sh.Hemingway(t3, t4))
//}
