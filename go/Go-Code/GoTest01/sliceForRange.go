package main

import "fmt"

func main() {
	var arr [5]int = [...]int{10, 20, 30, 40, 50}
	slice := arr[:]
	for i := 0; i < len(slice); i++ {
		fmt.Printf("slice[%v]=%v \n", i, slice[i])
	}

	for i, v := range slice {
		fmt.Printf("i=%v, v=%v \n", i, v)
	}

	slice2 := slice[1:2]
	fmt.Println("slice2=", slice2)
}
