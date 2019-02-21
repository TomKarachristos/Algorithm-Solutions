import sys

def get_next(line,next):
    while(next in line):
        next = next+1
        if(next == 53):
            return -1
    return next

for line in sys.stdin:
    line = list(map(int,line.rstrip().split(' ')))
    if(line[0] == 0):
        break
    x,y = line[:3],line[3:]
    x.sort(reverse=True)
    y.sort(reverse=True)
    if(y[1] > x[0]):
        print(get_next(line, 1))
    elif(y[1] > x[1]):
        next = get_next(line, x[1]+1)
        if(next == -1):
            print("-1")
            continue
        else:
            print( next )
    elif(y[1] < x[1] and y[0] > x[0]): 
        next = get_next(line, x[0]+1)
        if(next == -1):
            print("-1")
            continue
        else:
            print( next )
    else:
        print("-1")