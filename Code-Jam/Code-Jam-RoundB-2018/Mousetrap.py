from operator import itemgetter

q = int(input())
for _ in range(1, q+1):
    k = int(input())
    cards = list(map(int, input().split(' ')))[1:]
    ans = k * [-1]
    find = [i for i in range(k)]
    count = 1
    position = 0
    while count <= k:
        position = (position + count - 1) % len(find)
        found_pos = find[position]
        del find[position]
        ans[found_pos] = count
        count += 1

    result = len(cards) * [-1]
    for index,value in enumerate(cards):
        result[index] = ans[value-1]


    with open('Mousetrap.txt', 'a') as the_file:
        the_file.write('Case #{}: {}\n'.format(_,  ('{} '*len(cards)).format(*result)))
