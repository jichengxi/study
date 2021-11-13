package main

import "fmt"

func main() {
	// 基本数据类型在内存中的布局
	var i int = 10
	// i 的地址
	fmt.Println("i的内存地址=", &i)

	// 1. ptr是一个指针变量
	// 2. ptr的类型是 *int
	// 3. ptr 本身的值是 &i
	var ptr *int = &i
	fmt.Println("ptr=", ptr)
	fmt.Println("ptr指针本身的内存地址=", &ptr)
	fmt.Println("ptr指针指向的值=", *ptr)

}
