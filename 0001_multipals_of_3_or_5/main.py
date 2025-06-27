# Sum of Multiples of 3 or 5 - Mathematical Solution
# This solves Project Euler Problem 1 efficiently using math instead of loops

TARGET = 1_000_000_000  # Find sum of multiples below this number


def sum_divisible_by(divisor):
    """
    Calculate sum of all multiples of 'divisor' below TARGET

    Example: sum_divisible_by(3) finds sum of: 3 + 6 + 9 + 12 + ... + largest_multiple_below_TARGET

    Mathematical approach:
    1. Multiples of n are: n, 2n, 3n, 4n, ..., pn (where pn < TARGET)
    2. Factor out n: n × (1 + 2 + 3 + 4 + ... + p)
    3. Use arithmetic series formula: 1 + 2 + ... + p = p × (p + 1) / 2
    4. Final result: n × p × (p + 1) / 2
    """

    # Step 1: Find how many multiples of 'divisor' are below TARGET
    # Example: if TARGET=1000 and divisor=3, then p = 999//3 = 333
    # This means there are 333 multiples of 3 below 1000: 3, 6, 9, ..., 999
    p = (TARGET - 1) // divisor

    # Step 2: Apply the formula
    # Sum = divisor × (1 + 2 + 3 + ... + p)
    # Sum = divisor × [p × (p + 1) / 2]
    return divisor * (p * (p + 1)) // 2


def solve_multiples_problem():
    """
    Find sum of all multiples of 3 or 5 below TARGET

    Uses inclusion-exclusion principle:
    - Sum(3 or 5) = Sum(3) + Sum(5) - Sum(both 3 and 5)
    - "Both 3 and 5" means multiples of LCM(3,5) = 15

    Why subtract Sum(15)?
    Numbers like 15, 30, 45... are divisible by both 3 and 5,
    so they get counted twice (once in Sum(3) and once in Sum(5)).
    We subtract them once to avoid double-counting.
    """

    sum_of_3_multiples = sum_divisible_by(3)
    sum_of_5_multiples = sum_divisible_by(5)
    sum_of_15_multiples = sum_divisible_by(15)  # 15 = LCM(3, 5)

    # Apply inclusion-exclusion principle
    result = sum_of_3_multiples + sum_of_5_multiples - sum_of_15_multiples

    print(f"TARGET: {TARGET:,}")
    print(f"Sum of multiples of 3:  {sum_of_3_multiples:,}")
    print(f"Sum of multiples of 5:  {sum_of_5_multiples:,}")
    print(f"Sum of multiples of 15: {sum_of_15_multiples:,}")
    print(
        f"Final answer: {sum_of_3_multiples:,} + {sum_of_5_multiples:,} - {sum_of_15_multiples:,} = {result:,}"
    )

    return result


# Your original concise solution (now with comments):
def original_solution():
    """Your elegant one-liner solution with explanation"""
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)


# Test with smaller numbers first to verify the logic
print("=== Testing with smaller numbers ===")
TARGET = 10
print(f"Multiples of 3 or 5 below {TARGET}: 3, 5, 6, 9")
print(f"Expected sum: 3 + 5 + 6 + 9 = 23")
print(f"Our formula gives: {original_solution()}")

print("\n" + "=" * 50)
TARGET = 1000
print(f"Testing with TARGET = {TARGET:,}")
result_1000 = solve_multiples_problem()

print("\n" + "=" * 50)
TARGET = 1_000_000_000
print(f"Final calculation with TARGET = {TARGET:,}")
final_result = solve_multiples_problem()

print(f"\n🎯 The sum of all multiples of 3 or 5 below {TARGET:,} is: {final_result:,}")
