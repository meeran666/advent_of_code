package main

import (
	"fmt"
	"math"
	"os"
	"path/filepath"
	"slices"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}
func push_in_str(i int, slice []byte, len int) (string, int) {
	temp_str := ""
	for string(slice[i]) != " " && string(slice[i]) != "\n" {
		temp_str = temp_str + string(slice[i])
		i++
		if i >= len {
			break
		}
	}
	return temp_str, i
}
func main() {
	// 	input_str := `3   4
	// 4   3
	// 2   5
	// 1   3
	// 3   9
	// 3   3`
	// 	input := []byte(input_str)
	current_directory, err := os.Getwd()
	check(err)
	file_path := filepath.Join(current_directory, "advent_of_code_2024/Day1/input.txt")
	input, err := os.ReadFile(file_path)
	check(err)
	_ = input
	arr1 := []int{}
	_ = arr1
	arr2 := []int{}
	_ = arr2

	len := len(input)
	len_arr1 := 0
	i := 0
	for i < len {
		len_arr1++
		//finding first integer value in line
		str1, index1 := push_in_str(i, input, len)
		int1, err := strconv.Atoi(str1)
		check(err)
		arr1 = append(arr1, int1)
		i = index1
		i = i + 3

		//finding first integer value in line
		str2, index2 := push_in_str(i, input, len)
		int2, err := strconv.Atoi(str2)
		check(err)
		arr2 = append(arr2, int2)
		i = index2
		i++
	}
	slices.Sort(arr1)
	slices.Sort(arr2)
	total := 0
	for i := range len_arr1 {
		dif := arr1[i] - arr2[i]
		total = total + int(math.Abs(float64(dif)))
	}
	// fmt.Println(total)

	//2nd part
	total = 0
	for i1, v1 := range arr1 {
		_ = i1
		count := 0
		for i2, v2 := range arr2 {
			_ = i2
			if v1 == v2 {
				count++
			}
		}
		total = total + (v1 * count)
	}
	fmt.Println(total)
}
