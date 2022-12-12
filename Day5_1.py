# --- Day 5: Supply Stacks ---

def main():
    data_file = open("Day5.txt", "r")
    data = data_file.read()
    data_file.close()

    combined_data = data.split("\n")

    raw_stacks = combined_data[:8]
    stack_numbers = combined_data[8]
    raw_operations = combined_data[10:]
    
    stacks_columns = [[], [], [], [], [], [], [], [], []]
    irrelevant_chars = ["[", "]", " "]

    for stack in raw_stacks:
        for i in range(len(stack)):
            if stack[i] not in irrelevant_chars:
                stacks_columns[int(stack_numbers[i]) - 1].insert(0, stack[i])

    commands = []
    irrelevant_words = ["move", "from", "to"]
    for operation in raw_operations:
        commands.append([])
        raw_list = operation.split(" ")
        for item in raw_list:
            if item not in irrelevant_words:
                commands[-1].append(int(item))

    for command in commands:
        amount = command[0]
        from_column = command[1] - 1
        to_column = command[2] - 1

        for i in range(amount):
            top_item = stacks_columns[from_column].pop()
            stacks_columns[to_column].append(top_item)

    top_items = ""

    for column in stacks_columns:
        top_items += column[-1]

    print(top_items)

if __name__ == "__main__":
    main()