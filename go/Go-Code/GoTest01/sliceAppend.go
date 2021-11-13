package main

import "fmt"

func main() {
	var slice1 []int = []int{100, 200, 300}
	slice2 := append(slice1, 400, 500)
	fmt.Println("slice1=", slice1)
	fmt.Println("slice2=", slice2)
	slice3 := append(slice1, slice1...)
	fmt.Println("slice3=", slice3)

	var slice4 []int = []int{1, 2, 3, 4, 5}
	var slice5 = make([]int, 10)
	fmt.Println(slice5)
	copy(slice5, slice4)
	fmt.Println(slice5)
}
