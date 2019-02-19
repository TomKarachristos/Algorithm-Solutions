import sys

q = int(input())

for i in range(1, q + 1):
    n = int(input())
    vectors = list()
    vectors.append(list(map(int, input().split(' '))))
    vectors.append(list(map(int, input().split(' '))))

    vectors[0].sort()
    vectors[1].sort(reverse=True)

    ans = 0
    for z in range(n):
        ans = ans + (vectors[0][z] * vectors[1][z])

    with open('Minimum_Scalar_Product.txt', 'a') as the_file:
        the_file.write('Case #{}: {}\n'.format(i, ans))



