package main

import "fmt"




func main() {

	cityData := make(map[int]string)

	cityData[78400] = "Gradiška"
	cityData[21000] = "Novi Sad"
	cityData[11000] = "Beograd"
	cityData[78000] = "Banjaluka"
	cityData[89101] = "Trebinje"

	cities := make([]string, len(cityData), len(cityData))
	for k, v := range cityData {
		cities = append(cities, v)
		fmt.Println(k, ":", v)
	}
	fmt.Println(cities)

}