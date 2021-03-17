import random

maze = [[0 for i in range(10)] for j in range(10)]


def printmaze():
    for row in range(10):
        for col in range(10):
            print(maze[row][col], end="  ")
        print()


def makeRandomMaze():
    choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    flag = False
    for i in range(35):
        row = random.choice(choices)
        column = random.choice(choices)
        if(maze[row][column] == 1):
            flag = True
            while(flag):
                row = random.choice(choices)
                column = random.choice(choices)
                if(maze[row][column] != 1):
                    maze[row][column] = 1
                    flag = False
        else:
            maze[row][column] = 1


makeRandomMaze()
printmaze()
