package main

import (
	"fmt"
	"math"
	"os"
	"path/filepath"
	"slices"
	"sort"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}
func check_dif(int_slice []int) bool {
	for index := 0; index < len(int_slice)-1; index++ {
		if !(math.Abs(float64(int_slice[index]-int_slice[index+1])) >= 1 && math.Abs(float64(int_slice[index]-int_slice[index+1])) <= 3) {
			return false
		}
	}
	return true
}

//	func throwerror() {
//		log.Fatal("something wrong")
//	}

func checkSafe(int_slice []int) bool {
	if int_slice[0] > int_slice[1] {
		isDescending := sort.SliceIsSorted(int_slice, func(i, j int) bool {
			return int_slice[i] >= int_slice[j]
		})
		if isDescending {
			return check_dif(int_slice)
		}
	} else {
		isAscending := sort.SliceIsSorted(int_slice, func(i, j int) bool {
			return int_slice[i] <= int_slice[j]
		})
		if isAscending {
			return check_dif(int_slice)
		}
	}
	return false
}
func creating_1d_arr(ch_arr []string) bool {
	temp_int_slice := []int{}
	len_int_slice := 0
	for index, str := range ch_arr {
		_ = index
		int_val, err := strconv.Atoi(str)
		temp_int_slice = append(temp_int_slice, int_val)
		check(err)
		len_int_slice++
	}
	if checkSafe(temp_int_slice) {
		return true
	}
	//removing element one at a time in throughout the slice to check for safe
	for i := 0; i < len_int_slice; i++ {
		independent_slice := make([]int, len(temp_int_slice))
		copy(independent_slice, temp_int_slice)
		int_slice := slices.Delete(independent_slice, i, i+1)
		fmt.Println(int_slice)
		if checkSafe(int_slice) {
			return true
		}
	}
	return false
}
func main() {
	// 	input := `7 6 4 2 1
	// 1 2 7 8 9
	// 9 7 6 2 1
	// 1 3 2 4 5
	// 8 6 4 4 1
	// 1 3 6 7 9`
	current_directory, err := os.Getwd()
	check(err)
	file_path := filepath.Join(current_directory, "Day2/input.txt")
	input, err := os.ReadFile(file_path)
	check(err)
	tempinput := string(input)
	new_input := strings.Split(tempinput, "\n")
	//counting safe rows in input
	total := 0
	for row, line := range new_input {
		_ = row
		ch_arr := strings.Split(line, " ")

		if creating_1d_arr(ch_arr) {
			total = total + 1
		} else {
		}

	}

	fmt.Println(total)

}
