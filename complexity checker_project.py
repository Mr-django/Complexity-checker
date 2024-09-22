import time
import random
import sys

def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Function to measure time and space complexity
def measure_complexity(func, input_sizes):
    for n in input_sizes:
        numbers = [random.randint(0, 100) for _ in range(n)]
        input_size_bytes = sys.getsizeof(numbers)
        input_size_kb = input_size_bytes / 1024
        print(f"Input size: {n}, Memory usage (input): {input_size_kb} KB")

        start_time = time.time()
        mem_before = sys.getsizeof(numbers) + sys.getsizeof(0)  # Approximate initial memory
        result = func(numbers)
        end_time = time.time()
        mem_after = sys.getsizeof(numbers) + sys.getsizeof(result)  # Approximate final memory
        mem_usage_kb = (mem_after - mem_before) / 1024
        print(f"Input size: {n}, Time: {end_time - start_time} seconds")
        print(f"Memory usage during execution: {mem_usage_kb} KB")
        print()

# Example usage
input_sizes = [10, 100, 1000, 10000]
measure_complexity(sum_list, input_sizes)