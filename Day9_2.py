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

def checkDistanceAndAct(coordinates1, coordinates2):
    if not checkCloseEnough(coordinates1, coordinates2):
        if testRow(coordinates1, coordinates2):
            if coordinates1[0] - coordinates2[0] > 0:
                coordinates2[0] += 1
            else:
                coordinates2[0] -= 1

        elif testColumn(coordinates1, coordinates2):
            if coordinates1[1] - coordinates2[1] > 0:
                coordinates2[1] += 1
            else:
                coordinates2[1] -= 1

        elif (coordinates1[0] - coordinates2[0] == 2):
            if coordinates1[1] - coordinates2[1] == 1 or coordinates1[1] - coordinates2[1] == 2:
                coordinates2[0] += 1
                coordinates2[1] += 1
            elif coordinates1[1] - coordinates2[1] == -1 or coordinates1[1] - coordinates2[1] == -2:
                coordinates2[0] += 1
                coordinates2[1] -= 1

        elif (coordinates1[0] - coordinates2[0] == -2):
            if coordinates1[1] - coordinates2[1] == 1 or coordinates1[1] - coordinates2[1] == 2:
                coordinates2[0] -= 1
                coordinates2[1] += 1
            elif coordinates1[1] - coordinates2[1] == -1 or coordinates1[1] - coordinates2[1] == -2:
                coordinates2[0] -= 1
                coordinates2[1] -= 1

        elif (coordinates1[1] - coordinates2[1] == 2):
            if coordinates1[0] - coordinates2[0] == 1 or coordinates1[0] - coordinates2[0] == 2:
                coordinates2[0] += 1
                coordinates2[1] += 1
            elif coordinates1[0] - coordinates2[0] == -1 or coordinates1[0] - coordinates2[0] == -2:
                coordinates2[0] -= 1
                coordinates2[1] += 1

        elif (coordinates1[1] - coordinates2[1] == -2):
            if coordinates1[0] - coordinates2[0] == 1 or coordinates1[0] - coordinates2[0] == 2:
                coordinates2[0] += 1
                coordinates2[1] -= 1
            elif coordinates1[0] - coordinates2[0] == -1 or coordinates1[0] - coordinates2[0] == -2:
                coordinates2[0] -= 1
                coordinates2[1] -= 1
                
        else:
            print("Failure")
            quit()

    return coordinates2


def main():
    data_file = open("Day9.txt", "r")
    data = data_file.read()

    raw_steps = data.split("\n")
    steps = []

    previous_coordinates = [[0, 0]]

    for step in raw_steps:
        movement = step.split(" ")
        steps.append([movement[0], int(movement[1])])

    previous_steps = []

    positions_of_knots = []
    amount_of_knots = 10
    for i in range(amount_of_knots):
        positions_of_knots.append([0, 0])

    for step in steps:      
            action = step[0]
            amount = step[1]

            for j in range(amount):
                if action == "R":
                    positions_of_knots[0][0] += 1
                elif action == "L":
                    positions_of_knots[0][0] -= 1
                elif action == "U":
                    positions_of_knots[0][1] += 1
                elif action == "D":
                    positions_of_knots[0][1] -= 1

                
                for i in range(len(positions_of_knots) - 1):

                    positions_of_knots[i + 1] = checkDistanceAndAct(positions_of_knots[i], positions_of_knots[i + 1])
                    
                    if i == amount_of_knots - 2:
                        if not (positions_of_knots[i + 1] in previous_coordinates):
                            previous_coordinates.append([])
                            previous_coordinates[-1].append(positions_of_knots[i + 1][0])
                            previous_coordinates[-1].append(positions_of_knots[i + 1][1])
                      
    print(len(previous_coordinates))

if __name__ == "__main__":
    main()