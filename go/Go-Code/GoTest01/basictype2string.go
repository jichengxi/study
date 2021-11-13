package main

import (
	"fmt"
	"strconv"
)

func main() {
	//var num1 int = 99
	//var num2 float64 = 23.456
	//var b1 bool = true
	//var myChar byte = 'h'

	// 第一种方式，使用fmt.Sprintf方法转化
	//strNum1 := fmt.Sprintf("%d", num1)
	//fmt.Printf("str type %T str=%q \n", strNum1, strNum1)
	//
	//strNum2 := fmt.Sprintf("%f", num2)
	//fmt.Printf("str type %T str=%q \n", strNum2, strNum2)
	//
	//strB1 := fmt.Sprintf("%t", b1)
	//fmt.Printf("str type %T str=%q \n", strB1, strB1)
	//
	//strChar1 := fmt.Sprintf("%c", myChar)
	//fmt.Printf("str type %T str=%q \n", strChar1, strChar1)

	// 第二种方法， 使用strconv函数
	var num3 int = 80
	var num4 float64 = 23.567
	var b2 bool = true

	strNum3 := strconv.FormatInt(int64(num3), 10)
	fmt.Printf("str type %T str=%q \n", strNum3, strNum3)

	strNum4 := strconv.FormatFloat(num4, 'f', 10, 64)
	fmt.Printf("str type %T str=%q \n", strNum4, strNum4)

	strB2 := strconv.FormatBool(b2)
	fmt.Printf("str type %T str=%q \n", strB2, strB2)

	var num5 int = 4567
	strNum5 := strconv.Itoa(num5)
	fmt.Printf("str type %T str=%q \n", strNum5, strNum5)
}
