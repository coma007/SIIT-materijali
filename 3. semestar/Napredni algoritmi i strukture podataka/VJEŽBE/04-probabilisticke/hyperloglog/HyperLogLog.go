package main

import(
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"math"
)

const (
	HLL_MIN_PRECISION = 4
	HLL_MAX_PRECISION = 16
)

type HyperLogLog interface {
	emptyCount()
	Add()
	Estimate()
}

type HLL struct {
	m   uint64
	p   uint8
	reg []uint8
}

func (hll *HLL) emptyCount() uint8 {
	sum := uint8(0)
	for _, val := range hll.reg {
		if val == 0 {
			sum++
		}
	}
	return sum
}

func Create(p uint8) HLL {
	m := int(math.Pow(2, float64(p)))
	return HLL{uint64(m),p, make([]uint8, m, m)}
}

func (hll *HLL) Add(word string) {
	bin := ToBinary(GetMD5Hash(word))
	key := 0
	p := hll.p
	for i := 0; i < int(p); i++ {
		key +=  (int(bin[i]) - '0') * int(math.Pow(2, float64(int(p) - i)))
	}
	val := 0
	for i := len(bin) - 1; i > 0; i-- {
		if bin[i] == '0' {
			val++
		} else {
			break
		}
	}
	hll.reg[key] = uint8(val)

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

func (hll *HLL) Estimate() float64 {
	sum := 0.0
	for _, val := range hll.reg {
		sum = sum + math.Pow( float64(-val), 2.0) // ovo promijenih !!
	}

	alpha := 0.7213 / (1.0 + 1.079/float64(hll.m))
	estimation := alpha * math.Pow(float64(hll.m), 2.0) / sum
	emptyRegs := hll.emptyCount()
	if estimation < 2.5*float64(hll.m) { // do small range correction
		if emptyRegs > 0 {
			estimation = float64(hll.m) * math.Log(float64(hll.m)/float64(emptyRegs))
		}
	} else if estimation > math.Pow(2.0, 32.0)/30.0 { // do large range correction
		estimation = -math.Pow(2.0, 32.0) * math.Log(1.0-estimation/math.Pow(2.0, 32.0))
	}
	return estimation
}

func main() {

	//fmt.Println(int('1' - '0'))
	//fmt.Println(ToBinary(GetMD5Hash("nice")))
	hll := Create(6)
	hll.Add("Bojan")
	hll.Add("Bojan")
	hll.Add("Ica")
	hll.Add("Bojan")
	hll.Add("Bojan")
	hll.Add("Mica")
	hll.Add("Mica")
	hll.Add("Tica")
	hll.Add("Mica")
	hll.Add("Jeca")
	hll.Add("Katarina")
	hll.Add("Jelena")
	hll.Add("Katarina")
	hll.Add("Ivan")
	fmt.Println(hll.Estimate())
}
