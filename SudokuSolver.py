print('''
 _____           _       _            _____       _                
/  ___|         | |     | |          /  ___|     | |               
\ `--. _   _  __| | ___ | | ___   _  \ `--.  ___ | |_   _____ _ __ 
 `--. \ | | |/ _` |/ _ \| |/ / | | |  `--. \/ _ \| \ \ / / _ \ '__|
/\__/ / |_| | (_| | (_) |   <| |_| | /\__/ / (_) | |\ V /  __/ |   
\____/ \__,_|\__,_|\___/|_|\_\\__,_| \____/ \___/|_| \_/ \___|_|   
                                                                    
By: Mr LDGCA                                                                  
''')

# This program uses an exhaustive search method to solve the sudoku puzzle.
#   Every blank space is taken and the corresponding row, column and 3x3 cell is
#   is analysed to identify potential values. If only 1 value fits the space, it
#   is written to the space.
#   This process is repeated until no blank spaces remain.

'''
# Puzzle 01 : Easy
puzzle = [[2, 6, "-", "-", "-", "-", "-", "-", "-", ],
          ["-", 7, "-", "-", "-", 4, "-", 1, "-", ],
          [3, 5, "-", 6, 9, 1, 8, 7, "-", ],
          ["-", "-", 8, 2, "-", "-", "-", "-", "-", ],
          ["-", "-", 2, 5, 4, 6, 3, "-", "-", ],
          ["-", "-", "-", "-", "-", 9, 4, "-", "-", ],
          ["-", 2, 7, 9, 5, 3, "-", 4, 8, ],
          ["-", 4, "-", 7, "-", "-", "-", 9, "-", ],
          ["-", "-", "-", "-", "-", "-", "-", 5, 3]]

# Puzzle 02 : Hard
'''
puzzle = [["-", "-", "-", 8, 2, "-", "-", "-",9],
          [4, 8, "-", 1, "-", "-", 2, "-", "-"],
          ["-", 9, "-", 6, "-", "-", "-", "-", "-"],
          ["-", 4, "-", "-", "-", "-", "-", "-", 5],
          [3, "-", 1, 2, "-", 5, 8, "-", 4],
          [5, "-", "-", "-", "-", "-", "-", 6, "-"],
          ["-", "-", "-", "-", "-", 2, "-", 1, "-"],
          ["-", "-", 4, "-", "-", 1, "-", 5, 6],
          [6, "-", "-", "-", 7, 8, "-", "-", "-"]]

'''
# Puzzle 03 : Hard
puzzle = [["-", "-", 5, 4, "-", 9, "-", "-", 1],
          ["-", "-", "-", "-", 7, "-", "-", 3, 6],
          ["-", 1, "-", "-", "-", "-", 4, "-", "-"],
          ["-", 5, 4, "-", "-", "-", "-", "-", "-", ],
          ["-", 3, "-", 6, 2, 8, "-", 5, "-"],
          ["-", "-", "-", "-", "-", "-", 3, 1, "-"],
          ["-", "-", 8, "-", "-", "-", "-", 2, "-"],
          [9, 7, "-", "-", 4, "-", "-", "-", "-", ],
          [3, "-", "-", 8, "-", 7, 6, "-", "-"]]
'''


def validatePuzzle():
    global spacesRemain
    for i, row in enumerate(puzzle):
        if len(row) != 9:
            print("Puzzle row #" + str(i+1) + " is invalid !!!")
            spacesRemain = False
            return False
    if len(puzzle) != 9:
        print("Puzzle is invalid !!!")
        spacesRemain = False
        return False

    return True


def drawGrid():
    for row in range(9):
        if row % 3 == 0:
            print(" |---------|---------|---------|")
        for cell in range(3):
            print(" | " + str(puzzle[row][cell * 3 + 0]) + "  " + str(puzzle[row][cell * 3 + 1]) + "  " +
                  str(puzzle[row][cell * 3 + 2]), end="")
        print("")

    print(" |---------|---------|---------|")


def columnElements(index):
    elements = []
    for i in puzzle:
        elements.append(i[index])

    return elements


def cellElements(row, element):
    elements = []
    cellIndex = [row // 3, element // 3]
    for i in range(3):
        for j in range(3):
            n = puzzle[cellIndex[0] * 3 + i][cellIndex[1] * 3 + j]
            if n != "-":
                elements.append(n)
    return elements


# ======== main =========
if validatePuzzle():
    drawGrid()
    counter = 1
    spacesRemain = True
    previousAnswers = []

    input("Start solving ?")

    while spacesRemain:
        print("========= Round " + str(counter) + "=========")
        validValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        answers = []
        for row in range(9):
            for element in range(9):
                if puzzle[row][element] != "-":
                    answers.append("")
                else:
                    potentialAnswers = []
                    for i in validValues:
                        if i not in puzzle[row]:
                            if i not in columnElements(element):
                                if i not in cellElements(row, element):
                                    potentialAnswers.append(i)
                    answers.append(potentialAnswers)

        # for a given row, identify the potential answers that only appear once, then use that answer at the
        # corresponding index.
        for row in range(9):
            values = [item for sublist in answers[row * 9:row * 9 + 9] for item in sublist]
            uniqueValues = [i for i in values if values.count(i) == 1]
            if len(uniqueValues) == 1:
                print("Row : " + str(row) + "\t", end="")
                print(uniqueValues)
                for i, answer in enumerate(answers[row * 9:row * 9 + 9]):
                    for element in answer:
                        if element == uniqueValues[0]:
                            answers[row * 9 + i] = uniqueValues
                            break

        # for a given column, identify potential answers that occur only once, and substitute that value to
        # the corresponding index.
        for column in range(9):
            values = []
            for row in range(9):
                values.append(answers[row * 9 + column])
            values = [item for sublist in values for item in sublist]
            uniqueValues = [i for i in values if values.count(i) == 1]
            if len(uniqueValues) == 1:
                print("Column : " + str(column) + "\t", end="")
                print(uniqueValues)
                for row in range(9):
                    for element in answers[row * 9 + column]:
                        if uniqueValues[0] == element:
                            answers[row * 9 + column] = uniqueValues
                            break

        for i in range(81):
            if len(answers[i]) == 1:
                puzzle[i // 9][i % 9] = answers[i][0]

        drawGrid()
        counter += 1

        puzzleElements = [item for sublist in puzzle for item in sublist]
        puzzleElementSet = set(puzzleElements)

        if "-" not in puzzleElementSet:
            spacesRemain = False

        # Safety measure to prevent an infinite loop
        if answers == previousAnswers:
            print("Failed to solve")
            spacesRemain = False
        else:
            previousAnswers = answers

    print("Did I get it?")

else:
    print("Fix the puzzle and try again")