// --- Day 11: Monkey in the Middle ---
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

class Day11_1 {

    static ArrayList<String> convertArrayToArrayList(String[] to_convert) {
        ArrayList<String> return_array = new ArrayList<String>();

        for (int i = 0; i < to_convert.length; i++) {
            return_array.add(to_convert[i]);
        }

        return return_array;
    }

    public static void main(String[] args) {
        String raw_input = "";
        try {
            File input_file = new File("Day11.txt");
            Scanner file_reader = new Scanner(input_file);
            while (file_reader.hasNextLine()) {
                raw_input += file_reader.nextLine();
            }
        } catch (FileNotFoundException error) {
            error.printStackTrace();
        }

        ArrayList<String> raw_monkeys = new ArrayList<String>();

        String[] raw_monkeys_array = raw_input.split("Monkey ");

        for (int i = 1; i < raw_monkeys_array.length; i++) { // i = 1, because first string is empty 
            raw_monkeys.add(raw_monkeys_array[i]);
        }

        ArrayList<ArrayList<String>> monkeys = new ArrayList<ArrayList<String>>();
        
        for (int i = 0; i < raw_monkeys.size(); i++) {
            // Changes data to a more manageble format.
            raw_monkeys.set(i, raw_monkeys.get(i).replace(":  Starting items: ", "#"));
            raw_monkeys.set(i, raw_monkeys.get(i).replace("  Operation: new = old ", "#"));
            raw_monkeys.set(i, raw_monkeys.get(i).replace("  Test: divisible by ", "#"));
            raw_monkeys.set(i, raw_monkeys.get(i).replace("    If true: throw to monkey ", "#"));
            raw_monkeys.set(i, raw_monkeys.get(i).replace("    If false: throw to monkey ", "#"));
            
            monkeys.add(convertArrayToArrayList(raw_monkeys.get(i).split("#")));           
        }

        ArrayList<Integer> monkey_inspections = new ArrayList<Integer>();
        for (int i = 0; i < monkeys.size(); i++) {
            monkey_inspections.add(0);
        }

        ArrayList<String> current_monkey_items;
        int working_item;
        int index_of_true_monkey;
        String true_monkey_items;
        int index_of_false_monkey;
        String false_monkey_items;

        int num_of_round = 20;

        for (int i = 0; i < num_of_round; i++) {
            for (int j = 0; j < monkeys.size(); j++) {
        
                // Clause for when monkey has no items
                if (!monkeys.get(j).get(1).equals("")) {
                    current_monkey_items = convertArrayToArrayList(monkeys.get(j).get(1).split(", "));

                    // Loops through each item a monkey has
                    for (int k = 0; k < current_monkey_items.size(); k++) {

                        working_item = Integer.parseInt(current_monkey_items.get(k));

                        // Performs operation on current working item
                        if (monkeys.get(j).get(2).contains("* old")) {
                            working_item *= working_item;   
                        } else if (monkeys.get(j).get(2).contains("+ ")) {
                            working_item += Integer.parseInt(monkeys.get(j).get(2).replace("+ ", ""));
                        } else if (monkeys.get(j).get(2).contains("* ")) {
                            working_item *= Integer.parseInt(monkeys.get(j).get(2).replace("* ", ""));
                        }

                        // Divides current working item stress level by 3
                        working_item = (int)(working_item / 3);

                        // If condition is true pass item to true monkey
                        if (working_item % Integer.parseInt(monkeys.get(j).get(3)) == 0) {                        
                            index_of_true_monkey = Integer.parseInt(monkeys.get(j).get(4));
                            true_monkey_items = monkeys.get(index_of_true_monkey).get(1);
                            if (true_monkey_items.equals("")) {
                                monkeys.get(index_of_true_monkey).set(1, true_monkey_items += Integer.toString(working_item));
                            } else {
                                monkeys.get(index_of_true_monkey).set(1, true_monkey_items += ", " + Integer.toString(working_item));
                            }
                        } else { // If condition is false pass item to false monkey
                            index_of_false_monkey = Integer.parseInt(monkeys.get(j).get(5));
                            false_monkey_items = monkeys.get(index_of_false_monkey).get(1);
                            if (false_monkey_items.equals("")) {
                                monkeys.get(index_of_false_monkey).set(1, false_monkey_items += Integer.toString(working_item));
                            } else {
                                monkeys.get(index_of_false_monkey).set(1, false_monkey_items += ", " + Integer.toString(working_item));
                            }
                        }

                        // When item is finished, increase count of monkey inspections
                        monkey_inspections.set(j, monkey_inspections.get(j) + 1);
                    }

                    // Empties monkey's hands
                    monkeys.get(j).set(1, "");
                }
            }
        }

        // Finds the two highest in monkey inspections
        int max_1 = 0;
        int max_2 = 0;
        for (int i = 0; i < monkey_inspections.size(); i++) {
            if (monkey_inspections.get(i) > max_2) {
                if (monkey_inspections.get(i) > max_1) {
                    max_2 = max_1;
                    max_1 = monkey_inspections.get(i);
                } else {
                    max_2 = monkey_inspections.get(i);
                }
            }
        }
        System.out.println(max_1 * max_2);
    }
}