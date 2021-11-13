package main

import "fmt"

func main() {
	var address string = "北京长城 110 Hello World"
	fmt.Println(address)

	var str = "hello"
	str = "1"
	fmt.Println(str)

	str1 := `
	中国
	长城
	`
	fmt.Println(str1)
}
