package main

import "fmt"

// 把函数赋值给一个变量, 该变量也可以调用方法
func getSum(n1 int, n2 int) int {
	return n1 + n2
}

// 函数也是一种数据类型, 因此可以作为参数传入, 并且调用
func myFunc(func1 func(int, int) int, num1 int, num2 int) int {
	return func1(num1, num2)
}

type myFuncType func(int, int) int
func myFunc2(func1 myFuncType, num1 int, num2 int) int {
	return func1(num1, num2)
}

// 函数返回值重命名
func gerSumAndSub(n1 int, n2 int) (sum int, sub int) {
	sum = n1 + n2
	sub = n1 - n2
	return
}


func main() {
	a := getSum
	fmt.Printf("a的类型是%T, getSum的类型是%T \n", a, getSum)
	res := a(10, 20)
	fmt.Println("res=", res)

	res2 := myFunc(getSum, 20, 40)
	fmt.Println("res2=", res2)

	// 自定义数据类型
	type myInt int
	var num1 myInt
	num1 = 40
	fmt.Println("num1=", num1)

	res3 := myFunc2(getSum, 100, 40)
	fmt.Println("res3=", res3)

	sum1, sub1 := gerSumAndSub(100, 40)
	fmt.Printf("sum1=%v, sub1=%v \n", sum1, sub1)
}
