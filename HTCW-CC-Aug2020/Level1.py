print('Level 1 - Find the duplicates in a Python Tuple')


def countOnes(tupleToCount, searchItem):
    count = 0
    for t in tup:
        if t == searchItem:
            count += 1
    print(f'The number {searchItem} shows up {count} times in this tuple')


tup = (1, 1, 2, 3, 4, 1, 5, 6, 7, 1)

countOnes(tup, 1)
