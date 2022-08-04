package main

import (
	"fmt"
	"github.com/spaolacci/murmur3"
	"hash"
	"math"
	"time"
)

type CountMinSketch interface {
	Add()
	Query()
}

type CountMS struct {
	M     uint          // Velicina Set-a
	K     uint          // Broj hash funkcija
	E     float64       // Preciznost
	D     float64 		// Tacnost
	Set   [][]int      // Set sa bitovima
	hashs []hash.Hash32 // hash funkcije
	TimeConst uint
}

func Create(p float64, d float64) *CountMS {
	m := CalculateM(p)
	k := CalculateK(d)
	hashs, tc := CreateHashFunctions(k)
	set := make([][]int, k)
	for i, _ := range set {
		set[i] = make([]int, m)
	}
	bf := CountMS{m, k, p, d, set, hashs, tc}
	fmt.Printf("Created Count Min Skatch with M = %d, K = %d\n", m, k)
	return &bf
}

func (cms *CountMS) Add(elem string) {
	for i, hashF := range cms.hashs {
		j := HashIt(hashF, elem, cms.M)
		cms.Set[i][j] += 1
	}
	fmt.Printf("Element %s added !\n", elem)
}

func (cms *CountMS) Query(elem string) int {
	values := make([]int, cms.K)
	for i, hashF := range cms.hashs {
		j:= HashIt(hashF, elem, cms.M)
		values[i] = cms.Set[i][j]
	}
	min := values[0]
	for _, v := range values {
		if v < min {
			min = v
		}
	}
	return min
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

func CalculateM(epsilon float64) uint {
	return uint(math.Ceil(math.E / epsilon))
}

func CalculateK(delta float64) uint {
	return uint(math.Ceil(math.Log(math.E / delta)))
}

func CreateHashFunctions(k uint) ([]hash.Hash32, uint) {
	var h []hash.Hash32
	ts := uint(time.Now().Unix())
	for i := uint(0); i < k; i++ {
		h = append(h, murmur3.New32WithSeed(uint32(ts+1)))
	}
	return h, ts
}

func main() {

	bf := Create(0.1, 0.01)
	bf.Add("Bojan")
	bf.Add("Mićo")
	bf.Add("Nemanja")
	bf.Add("Branko")
	bf.Add("Miloš")
	bf.Add("Bojan")
	bf.Add("Mićo")
	bf.Add("Nemanja")
	bf.Add("Branko")
	bf.Add("Miloš")
	fmt.Println("\nNemanja ? ", bf.Query("Nemanja"))
	fmt.Println("Branko ? ", bf.Query("Branko"))
	bf.Add("Nemanja")
	bf.Add("Gaga")
	bf.Add("Djuro")
	bf.Add("Suncica")
	bf.Add("Suncica")
	bf.Add("Jovo")
	bf.Add("Jovo")
	bf.Add("Jovo")
	bf.Add("Suncica")
	bf.Add("Suncica")
	bf.Add("Branko")
	bf.Add("Nemanja")
	bf.Add("Gaga")
	bf.Add("Djuro")
	bf.Add("Suncica")
	bf.Add("Suncica")
	bf.Add("Jovo")
	bf.Add("Jovo")
	bf.Add("Jovo")
	bf.Add("Suncica")
	bf.Add("Suncica")
	bf.Add("Branko")
	fmt.Println("\nSuncica ? ", bf.Query("Suncica"))
	fmt.Println("Jovo ? ", bf.Query("Jovo"))

}