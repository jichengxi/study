package main

import "fmt"

func bubbleSort(arr *[5]int) {
	fmt.Println("排序前的arr=", *arr)
	fmt.Println(len(*arr) - 1)

	for i := 0; i < (len(arr) - 1); i ++ {
		for j := 0; j < (len(arr) - 1 - i); j++ {
			if (*arr)[j] > (*arr)[j + 1] {
				(*arr)[j], (*arr)[j + 1] = (*arr)[j + 1], (*arr)[j]
			}
		}
	}
	fmt.Println("排序后的arr=:", *arr)
}

func main() {
	// 定义一个数组
	arr := [5]int{24, 69, 80, 57, 13}
	// 将数组传递给一个函数完成排序
	bubbleSort(&arr)
}
