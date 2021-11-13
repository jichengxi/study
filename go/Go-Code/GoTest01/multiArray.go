package main

import "fmt"

func main() {
	var arr [4][6]int
	arr[1][2] = 1
	arr[2][1] = 2
	arr[2][3] = 3
	//fmt.Println(arr)
	for i := 0; i < 4; i++ {
		for j :=0; j < 6; j++ {
			fmt.Print(arr[i][j], " ")
		}
		fmt.Println()
	}

	// 遍历二维数组
	var arr2 [2][3]int = [2][3]int{{1, 2, 3}, {4, 5, 6}}
	for i := 0; i < len(arr2); i++ {
		for j := 0; j < len(arr2[i]); j++ {
			fmt.Print(arr2[i][j], " ")
		}
		fmt.Println()
	}

	for i, v := range arr2 {
		for i2, v2 := range v {
			fmt.Printf("arr2[%v][%v]=%v \n", i, i2, v2)
		}
	}
}
