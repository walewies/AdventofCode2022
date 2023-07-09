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

def main():
    data_file = open("Day9.txt", "r")
    data = data_file.read()

    raw_steps = data.split("\n")
    steps = []

    head_coordinates = [0, 0]
    tail_coordinates = [0, 0]

    for step in raw_steps:
        movement = step.split(" ")
        steps.append([movement[0], int(movement[1])])

    previous_coordinates = [[0, 0]]

    for step in steps:
        action = step[0]
        amount = step[1]
    
        for i in range(amount):
            if action == "R":
                head_coordinates[0] += 1
            elif action == "L":
                head_coordinates[0] -= 1
            elif action == "U":
                head_coordinates[1] += 1
            elif action == "D":
                head_coordinates[1] -= 1

            if not checkCloseEnough(head_coordinates, tail_coordinates):

                if testRow(head_coordinates, tail_coordinates):
                    if head_coordinates[0] - tail_coordinates[0] > 0:
                        tail_coordinates[0] += 1
                    else:
                        tail_coordinates[0] -= 1

                elif testColumn(head_coordinates, tail_coordinates):
                    if head_coordinates[1] - tail_coordinates[1] > 0:
                        tail_coordinates[1] += 1
                    else:
                        tail_coordinates[1] -= 1

                elif (head_coordinates[0] - tail_coordinates[0] == 2):
                    if head_coordinates[1] - tail_coordinates[1] == 1:
                        tail_coordinates[0] += 1
                        tail_coordinates[1] += 1
                    elif head_coordinates[1] - tail_coordinates[1] == -1:
                        tail_coordinates[0] += 1
                        tail_coordinates[1] -= 1

                elif (head_coordinates[0] - tail_coordinates[0] == -2):
                    if head_coordinates[1] - tail_coordinates[1] == 1:
                        tail_coordinates[0] -= 1
                        tail_coordinates[1] += 1
                    elif head_coordinates[1] - tail_coordinates[1] == -1:
                        tail_coordinates[0] -= 1
                        tail_coordinates[1] -= 1

                elif (head_coordinates[1] - tail_coordinates[1] == 2):
                    if head_coordinates[0] - tail_coordinates[0] == 1:
                        tail_coordinates[0] += 1
                        tail_coordinates[1] += 1
                    elif head_coordinates[0] - tail_coordinates[0] == -1:
                        tail_coordinates[0] -= 1
                        tail_coordinates[1] += 1

                elif (head_coordinates[1] - tail_coordinates[1] == -2):
                    if head_coordinates[0] - tail_coordinates[0] == 1:
                        tail_coordinates[0] += 1
                        tail_coordinates[1] -= 1
                    elif head_coordinates[0] - tail_coordinates[0] == -1:
                        tail_coordinates[0] -= 1
                        tail_coordinates[1] -= 1

                else:
                    quit()
                
                if not (tail_coordinates in previous_coordinates):
                    previous_coordinates.append([])
                    previous_coordinates[-1].append(tail_coordinates[0])
                    previous_coordinates[-1].append(tail_coordinates[1])

    print(len(previous_coordinates))

if __name__ == "__main__":
    main()