package main

import "fmt"

func cal(n1 float64, n2 float64, operator byte) float64 {
	var res float64
	switch operator {
		case '+':
			res = n1 + n2
		case '-':
			res = n1 - n2
		case '*':
			res = n1 * n2
		case '/':
			res = n1 / n2
		default:
			fmt.Println("操作符号错误...")
	}
	return res
}

func main() {
	result := cal(12.0, 11.0, '+' )
	fmt.Println(result)
}
