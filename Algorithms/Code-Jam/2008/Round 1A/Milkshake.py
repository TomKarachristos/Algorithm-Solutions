import sys

def serve_customers(ans, customers):
    for index in range(len(customers)):
        has_connect = False
        malted_position = -1
        customer = customers[index]
        for two_step in range(1, customer[0]*2, 2):
            position = customer[two_step]-1 # indexing start from 0
            if (ans[position] == customer[two_step + 1]):
                has_connect = True
                break
            else:
                if (ans[position] == 0 and customer[two_step + 1] == 1):
                    malted_position = position

        if (not has_connect):
            if (malted_position != -1):
                ans[malted_position] = 1
                # Now that we melt lets solve the problem again
                return serve_customers(ans, customers)
            else:
                return False
    return True

q = int(input())

for index in range(1, q + 1):
    n = int(input())
    m = int(input())
    customers = [None] * m
    ans = [0] * n
    for j in range(m):
        # customers[0] the number of pairs
        customers[j] = list(map(int, input().split(' ')))

    if(serve_customers(ans, customers)):
        with open('milkshake.txt', 'a') as the_file:
            the_file.write(f'Case #{index}: ' + ('{} '*len(ans)).format(*ans) + '\n')
    else:
        with open('milkshake.txt', 'a') as the_file:
            the_file.write(f'Case #{index}: IMPOSSIBLE\n')

