package main

import "fmt"

func modify(map1 map[int]int) {
	map1[10] = 900
}

//定义一个学生的结构体
type Stu struct {
	Name string
	Age int
	Address string
}

func main() {
	map1 := make(map[int]int)
	map1[1] = 90
	map1[2] = 88
	map1[10] = 1
	map1[20] = 2
	modify(map1)
	fmt.Println(map1)

	students := make(map[string]Stu)
	stu1 := Stu{"tom", 10, "北京"}
	stu2 := Stu{"mary", 28, "上海"}
	students["no1"] = stu1
	students["no2"] = stu2
	fmt.Println(students)

	for k, v := range students {
		fmt.Println("学生的编号是", k)
		fmt.Println("学生的姓名是", v.Name)
		fmt.Println("学生的年龄是", v.Age)
		fmt.Println("学生的地址是", v.Address)
		fmt.Println()
	}
}
