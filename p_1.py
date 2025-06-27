# Multiples of 3 or 5
# Problem 1
# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6, and 9. The sum
# of these multiples is 23. Find the sum of all the
# multiples of 3 or 5 below 1000.


def sum_multiples(m1, m2, length):
    sum = 0
    for multiple in range(length):
        if multiple % m1 == 0 or multiple % m2 == 0:
            sum += multiple
    return sum


print(sum_multiples(3, 5, 1000))
