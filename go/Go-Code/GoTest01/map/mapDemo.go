package main

import (
	"fmt"
)

func main() {
	var a map[string]string
	a = make(map[string]string)
	a["no1"] = "宋江"
	a["no2"] = "吴用"
	fmt.Println(a)

	cities := make(map[string]string)
	cities["no1"] = "北京"
	cities["no2"] = "上海"
	cities["no3"] = "广州"
	fmt.Println(cities)
	delete(cities, "no1")
	fmt.Println(cities)
	fmt.Println(cities["no2"])

	for k, v := range cities {
		fmt.Println("key=", k, "value=", v)
	}

	heroes := map[string]string{
		"hero1": "宋江",
		"hero2": "卢俊义",
	}
	heroes["hero3"] = "林冲"
	fmt.Println(heroes)

	studentMap := make(map[string]map[string]string)
	studentMap["stu01"] = make(map[string]string)
	studentMap["stu01"]["name"] = "tom"
	studentMap["stu01"]["sex"] = "男"
	studentMap["stu01"]["address"] = "北京长安街~"
	studentMap["stu02"] = make(map[string]string)
	studentMap["stu02"]["name"] = "mary"
	studentMap["stu02"]["sex"] = "女"
	studentMap["stu02"]["address"] = "上海黄浦江~"
	fmt.Println(studentMap)
}
