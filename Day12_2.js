// --- Day 12: Hill Climbing Algorithm ---
let fs = require('fs');
const { EOL } = require("os"); // End Of Line for system compatibiliy

// Alphabet indeces signify hights
const alphabet = 'SabcdefghijklmnopqrstuvwxyzE';
const alphabet_array = alphabet.split('');

function checkSurroundingAndModify(main_point, grid, coordinates_and_distances) {
    let main_y = main_point[0];
    let main_x = main_point[1];
    let main_letter_index = alphabet_array.indexOf(grid[main_y][main_x]);
    let max_letter_index = main_letter_index + 1;
    let altered_index;
    let value_of_main_point = coordinates_and_distances[main_y + "," + (main_x)];
    let value_of_altered_point;
    let new_main_points = [];
    let altered_point;
    
    // If statements to ensure that you keep to the grid

    // Check Left
    if (main_x - 1 >= 0) {
        altered_point = [main_y, main_x - 1];
        altered_index = alphabet_array.indexOf(grid[main_y][main_x - 1]);
        if (altered_index <= main_letter_index || altered_index == max_letter_index) {
            value_of_altered_point = coordinates_and_distances[main_y + "," + (main_x - 1)];
            if (value_of_altered_point > value_of_main_point + 1 || value_of_altered_point == null) {
                value_of_altered_point = value_of_main_point + 1;
                coordinates_and_distances[main_y + "," + (main_x - 1)] = value_of_altered_point;
                new_main_points.push(altered_point);
            }
        }
    }

    // Check Right
    if (main_x + 1 < grid[0].length) {
        altered_point = [main_y, main_x + 1];
        altered_index = alphabet_array.indexOf(grid[main_y][main_x + 1]);        
        if (altered_index <= main_letter_index || altered_index == max_letter_index) {
            value_of_altered_point = coordinates_and_distances[main_y + "," + (main_x + 1)];
            if (value_of_altered_point > value_of_main_point + 1 || value_of_altered_point == null) {
                value_of_altered_point = value_of_main_point + 1;
                coordinates_and_distances[main_y + "," + (main_x + 1)] = value_of_altered_point;
                new_main_points.push(altered_point);
            }
        }
    }

    // Check Top
    if (main_y - 1 >= 0) {
        altered_point = [main_y - 1, main_x];
        altered_index = alphabet_array.indexOf(grid[main_y - 1][main_x]);
        if (altered_index <= main_letter_index || altered_index == max_letter_index) {
            value_of_altered_point = coordinates_and_distances[(main_y - 1) + "," + main_x];
            if (value_of_altered_point > value_of_main_point + 1 || value_of_altered_point == null) {
                value_of_altered_point = value_of_main_point + 1;
                coordinates_and_distances[(main_y - 1) + "," + main_x] = value_of_altered_point;
                new_main_points.push(altered_point);
            }
        }
    }

    // Check Bottom
    if (main_y + 1 < grid.length) {
        altered_point = [main_y + 1, main_x];
        altered_index = alphabet_array.indexOf(grid[main_y + 1][main_x]);
        if (altered_index <= main_letter_index || altered_index == max_letter_index) {
            value_of_altered_point = coordinates_and_distances[(main_y + 1) + "," + main_x];
            if (value_of_altered_point > value_of_main_point + 1 || value_of_altered_point == null) {
                value_of_altered_point = value_of_main_point + 1;
                coordinates_and_distances[(main_y + 1) + "," + main_x] = value_of_altered_point;
                new_main_points.push(altered_point);
            }
        }
    }

    return [coordinates_and_distances, new_main_points];
}

function main() {
    let input = fs.readFileSync("Day12.txt", "utf8");

    let rows = input.split(EOL);
    let grid = [];
    let starting_positions = [];
    let E_position = [];
    let coordinates_and_distances = {};

    for (let i = 0; i < rows.length; i++) {
        grid.push([]);
        for (let j = 0; j < rows[0].length; j++) {
            grid[grid.length - 1].push(rows[i][j]);
            coordinates_and_distances[[i, j]] = null;
            if (rows[i][j] == "S" || rows[i][j] == "a") {
                starting_positions.push([i, j]);
            } else if (rows[i][j] == "E") {
                E_position = [i, j];
            }
        }
    }

    let reset_coordiantes_and_distances = {...coordinates_and_distances};
    let end_lengths = [];
    let start_position;
    let main_points;

    for (let i = 0; i < starting_positions.length; i++) {

        coordinates_and_distances = {...reset_coordiantes_and_distances};
        start_position = starting_positions[i];
        coordinates_and_distances[start_position[0] + "," + start_position[1]] = 0;
        main_points = [start_position];

        while (main_points.length > 0) {
            results = checkSurroundingAndModify(main_points[0], grid, coordinates_and_distances);
            coordinates_and_distances = results[0];

            // removes first element in main_points when finished with it 
            main_points.shift()

            // Adds new main points
            for (let j = 0; j < results[1].length; j++) {
                main_points.push(results[1][j])
            }
        }

        end_lengths.push(coordinates_and_distances[E_position[0] + "," + E_position[1]]);
    }
    
    let min_distance = null;
    for (let i = 0; i < end_lengths.length; i++) {
        
        if (min_distance !== null && end_lengths[i] !== null) {
            if (end_lengths[i] < min_distance) {
                min_distance = end_lengths[i];
            }
        } else {
            if (end_lengths[i] !== null) {
                min_distance = end_lengths[i];
            }
        }
    }

    console.log(min_distance);
}

main()