# SudokuSolver

By: MrLDGCA

## Introduction
This CLI program will solve any given sudoku puzzle.
The solver uses a rule based approach to find the solution. No trial-and-error algorithms are being used.
 
Several puzzles are included in the sourcecode for testing and reference.

## Algorithm

Rules:

- for all the empty cell:
  - create a list of values [0-9]
  - identify values present in the row and remove them from the list
  - identify values present in the column and remove them from the list
  - identify values present in the corresponding 3x3 cell and remove them from the list
  - if only 1 value remains in the list, assign it to the cell
 
  - [ 
 	The above rules could only solve "Easy" puzzles.
     	The following check is needed for "Medium" and "Hard" puzzles.
 
 	- for every cell in a row:
 		- take the lists of potential solutions
 		- identify values that only occure once (i.e. the value has only 1 suitable position)
 		- replace the list of multiple values with the list with just the single suitable value
    ]
 - loop again until all the cells are filled
