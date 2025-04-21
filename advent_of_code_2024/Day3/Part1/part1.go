package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"
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
func main() {
	// input := `xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`
	// fmt.Println("something")
	current_directory, err := os.Getwd()
	check(err)
	file_path := filepath.Join(current_directory, "Day3/input.txt")
	input, err := os.ReadFile(file_path)
	check(err)
	new_input := string(input)

	len_new_input := len(new_input)
	fmt.Println(len_new_input)
	var term int
	total := 0
	count := 0
	for i := 0; i < len_new_input; i++ {
		if new_input[i] == 'm' {
			count = 1
			continue
		}

		if count == 1 && new_input[i] != 'u' {
			count = 0
			continue
		}

		if count == 2 && new_input[i] != 'l' {
			count = 0
			continue
		}

		if count == 3 && new_input[i] != '(' {
			count = 0
			continue
		}
		if count == 4 {
			count = 0
			i, term = loadNumeric(len_new_input, new_input, i)
			total = total + term
		}
		count++
	}
	fmt.Println(total)
}
