# --- Day 1: Calorie Counting ---

def main():
    input_file = open("Day1.txt", "r")
    data = input_file.read()
    input_file.close()
    elves_raw = data.split("\n\n")
    elves = []
    for elf in elves_raw:
        elves.append(elf.split("\n"))
    
    max_calories = 0
    elf_index = None

    max1 = 0
    max2 = 0
    max3 = 0

    for elf in elves:
        calories = 0
        for item in elf:
            calories += int(item)
        if calories > max3:
            if calories > max2:
                if calories > max1:
                    max3 = max2
                    max2 = max1
                    max1 = calories
                else:
                    max3 = max2
                    max2 = calories
            else:
                max3 = calories

    print(max1 + max2 + max3)
    

if __name__ == "__main__":
    main()