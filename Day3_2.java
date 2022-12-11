// --- Day 3: Rucksack Reorganization ---

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

class Day3_2 {
    public static void main(String[] args) {
        ArrayList<String> backpacks = new ArrayList<String>();
        try {
            File dataFile = new File("Day3.txt");
            Scanner fileReader = new Scanner(dataFile);

            while (fileReader.hasNextLine()) {
                backpacks.add(fileReader.nextLine());
            }
            fileReader.close();
        } catch (FileNotFoundException error) {
            error.printStackTrace();
        }  

        ArrayList<Character> alphabets = new ArrayList<Character>();

        for (int i = 97; i < 123; i++) {
            alphabets.add((char) i);
        }

        for (int i = 65; i < 91; i++) {
            alphabets.add((char) i);
        }

        String string1;
        String string2;
        String string3;
        int loop_range;
        int total_sum = 0;
        ArrayList<Character> possible_badges = new ArrayList<Character>();
        String loop_string;
        String compare_string;
        for (int i = 0; i < backpacks.size() - 2; i += 3) {
            string1 = backpacks.get(i);
            string2 = backpacks.get(i + 1);
            string3 = backpacks.get(i + 2);

            if (string1.length() > string2.length()) {
                loop_range = string2.length();
                loop_string = string2;
                compare_string = string1;
            } else {
                loop_range = string1.length();
                loop_string = string1;
                compare_string = string2;
            }

            for (int j = 0; j < loop_range; j++) {
                if (compare_string.contains(Character.toString(loop_string.charAt(j)))) {
                    possible_badges.add(loop_string.charAt(j));
                }
            }

            for (int k = 0; k < possible_badges.size(); k++) {
                if (string3.contains(Character.toString(possible_badges.get(k)))) {
                    total_sum += alphabets.indexOf(possible_badges.get(k)) + 1;
                    break;
                }
            }
            possible_badges.clear();
        }
        System.out.println(total_sum);
    }
}