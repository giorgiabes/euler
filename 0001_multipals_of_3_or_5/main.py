# Multiples of 3 or 5
# Problem 1
# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6, and 9. The sum
# of these multiples is 23. Find the sum of all the
# multiples of 3 or 5 below 1000.


# solution 1
def sum_multiples(n):
    sum = 0
    for multiple in range(n):
        if multiple % 3 == 0 or multiple % 5 == 0:
            sum += multiple
    return sum
