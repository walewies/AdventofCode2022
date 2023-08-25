// --- Day 10: Cathode-Ray Tube ---
#include <iostream>
#include <fstream>
#include <vector>

std::vector<std::string> split(std::string input_string, char split_substring) {
    std::string temp_string = "";
    std::vector<std::string> return_vector = {};
    for (int i = 0; i < input_string.size(); i++) {
        if (input_string[i] == split_substring) {
            return_vector.push_back(temp_string);
            temp_string = "";
        } else {
            temp_string += input_string[i];
        }
    }
    return_vector.push_back(temp_string);
    return return_vector;
}

bool contains(std::string input_string, char to_find) {
    for (int i = 0; i < input_string.size(); i++) {
        if (input_string[i] == to_find) {
            return true;
        }
    }
    return false;
}

int getIndexFromString(std::string input_string, char to_find) {
    for (int i = 0; i < input_string.size(); i++) {
        if (input_string[i] == to_find) {
            return i;
        }
    }
    return -1;
}

int main() {
    std::fstream data_file;
    data_file.open("Day10.txt");

    std::vector<std::string> tasks = {};
    std::string file_line;
    while (getline(data_file, file_line)) {
        tasks.push_back(file_line);
    }

    std::vector<int> signal_strengths = {};
    
    int test_cycle = 20;
    int cycle_step = 40;

    int register_X = 1;

    bool cycle_skip = false;
    int addx_value = 0;

    int task_index = 0;

    int index_of_space;
    int length_of_int;

    for (int cycle_value = 1; cycle_value <= 220; cycle_value++) {

        if (cycle_value == test_cycle) {
            signal_strengths.push_back(cycle_value * register_X);
            test_cycle += cycle_step;
        } 

        // checks for addx
        if (contains(tasks[task_index], ' ')) {
            if (addx_value == 0) {
                // finds and changes the addx value
                index_of_space = getIndexFromString(tasks[task_index], ' ');
                length_of_int = tasks[task_index].size() - index_of_space;
                addx_value = std::stoi(tasks[task_index].substr(index_of_space, length_of_int));
            } else {
                register_X += addx_value;
                addx_value = 0;
                task_index += 1;
            }
        } else { // noop
            task_index += 1;
        }
    }

    int final_sum = 0;
    for (int i = 0; i < signal_strengths.size(); i++) {
        final_sum += signal_strengths[i]; 
    }
    
    std::cout << final_sum << "\n";
}