// --- Day 4: Camp Cleanup ---
const fs = require('fs');

function main() {
    let input_data = fs.readFileSync("Day4.txt", "utf8");
    let pairs = input_data.split("\n");
    let shifts_per_pair;
    let temp_array = [];
    let shifts = [];
    let overlapping_shifts = 0;

    for (let i = 0; i < pairs.length; i++) {
        shifts_per_pair = pairs[i].split(",");
        for (let j = 0; j < 2; j++) {
            shift_range_per_elf = shifts_per_pair[j].split("-");
            temp_array.push(shift_range_per_elf);
        }
        shifts.push(temp_array);
        temp_array = [];
    }
    
    let elf1_max;
    let elf1_min;
    let elf2_max;
    let elf2_min;
    for (let i = 0; i < shifts.length; i++) {
        elf1_max = parseInt(shifts[i][0][1]);
        elf1_min = parseInt(shifts[i][0][0]);
        elf2_max = parseInt(shifts[i][1][1]);
        elf2_min = parseInt(shifts[i][1][0]);
        if ((elf1_min >= elf2_min && elf1_min <= elf2_max) || (elf1_max >= elf2_min && elf1_max <= elf2_max)
            || (elf2_min >= elf1_min && elf2_min <= elf1_max) || (elf2_max >= elf1_min && elf2_max <= elf1_max)) {
            overlapping_shifts++;
        }
    }

    console.log(overlapping_shifts);
}

main();