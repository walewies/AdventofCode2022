# --- Day 9: Rope Bridge ---

def testDiagonal(coordinate1, coordinate2):
    column_subtraction = coordinate1[0] - coordinate2[0]
    row_subtraction = coordinate1[1] - coordinate2[1]

    if abs(row_subtraction) == abs(column_subtraction) and abs(row_subtraction) == 1:
        return True
    else:
        return False

def testColumn(coordinate1, coordinate2):
    if coordinate1[0] == coordinate2[0]:
        return True
    else:
        return False

def testDirectColumn(coordinate1, coordinate2):
    column_subtraction = coordinate1[0] - coordinate2[0]

    if abs(column_subtraction) == 1 and coordinate1[1] == coordinate2[1]:
        return True
    else:
        return False

def testRow(coordinate1, coordinate2):
    if coordinate1[1] == coordinate2[1]:
        return True
    else:
        return False

def testDirectRow(coordinate1, coordinate2):
    row_subtraction = coordinate1[1] - coordinate2[1]

    if abs(row_subtraction) == 1 and coordinate1[0] == coordinate2[0]:
        return True
    else:
        return False

def testEqual(coordinate1, coordinate2):
    if coordinate1 == coordinate2:
        return True
    else:
        return False

def checkCloseEnough(coordinate1, coordinate2):
    if (testDirectColumn(coordinate1, coordinate2) or testDirectRow(coordinate1, coordinate2) or testEqual(coordinate1, coordinate2) or testDiagonal(coordinate1, coordinate2)):
        return True
    else:
        return False

def checkDistanceAndAct(coordinates1, coordinates2, new_steps):
    if not checkCloseEnough(coordinates1, coordinates2):
        if testRow(coordinates1, coordinates2):
            if coordinates1[0] - coordinates2[0] > 0:
                coordinates2[0] += 1
                new_steps.append(["R", 1])
            else:
                coordinates2[0] -= 1
                new_steps.append(["L", 1])

        elif testColumn(coordinates1, coordinates2):
            if coordinates1[1] - coordinates2[1] > 0:
                coordinates2[1] += 1
                new_steps.append(["U", 1])
            else:
                coordinates2[1] -= 1
                new_steps.append(["D", 1])

        elif (coordinates1[0] - coordinates2[0] == 2):
            if coordinates1[1] - coordinates2[1] == 1:
                coordinates2[0] += 1
                coordinates2[1] += 1
                new_steps.append(["R", 1])
                new_steps.append(["U", 1])
            elif coordinates1[1] - coordinates2[1] == -1:
                coordinates2[0] += 1
                coordinates2[1] -= 1
                new_steps.append(["R", 1])
                new_steps.append(["D", 1])

        elif (coordinates1[0] - coordinates2[0] == -2):
            if coordinates1[1] - coordinates2[1] == 1:
                coordinates2[0] -= 1
                coordinates2[1] += 1
                new_steps.append(["L", 1])
                new_steps.append(["U", 1])
            elif coordinates1[1] - coordinates2[1] == -1:
                coordinates2[0] -= 1
                coordinates2[1] -= 1
                new_steps.append(["L", 1])
                new_steps.append(["D", 1])

        elif (coordinates1[1] - coordinates2[1] == 2):
            if coordinates1[0] - coordinates2[0] == 1:
                coordinates2[0] += 1
                coordinates2[1] += 1
                new_steps.append(["R", 1])
                new_steps.append(["U", 1])
            elif coordinates1[0] - coordinates2[0] == -1:
                coordinates2[0] -= 1
                coordinates2[1] += 1
                new_steps.append(["L", 1])
                new_steps.append(["U", 1])

        elif (coordinates1[1] - coordinates2[1] == -2):
            if coordinates1[0] - coordinates2[0] == 1:
                coordinates2[0] += 1
                coordinates2[1] -= 1
                new_steps.append(["R", 1])
                new_steps.append(["D", 1])
            elif coordinates1[0] - coordinates2[0] == -1:
                coordinates2[0] -= 1
                coordinates2[1] -= 1
                new_steps.append(["L", 1])
                new_steps.append(["D", 1])

        else:
            print("failure")
            quit()

    # print(str(coordinates2) + "coord 2")
    # print(str(new_steps) + "New_steps")
    return [coordinates2, new_steps]
        
        # if not (coordinates2 in previous_coordinates):
        #     previous_coordinates.append([])
        #     previous_coordinates[-1].append(coordinates2[0])
        #     previous_coordinates[-1].append(coordinates2[1])

def main():
    data_file = open("Day9.txt", "r")
    data = data_file.read()

    raw_steps = data.split("\n")
    steps = []

    head_coordinates = [0, 0]
    tail_coordinates = [0, 0]

    previous_coordinates = [[0, 0]]

    for step in raw_steps:
        movement = step.split(" ")
        steps.append([movement[0], int(movement[1])])

    finished_movements = []

    for i in range(9):
        print(i)
        new_steps = []
        for step in steps:
            action = step[0]
            amount = step[1]

            for j in range(amount):
                # print(tail_coordinates)
                if action == "R":
                    head_coordinates[0] += 1
                elif action == "L":
                    head_coordinates[0] -= 1
                elif action == "U":
                    head_coordinates[1] += 1
                elif action == "D":
                    head_coordinates[1] -= 1

                results = checkDistanceAndAct(head_coordinates, tail_coordinates, new_steps)
                tail_coordinates = results[0]
                new_steps = results[1]

                if i == 8:
                    if not (tail_coordinates in previous_coordinates):
                        previous_coordinates.append([])
                        previous_coordinates[-1].append(tail_coordinates[0])
                        previous_coordinates[-1].append(tail_coordinates[1])
                        # print(previous_coordinates)
        finished_movements.append(head_coordinates)
        head_coordinates = [0, 0]
        tail_coordinates = [0, 0]
        steps = new_steps
        # print(steps)

    # print (finished_movements)  
    print(len(previous_coordinates))
    print("This Works")

if __name__ == "__main__":
    main()