def sum_numbers(*args):
    sum = 0
    for value in args:
        sum += value
    return sum


def difference_numbers(*args):
    difference = 0
    for value in args:
        difference -= value
    return difference


def product_numbers(*args):
    product = 1
    for value in args:
        product *= value
    return product


def quotient_numbers(*args):
    quotient = 1
    for value in args:
        quotient /= value
    return quotient


print(sum_numbers(1,2,3,4,5))
print(difference_numbers(1,2,3,4,5))
print(product_numbers(1,2,3))
print(quotient_numbers(1,2,3,4,5))

