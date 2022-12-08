// --- Day 2: Rock Paper Scissors ---

#include <iostream>
#include <fstream>
#include <string>
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

int getIndex(std::vector<std::string> base, std::string to_find) {
    for (int i = 0; i < base.size(); i++) {
        if (base[i] == to_find) {
            return i;
        }
    }
    return -1;
}

std::vector<std::string> opponent_plays = {"A", "B", "C"}; // {Rock, Paper, Scissors}
std::vector<std::string> my_plays = {"X", "Y", "Z"}; // {Lose, Draw, Win}

int main() {
    std::fstream data_file;
    data_file.open("Day2.txt");

    std::vector<std::vector<std::string>> strategy = {};

    std::string file_line;
    while (getline(data_file, file_line)) {
        strategy.push_back(split(file_line, ' '));

    }

    int score = 0;

    for (int i = 0; i < strategy.size(); i++) {
        std::string opponent_play = strategy[i][0];
        std::string my_play = strategy[i][1];
        
        score += getIndex(my_plays, my_play) * 3;

        if (my_play == "Y") { // draw
            score += getIndex(opponent_plays, opponent_play) + 1;
        } else if (my_play == "Z") { // Win
            int add_to_score = getIndex(opponent_plays, opponent_play) + 1;
            if (add_to_score > 2) { // Checks if index greater than list size.
                add_to_score -= 3;
            }
            score += add_to_score + 1;
        } else if (my_play == "X") { // Lose
            int add_to_score = getIndex(opponent_plays, opponent_play) + 2;
            if (add_to_score > 2) { // Checks if index greater than list size.
                add_to_score -= 3;
            }
            score += add_to_score + 1;
        }
    }

    std::cout << score << "\n";

    return 0;
}