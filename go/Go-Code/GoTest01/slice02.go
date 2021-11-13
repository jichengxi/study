package main

import "fmt"

func main() {
	var slice1 []float64 = make([]float64, 5, 10)
	fmt.Println(slice1)
	slice1[1] = 10
	slice1[3] = 20
	fmt.Println(slice1)

	var slice2 []string = []string{"tom", "jack", "mary"}
	fmt.Println(slice2)
	slice2[1] = "jcx"
	slice2[2] = "jcx11"
	fmt.Println(slice2)
}
