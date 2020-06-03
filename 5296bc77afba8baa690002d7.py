def row(puzzle,N): ##return list of all digits in the row N
    return puzzle[N]

def column(puzzle,N): #return list of all digits in the column N
    return [x[N] for x in puzzle]

# quads:
# [0 1 2
#  3 4 5
#  6 7 8]

def quart(puzzle,N): #return list of all digits in the subgrid N ("quart")
    minY=(N//3)*3
    maxY=minY+3
    minX=(N%3)*3
    maxX=minX+3
    return [ x[minX:maxX] for x in puzzle[minY:maxY] ]

def find_quart(coords): # identify quart based on coordinates tuple (y,x)
    return int(coords[0]/3)*3+int(coords[1]/3)

def options(puzzle,coordinates): # find all available options for current field
    r = set(row(puzzle,coordinates[0]))
    c = set(column(puzzle,coordinates[1]))
    q = set ([ item for innerlist in quart(puzzle,find_quart(coordinates)) for item in innerlist ])
    return r | c | q

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    while 0 in [ item for innerlist in puzzle for item in innerlist ]:
        for y in range(9):
            for x in range(9):
                if puzzle[y][x]>0:
                    continue
                opts=options(puzzle,(y,x) )
                r = set(range(1,10)) - opts
                if (len(r) == 1):
                    for val in r:
                        puzzle[y][x]=val
                        break
    return puzzle
