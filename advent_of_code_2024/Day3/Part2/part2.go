package main

import (
	"fmt"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}
func loadNumeric(len_new_input int, new_input string, i int) (int, int) {
	var valid1 []byte
	var valid2 []byte
	var term int
	for i < len_new_input && new_input[i] != ',' {
		if new_input[i] < '0' || new_input[i] > '9' {
			return i, 0
		}
		valid1 = append(valid1, new_input[i])
		i++
	}
	i++
	for i < len_new_input && new_input[i] != ')' {
		if new_input[i] < '0' || new_input[i] > '9' {
			return i, 0
		}
		valid2 = append(valid2, new_input[i])
		i++

	}
	if len(valid2) == 0 {
		return i, 0
	}
	term1, err := strconv.Atoi(string(valid1))
	check(err)
	term2, err := strconv.Atoi(string(valid2))
	check(err)
	term = term1 * term2
	return i, term
}
func indexes(input string, substr string) []int {
	var index_arr []int
	start := 0

	for {
		index := strings.Index(input[start:], substr)
		if index == -1 {
			break
		}
		real_index := start + index
		index_arr = append(index_arr, real_index)
		start = start + index + len(substr)
	}
	return index_arr
}
func dont_indexes(input string) []int {
	substr := "don't()"
	return indexes(input, substr)
}
func do_indexes(input string) []int {
	substr := "do()"
	return indexes(input, substr)
}
func find_diff(indexes []int, target int) int {
	fmt.Println("good")
	for i, v := range indexes {
		_ = v
		if indexes[i] < target && (i+1 >= len(indexes) || indexes[i+1] > target) {
			fmt.Println("ok5")
			fmt.Println(i)
			fmt.Println(indexes[i])
			fmt.Println(target)
			fmt.Println(target - indexes[i])
			return target - indexes[i]
		}

	}
	fmt.Println("ok1")

	return target - indexes[len(indexes)-2]
}
func do_appliable(do_indexes []int, dont_indexes []int, target_index int) bool {
	if do_indexes[0] > target_index && dont_indexes[0] > target_index {

		return true
	}

	dont_dif := find_diff(dont_indexes, target_index)
	do_dif := find_diff(do_indexes, target_index)
	if dont_dif > do_dif {
		return true
	} else {
		return false
	}

}
func main() {
	input := `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`
	// current_directory, err := os.Getwd()
	// check(err)
	// file_path := filepath.Join(current_directory, "Day3/input.txt")
	// input, err := os.ReadFile(file_path)
	// check(err)
	new_input := string(input)

	//check for indexes of don't()
	dont_indexes := dont_indexes(new_input)
	fmt.Println(dont_indexes)
	//check for indexes of do()
	do_indexes := do_indexes(new_input)
	fmt.Println(do_indexes)

	len_new_input := len(new_input)
	var term int
	total := 0
	mul_ch_count := 0

	for i := 0; i < len_new_input; i++ {
		if new_input[i] == 'm' {
			mul_ch_count = 1
			continue
		}

		if mul_ch_count == 1 && new_input[i] != 'u' {
			mul_ch_count = 0
			continue
		}

		if mul_ch_count == 2 && new_input[i] != 'l' {
			mul_ch_count = 0
			continue
		}

		if mul_ch_count == 3 && new_input[i] != '(' {
			mul_ch_count = 0
			continue
		}
		if mul_ch_count == 4 {
			println(do_appliable(do_indexes, dont_indexes, i-4))
		}
		if mul_ch_count == 4 {
			mul_ch_count = 0
			i, term = loadNumeric(len_new_input, new_input, i)
			total = total + term
		}
		mul_ch_count++
	}
	fmt.Println(total)
}
