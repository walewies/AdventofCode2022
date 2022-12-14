// --- Day 7: No Space Left On Device ---
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

class Day7_2 {
    public static void main(String[] args) {    
        ArrayList<String> command_log = new ArrayList<String>();
        try {
            File data_file = new File("Day7.txt");
            Scanner file_reader = new Scanner(data_file);
            while (file_reader.hasNextLine()) {
                command_log.add(file_reader.nextLine());
            }
        } catch (FileNotFoundException error) {
            error.printStackTrace();
        }

        String command;
        ArrayList<Integer> working_directories = new ArrayList<Integer>();
        ArrayList<Integer> counted_directories = new ArrayList<Integer>();
        int last_element_id;
        int last_element;
        int new_last_element_id;
        int new_last_element;
        int to_add;
        
        for (int i = 0; i < command_log.size(); i++) {
            
            command = command_log.get(i);

            if (command.substring(2, 4).equals("ls")) {
                // pass
            } else if (command.substring(2, 4).equals("cd")) {
                if (command.substring(5).equals("..")) {
                    last_element_id = working_directories.size() - 1;
                    last_element = working_directories.get(last_element_id);
                    counted_directories.add(last_element);
                    working_directories.remove(last_element_id);

                    new_last_element_id = working_directories.size() - 1;
                    new_last_element = working_directories.get(new_last_element_id);
                    working_directories.set(new_last_element_id, new_last_element + last_element);
                } else {
                    working_directories.add(0);
                }
            } else if (command.substring(0, 3).equals("dir")) {
                // pass
            } else {
                last_element_id = working_directories.size() - 1;
                last_element = working_directories.get(last_element_id);
                to_add = Integer.parseInt(command.split(" ")[0]);
                working_directories.set(last_element_id, last_element + to_add);
            }
        }

        for (int i = working_directories.size() - 1; i >= 0; i--) {
            if (working_directories.size() == 1) {
                last_element_id = working_directories.size() - 1;
                last_element = working_directories.get(last_element_id);
                counted_directories.add(last_element);
                working_directories.remove(last_element_id);
            } else {
                last_element_id = working_directories.size() - 1;
                last_element = working_directories.get(last_element_id);
                counted_directories.add(last_element);
                working_directories.remove(last_element_id);

                new_last_element_id = working_directories.size() - 1;
                new_last_element = working_directories.get(new_last_element_id);
                working_directories.set(new_last_element_id, new_last_element + last_element);
            }
        }

        int total_size = 70000000;
        int required_size = 30000000;
        int available_size = total_size - counted_directories.get(counted_directories.size() - 1);
        int smallest_deletable_directory = counted_directories.get(counted_directories.size() - 1);
        for (int i = 0; i < counted_directories.size(); i++) {
            if (available_size + counted_directories.get(i) > required_size && counted_directories.get(i) < smallest_deletable_directory) {
                smallest_deletable_directory = counted_directories.get(i);
            }
        }
        System.out.println(smallest_deletable_directory);
    }
}