package main

import "fmt"

func main() {
	var age int
	fmt.Println("请输入年龄:")
	fmt.Scanln(&age)
	if age > 18 {
		fmt.Println("你年龄大于18")
	} else if age < 18 && age > 14 {
		fmt.Println("你年龄小于18大于14")
	} else {
		fmt.Println("你年龄小于14")
	}
	//if age :=20; age > 18 {
	//	fmt.Println("你年龄大于18, 要对自己的年龄负责!")
	//}
}
