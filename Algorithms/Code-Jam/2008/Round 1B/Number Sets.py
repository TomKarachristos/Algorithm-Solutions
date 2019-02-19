import sys
import math

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

q = int(input())

def prime_factors(n, P):
    num = set()

    #add 2 to list or prime factors and remove all even numbers(like sieve of ertosthenes)
    while(n%2 == 0):
        if 2 >= P:
            num.add(2)
        n /= 2

    #divide by odd numbers and remove all of their multiples increment by 2 if no perfectlly devides add it
    for i in range(3, int(math.sqrt(n))+1, 2):
        while (n%i == 0):
            if i >= P:
                num.add(i)
            n /= i

    #if no is > 2 i.e no is a prime number that is only divisible by itself add it
    if n>2:
        if( n >= P):
            num.add(n)

    return num

dis = {}
for _ in range(1, q+1):
    start, end, P_prime = map(int, input().split(' '))
    num_set = end-start+1
    ans = union_find(num_set)
    for i in range(start, end+1):
        for j in range(start, end+1):
            s_i = str(i) + str(P_prime)
            if s_i not in dis:
                dis[s_i] = prime_factors(i, P_prime)
            s_j = str(j) + str(P_prime)
            if s_j not in dis:
                dis[s_j] = prime_factors(j, P_prime)

            if len(dis[s_i]) != 0 and len(dis[s_j]) != 0:
                if dis[s_i] & dis[s_j]:
                    ans.union(i-start, j-start)

    with open('set_numbers.txt', 'a') as the_file:
        the_file.write('Case #{}: {}\n'.format(_, ans.count()))
