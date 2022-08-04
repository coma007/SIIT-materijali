package main

import (
	"fmt"
	"gopkg.in/yaml.v2"
	"io/ioutil"
	"log"
)

type Config struct {
	WalSize uint64  	`yaml:"wal_size"`
	MemtableSize uint64	`yaml:"memtable_size"`
	Threshold uint8 	`yaml:"threshold"`
}

func main() {
	var config Config
	configData, err := ioutil.ReadFile("config.yml")
	if err != nil {
		log.Fatal(err)
	}
	yaml.Unmarshal(configData, &config)
	fmt.Println(config)
	marshalled, err := yaml.Marshal(config)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(marshalled))
}
