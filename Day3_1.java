// --- Day 3: Rucksack Reorganization ---

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

class Day3_1 {
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
        int split_point;
        int total_sum = 0;
        for (int i = 0; i < backpacks.size(); i++) {
            split_point = backpacks.get(i).length() / 2;
            string1 = backpacks.get(i).substring(0, split_point);
            string2 = backpacks.get(i).substring(split_point);

            for (int j = 0; j < string1.length(); j++) {
                if (string2.contains(Character.toString(string1.charAt(j)))) {
                    total_sum += alphabets.indexOf(string1.charAt(j)) + 1;
                    break;
                }
            }
        }
        System.out.println(total_sum);
    }
}