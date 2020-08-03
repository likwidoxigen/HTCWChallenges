print('Level 2 - Find the max and min of a Python Set')


def findBounds(settoSearch):
    sort_list = sorted(this_set)
    if len(this_set) < 1:
        return {'smallest': None, 'largest': None}
    else:
        return {'smallest': sort_list[0], 'largest': sort_list[-1]}


this_set = set([15, 11, 8, 15, 32, 20])
bounds = findBounds(this_set)

print(
    f'The smallest value is {bounds["smallest"]} and largest value is {bounds["largest"]}')
