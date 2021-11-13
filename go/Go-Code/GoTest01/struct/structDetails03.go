package main

import (
	"encoding/json"
	"fmt"
)

type A struct {
	Num int
}

type B struct {
	Num int
}

type Monster struct {
	Name string `json:"name"`
	Age int `json:"age"`
	Skill string `json:"skill"`
}

func main() {
	var a A
	var b B
	b = B(a)
	fmt.Println(a, b)

	// 创建一个monster变量
	monster := Monster{"牛魔王", 500, "芭蕉扇"}
	// 将monster变量序列化为json字符串
	jsonStr, err := json.Marshal(monster)
	if err != nil {
		fmt.Println("err=", err)
	}
	fmt.Println("jsonStr=", string(jsonStr))

}
