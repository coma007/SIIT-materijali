package main

import (
	"encoding/gob"
	"fmt"
    "github.com/spaolacci/murmur3"
	"hash"
	"math"
	"os"
	"time"
)

type BloomFilter interface {
	Add()
	Query()
}

type BloomF struct {
	M     uint          // Velicina Set-a
	K     uint          // Broj hash funkcija
	P     float64       // False-positive vjerovatnoca
	Set   []byte        // Set sa bitovima
	hashs []hash.Hash32 // hash funkcije
	TimeConst uint
}

func Create(n uint, p float64) *BloomF {
	m := CalculateM(int(n), p)
	k := CalculateK(int(n), m)
	hashs, tc := CreateHashFunctions(k)
	bf := BloomF{m, k, p, make([]byte, m), hashs, tc}
	fmt.Printf("Created Bloom Filter with M = %d, K = %d\n", m, k)
	return &bf
}

func (bf *BloomF) Add(elem string) {
	for _, hashF := range bf.hashs {
		i := HashIt(hashF, elem, bf.M)
		bf.Set[i] = 1
	}
	fmt.Printf("Element %s added !\n", elem)
}

func (bf *BloomF) Query(elem string) bool {
	for _, hashF := range bf.hashs {
		i := HashIt(hashF, elem, bf.M)
		if bf.Set[i] != 1 {
			return false
		}
	}
	return true
}

func HashIt(hashF hash.Hash32, elem string, m uint) uint32 {
	_, err := hashF.Write([]byte(elem))
	if err != nil {
		panic(err)
	}
	i := hashF.Sum32() % uint32(m)
	hashF.Reset()
	return i
}

func CalculateM(expectedElements int, falsePositiveRate float64) uint {
	return uint(math.Ceil(float64(expectedElements) * math.Abs(math.Log(falsePositiveRate)) / math.Pow(math.Log(2), float64(2))))
}

func CalculateK(expectedElements int, m uint) uint {
	return uint(math.Ceil((float64(m) / float64(expectedElements)) * math.Log(2)))
}

func CreateHashFunctions(k uint) ([]hash.Hash32, uint) {
	var h []hash.Hash32
	ts := uint(time.Now().Unix())
	for i := uint(0); i < k; i++ {
		h = append(h, murmur3.New32WithSeed(uint32(ts+1)))
	}
	return h, ts
}

func CopyHashFunctions(k uint, tc uint) ([]hash.Hash32) {
	var h []hash.Hash32
	for i := uint(0); i < k; i++ {
		h = append(h, murmur3.New32WithSeed(uint32(tc+1)))
	}
	return h
}

func main() {

	bf := Create(30, 2)
	bf.Add("Bojan")
	bf.Add("Mićo")
	bf.Add("Katarina")
	bf.Add("Milica")
	bf.Add("Miloš")
	fmt.Println("\nNemanja ? ", bf.Query("Nemanja"))
	fmt.Println("Katarina ? ", bf.Query("Katarina"))
	bf.Add("Branko")
	bf.Add("Gaga")
	bf.Add("Djuro")
	bf.Add("Suncica")
	bf.Add("Ljupka")
	bf.Add("Krinka")
	bf.Add("Djole")
	bf.Add("Mirjana")
	bf.Add("Jovo")
	bf.Add("Dado")
	bf.Add("Mira")
	fmt.Println("\nNemanja ? ", bf.Query("Nemanja"))
	fmt.Println("Jovo ? ", bf.Query("Katarina"))

	fmt.Println("\nSerialization in progress ...")

	nwf, _ := os.Create("bf.gob")
	nwf.Close()

	file, _ := os.OpenFile("bf.gob", os.O_RDWR, 0666)
	defer file.Close()
	encoder := gob.NewEncoder(file)
	err := encoder.Encode(bf)
	if err != nil {
		fmt.Println(err)
	}

	decoder := gob.NewDecoder(file)
	var srs = new(BloomF)
	file.Seek(0, 0)
	for {
		err = decoder.Decode(srs)
		if err != nil {
			fmt.Println(err)
			break
		}
		fmt.Println(*srs)
	}
	srs.hashs = CopyHashFunctions(srs.K, srs.TimeConst)
	fmt.Println("\nNemanja ? ", srs.Query("Nemanja"))
	fmt.Println("Jovo ? ", srs.Query("Katarina"))
}
