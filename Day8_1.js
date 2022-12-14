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

function isVisible(row_array, column_array, row, column) {
    let left_visible = true;
    let right_visible = true;
    let top_visible = true;
    let bottom_visible = true;
    
    for (let i = 0; i < column; i++) {
        if (row_array[i] >= row_array[column]) {
            left_visible = false;
            break;
        } 
    }

    for (let i = column + 1; i < row_array.length; i++) {
        if (row_array[i] >= row_array[column]) {
            right_visible = false;
            break;
        } 
    }

    for (let i = 0; i < row; i++) {
        if ((column_array[i] >= column_array[row])) {
            top_visible = false;
            break;
        }
    }

    for (let i = row + 1; i < column_array.length; i++) {
        if ((column_array[i] >= column_array[row])) {
            bottom_visible = false;
            break;
        }
    }
    
    if (left_visible || right_visible || top_visible || bottom_visible) {
        return true;
    } else {
        return false;
    }
}

function main() {
    let data = fs.readFileSync("Day8.txt", "utf8");

    let tree_rows = data.split("\n");
    let row_length = tree_rows[0].length;
    let column_length = tree_rows.length;
    let visible_trees = 2 * row_length + 2 * column_length - 4;

    for (let i = 1; i < column_length - 1; i++) {
        for (let j = 1; j < row_length - 1; j++) {
            if (isVisible(getRow(i, tree_rows), getColumn(j, tree_rows), i, j)) {
                visible_trees++;
            }
        }
    }

    console.log(visible_trees);
}

main()