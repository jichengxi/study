package main

import "fmt"

func main() {
	var intArr [5]int = [...]int{1, 22, 33, 66, 99}
	slice := intArr[1:3]
	fmt.Println("intArr=", intArr)
	fmt.Println("slice的元素是", slice)
	fmt.Println("slice的元素个数是", len(slice))
	fmt.Println("slice的容量是", cap(slice))

	fmt.Println("intArr[1]的地址=", &intArr[1])
	fmt.Println("slice[0]的地址=", &slice[0])
	slice[1] = 34
	fmt.Println("intArr=", intArr)
	fmt.Println("slice的元素是", slice)
}
