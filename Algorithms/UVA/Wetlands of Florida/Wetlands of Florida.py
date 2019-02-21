import sys

def conditions_to_append(theStack,x,y):
    if( x < 0 or x >= len(surface) or y < 0 or y >= len(surface[x])):
        return
    else:
        theStack.append((x,y)  )

def floodfill(surface, x, y, oldColor):
    # assume surface is a 2D image and surface[x][y] is the color at x, y.
    visited = set((x,y)) 
    theStack = [ (x, y) ]
    counter = 0
    while len(theStack) > 0:
        x, y = theStack.pop()
    
        if surface[x][y] != oldColor or (x , y) in visited:
            continue
        visited.add((x,y))

        counter += 1
        conditions_to_append(theStack, x + 1, y )  # right
        conditions_to_append(theStack, x - 1, y )  # left
        conditions_to_append(theStack, x, y + 1 )  # down
        conditions_to_append(theStack, x, y - 1 )  # up
        conditions_to_append(theStack, x + 1, y + 1 )
        conditions_to_append(theStack, x - 1, y - 1 )
        conditions_to_append(theStack, x + 1, y - 1 )
        conditions_to_append(theStack, x - 1, y + 1 )
        
    return counter

cases = int(sys.stdin.readline())
blank_line = sys.stdin.readline()
for index in range(cases):
    line = sys.stdin.readline().rstrip()
    surface = []
    while not line[0].isdigit():
        surface.append( list(line) )
        line = sys.stdin.readline().rstrip()
    
    while line != '':
        a,b = line.split()
        print(floodfill(surface, int(a)-1, int(b)-1, 'W'))
        try:
            line = input()
        except EOFError:
            break
    if(index != cases-1):
        print()
