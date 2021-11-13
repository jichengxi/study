package main

import "fmt"

func main() {
	for i:=0; i<=10; i++ {
		fmt.Println("你好-1", i)
	}

	j := 1
	for j <= 10 {
		fmt.Println("你好-2", j)
		j++
	}

	k := 1
	for {
		if k <= 10 {
			fmt.Println("你好-3", k)
		} else {
			break
		}
		k++
	}

	// 遍历字符串
	var str string = "hello,world!北京" // 传统方式 按照字节遍历
	str2 := []rune(str) // 把str 转换成 []rune
	for i :=0; i < len(str2); i++ {
		fmt.Printf("%c \n", str2[i])
	}

	str = "abc~ok上海"
	for index, val := range str {  // for range 按照字符遍历
		fmt.Printf("index=%d, val=%c \n", index, val)
	}
}
