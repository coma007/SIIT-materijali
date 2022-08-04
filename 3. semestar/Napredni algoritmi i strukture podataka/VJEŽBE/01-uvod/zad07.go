package main

import (
	"fmt"
	"reflect"
)

func anagram(word string, candidates []string) []string {

	var wordMap = make(map[string]int)
	var matches = make([]string, len(candidates), len(candidates))

	for _, l := range word {
		if wordMap[string(l)] >= 0 {
			wordMap[string(l)] += 1
		} else {
			wordMap[string(l)] = 1
		}
	}

	for _, v := range candidates {
		if len(v) == len(word) {
			var matchMap = make(map[string]int)
			for _, l := range v {
				if matchMap[string(l)] >= 0 {
					matchMap[string(l)] += 1
				} else {
					matchMap[string(l)] = 1
				}
			}
			if reflect.DeepEqual(matchMap, wordMap) {
				matches = append(matches, v)
			}
		}
	}

	return matches
}


func main() {

	fmt.Println(anagram("listen", []string{"enlists", "google", "inlets", "banana"}))

}
