package main

import (
	"fmt"
	"math/rand"
	"sort"
)

type Hero struct {
	Name string
	Age int
}

type HeroSlice []Hero

func (hs HeroSlice) Len() int {
	return len(hs)
}

// less方法就是决定你用什么标准进行排序
// 按照年龄进行排序

func (hs HeroSlice) Less(i, j int) bool {
	return hs[i].Age < hs[j].Age
}

func (hs HeroSlice) Swap(i, j int) {
	hs[i], hs[j] = hs[j], hs[i]
}

func main() {
	// 数组切片排序
	var intSlice = []int{0, -1, 10, 7, 90}
	// 1. 冒泡排序
	// 2. 系统提供的方法排序
	sort.Ints(intSlice)
	fmt.Println(intSlice)

	// 结构体切片排序
	// 1. 冒泡排序
	// 2. 系统提供的方法排序
	var heros HeroSlice
	for i := 0; i < 10; i++ {
		hero := Hero{
			Name: fmt.Sprintf("英雄~%d", rand.Intn(100)),
			Age: rand.Intn(100),
		}
		heros = append(heros, hero)
	}

	for _, v := range heros {
		fmt.Println(v)
	}
	fmt.Println("排序后--------------------")
	sort.Sort(heros)
	for _, v := range heros {
		fmt.Println(v)
	}
}
