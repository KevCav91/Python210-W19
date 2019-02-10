feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

comp = [delicacy for delicacy in feast if len(delicacy) > 6]

print(len(feast))

print(len(comp))

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

comprehension = [ number * skit for number, skit in list_of_tuples ]

print(comprehension)

print(comprehension[0])

print(len(comprehension[2]))

dict_of_weapons = {'first': 'fear',
                   'second': 'surprise',
                   'third':'ruthless efficiency',
                   'forth':'fanatical devotion',
                   'fifth': None}

dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

print('first' in dict_comprehension)

print('FIRST' in dict_comprehension)

print(len(dict_of_weapons))
print(len(dict_comprehension))


def count_evens(nums):
    even_nums = [num for num in nums if num % 2 == 0]
    return len(even_nums)


print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([1, 3, 5]))



