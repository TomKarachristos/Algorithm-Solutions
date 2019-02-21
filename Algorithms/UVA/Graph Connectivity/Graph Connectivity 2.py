import sys

def get_number(char):
    return ord(char) - 65

"""
MakeSet(x) initializes disjoint set for object x
Find(x) returns representative object of the set containing x
Union(x,y) makes two sets containing x and y respectively into one set

Some Applications:
- Kruskal's algorithm for finding minimal spanning trees
- Finding connected components in graphs
- Finding connected components in images (binary)
"""

class union_find:
    """An implementation of union find data structure.
    It uses weighted quick union by rank with path compression.
    """

    def __init__(self, N):
        """Initialize an empty union find object with N items.

        Args:
            N: Number of items in the union find object.
        """

        self._id = list(range(N))
        self._count = N
        self._rank = [0] * N

    def find(self, p):
        """Find the set identifier for the item p."""

        id = self._id
        while p != id[p]:
            p = id[p] = id[id[p]]   # Path compression using halving.
        return p

    def count(self):
        """Return the number of items."""
        return self._count

    def connected(self, p, q):
        """Check if the items p and q are on the same set or not."""
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """Combine sets containing p and q into a single set."""
        id = self._id
        rank = self._rank

        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        self._count -= 1
        if rank[i] < rank[j]:
            id[i] = j
        elif rank[i] > rank[j]:
            id[j] = i
        else:
            id[j] = i
            rank[i] += 1

    def __str__(self):
        """String representation of the union find object."""
        return " ".join([str(x) for x in self._id])

    def __repr__(self):
        """Representation of the union find object."""
        return "UF(" + str(self) + ")"

cases = int(sys.stdin.readline().rstrip())
blank_line =  sys.stdin.readline()
for index in range(cases):
    line =  sys.stdin.readline().rstrip()
    n = get_number(line)
    sets = union_find(n+1)
    line = sys.stdin.readline().rstrip()
    while line != '':
        sets.union( get_number(line[0]), get_number(line[1]) )
        line = sys.stdin.readline().rstrip()
    
    print(sets.count())
    if(index != cases-1):
        print()