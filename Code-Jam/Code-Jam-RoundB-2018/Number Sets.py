import sys


class union_find:
    """
    An implementation of union find data structure.
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
            p = id[p] = id[id[p]]  # Path compression using halving.
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

q = int(sys.stdin.readline().rstrip())

# This function returns a list containing all the factors of a ginven parameters n
def getFactors(n):
    # Create an empty list for factors
    factors=set();

    # Loop over all factors
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            factors.add(i)

    # Return the list of factors
    return factors



for i in range(q):
    start, end, prime = map(int, sys.stdin.readline().rstrip().split(' '))
    num_set = end-start
    for i in range(start,end):
        for j in range(start,end):
            if( i != j ):
                for k in range(prime):
                    if(getFactors(i).intersection(getFactors((j)))):






