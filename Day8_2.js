// --- Day 8: Treetop Tree House ---
let fs = require('fs');

function getRow(row, grid) {
    let row_array = [];
    let row_string = grid[row]
    let row_length = row_string.length;
    
    for (let i = 0; i < row_length; i++) {
        row_array.push(parseInt(row_string[i]));
    }

    return row_array;
}

function getColumn(column, grid) {
    let column_array = [];
    let column_length = grid.length;

    for (let i = 0; i < column_length; i++) {
        column_array.push(parseInt(grid[i].charAt(column)));
    }

    return column_array;
}

function getScenicScore(row_array, column_array, row, column) {
    let left_score = 0;
    let right_score = 0;
    let top_score = 0;
    let bottom_score = 0;
    
    for (let i = column - 1; i >= 0; i--) {
        left_score++;
        if (row_array[i] >= row_array[column]) {
            break;
        }
    }

    for (let i = column + 1; i < row_array.length; i++) {
        right_score++;
        if (row_array[i] >= row_array[column]) {
            break;
        } 
    }

    for (let i = row - 1; i >= 0; i--) {
        top_score++;
        if ((column_array[i] >= column_array[row])) {
            break;
        }
    }

    for (let i = row + 1; i < column_array.length; i++) {
        bottom_score++;
        if ((column_array[i] >= column_array[row])) {
            break;
        }
    }
    
    return left_score * right_score * top_score * bottom_score;
}

function main() {
    let data = fs.readFileSync("Day8.txt", "utf8");

    let tree_rows = data.split("\n");
    let row_length = tree_rows[0].length;
    let column_length = tree_rows.length;
    let highest_scenic_score = 0;
    let current_scenic_score;

    for (let i = 1; i < column_length - 1; i++) {
        for (let j = 1; j < row_length - 1; j++) {
            current_scenic_score = getScenicScore(getRow(i, tree_rows), getColumn(j, tree_rows), i, j)
            if (current_scenic_score > highest_scenic_score) {
                highest_scenic_score = current_scenic_score;
            }
        }
    }

    console.log(highest_scenic_score);
}

main()