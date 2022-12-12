// --- Day 6: Tuning Trouble ---
#include <iostream>
#include <fstream>
#include <string>

bool contains(std::string input_string, char to_find) {
    for (int i = 0; i < input_string.size(); i++) {
        if (input_string[i] == to_find) {
            return true;
        }
    }
    return false;
}

int main() {
    std::fstream data_file;
    data_file.open("Day6.txt");

    std::string data;
    getline(data_file, data);

    int marker_size = 4;
    int marker_index;
    std::string test_string = "";
    int index_of_duplicate;

    for (int i = 0; i < data.size(); i++) {

        if (!contains(test_string, data[i])) {
            test_string += data[i];
        } else {
            index_of_duplicate = test_string.find(data[i]);
            test_string = test_string.substr(index_of_duplicate + 1, test_string.size());
            test_string += data[i];
        }

        if (test_string.size() == marker_size) {
                marker_index = i + 1;
                break;
        }
    }

    std::cout << marker_index << "\n";
    return 0;
}