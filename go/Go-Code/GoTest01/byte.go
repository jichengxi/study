package main

import "fmt"

func main() {
	var c1 byte = 'a'
	var c2 byte = '0'
	// 直接输出是ASCII码值
	fmt.Println("c1 =", c1)
	fmt.Println("c2 =", c2)
	// 输出字符需要格式化输出
	fmt.Printf("c1=%c c2=%c \n", c1, c2)

	// 中文是unicode，不能用byte
	var c3 int = '北'
	fmt.Printf("c3=%c 对应的码值是%d \n", c3, c3)

	var c4 int = 22269
	fmt.Printf("c4=%c \n", c4)

	var n1 = 10 + 'a'
	fmt.Println("n1=", n1)
}
