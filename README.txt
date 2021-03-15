This is a python implementation of a sudoku game that this played from the command line. This program required the term color package in order to run.

RUNNING THIS PROGRAM ON FLIP:
Navigate to the directory containing sudoku_game.py
Enter: virtualenv projectname (project name can be whatever you want)
Enter:  source projectname/bin/activate
Enter: pip install termcolor
Enter: python sudoku_game.py

WHAT IS SUDOKU:
In classic sudoku, the objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution. (citation: Wikipedia "Sudoku" https://en.wikipedia.org/wiki/Sudoku)


USING THIS PROGRAM:
There are five modes in this program: Easy, Medium, Hard,Brute Force, and Verify.

Upon start-up the program will asked the user to select a mode by typing one of the modes listed above.

Easy: Solve one easy level sudoku puzzle
Medium: Solve one medium level sudoku puzzle
Hard: Solve one hard level sudoku puzzle
Brute Force: the program generates brute force solution to a sudoku puzzle
Verify: Verify the correctness of any completed sudoku puzzle.

The command line will print: "Easy, Medium, Hard, Brute Force, or Verify?" to the console.
An input listed above wrapped in quotations marks must be passed into the program for it to run.

INSTRUCTIONS FOR PLAYING IN EASY, MEDIUM OR HARD MODE:
The program will prompt you for your moves until you win or quit the game. You make move pass a row, column, and value. If you make a mistake and want to remove a value from a cell pass the row number, column number, and "0" into the game and the value will be removed.

Sudoku Grid with numbered cells (xx = [row][column]):
[00,01,02,03,04,05,06,07,08]
[10,11,12,13,14,15,16,17,18]
[20,21,22,23,24,25,26,27,28]
[30,31,32,33,34,35,36,37,38]
[40,41,42,43,44,45,46,47,48]
[50,51,52,53,54,55,56,57,58]
[60,61,62,63,64,65,66,67,68]
[70,71,72,73,74,75,76,77,78]
[80,81,82,83,84,85,86,87,88]


INSTRUCTIONS FOR BRUTE FORCE MODE:
The program will solve one sudoku board and print that solved board to the console.

INSTRUCTIONS FOR VERIFY MODE
This program can verify the correctness of any completed sudoku board. When Verify mode is selected the program will prompt you to provide a sudoku puzzle as a string with a space between every value. Make sure the string is wrapped with quotations. 

Example:
To test the Verify mode enter a completed puzzle in this format:
7 4 3 8 1 9 2 5 6 5 8 1 7 6 2 3 4 9 2 9 6 3 5 4 8 7 1 9 1 7 2 4 5 6 8 3 6 5 8 9 3 1 4 2 7 4 3 2 6 7 8 9 1 5 8 6 5 4 9 7 1 3 2 3 7 4 1 2 6 5 9 8 1 2 9 5 8 3 7 6 4	


EXAMPLE SOLUTIONS for Easy, Medium, Hard, and Verify Mode:

Example Easy Mode Solution:
easy_test=[
[6,8,5,9,1,3,4,2,7],
[4,2,3,6,8,7,9,1,5],
[9,7,1,2,5,4,6,8,3],
[1,9,2,5,3,8,7,6,4],
[3,4,7,1,6,2,5,9,8],
[8,5,6,4,7,9,1,3,2],
[2,6,9,3,4,5,8,7,1],
[5,1,8,7,2,6,3,4,9],
[7,3,4,8,9,1,2,5,6]
]

Example Medium Mode Solution:
medium_test = [
[7,4,3,8,1,9,2,5,6],
[5,8,1,7,6,2,3,4,9],
[2,9,6,3,5,4,8,7,1],
[9,1,7,2,4,5,6,8,3],
[6,5,8,9,3,1,4,2,7],
[4,3,2,6,7,8,9,1,5],
[8,6,5,4,9,7,1,3,2],
[3,7,4,1,2,6,5,9,8],
[1,2,9,5,8,3,7,6,4]
]

Example Hard Mode Solution:
hard_test = [
[2,9,6,7,8,1,4,3,5],
[5,8,1,4,3,9,2,7,6],
[7,4,3,5,2,6,9,8,1],
[9,1,7,8,6,3,5,2,4],
[4,3,2,1,9,5,8,6,7],
[6,5,8,2,4,7,1,9,3],
[8,6,5,3,1,2,7,4,9],
[3,7,4,9,5,8,6,1,2],
[1,2,9,6,7,4,3,5,8]
]

Example test for Verify Mode:
7 4 3 8 1 9 2 5 6 5 8 1 7 6 2 3 4 9 2 9 6 3 5 4 8 7 1 9 1 7 2 4 5 6 8 3 6 5 8 9 3 1 4 2 7 4 3 2 6 7 8 9 1 5 8 6 5 4 9 7 1 3 2 3 7 4 1 2 6 5 9 8 1 2 9 5 8 3 7 6 4	