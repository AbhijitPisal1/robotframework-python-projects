def check_divisibility_in_range(num, start, end):
    """
    Check if a number is divisible by each integer from start to end (inclusive).
    """
    divisible_list =[]
    if start > end:
        print("Invalid range: start must be less than or equal to end.")
        return []

    print(f"Divisibility check for {num} from {start} to {end}:")

    for divisor in range(start, end + 1):
        if divisor == 0:
            print("Cannot divide by 0")
            continue
        if num % divisor == 0:
            print(f"Divisible by {divisor}")
            divisible_list.append(divisor)
        else:
            print(f"Not divisible by {divisor}")
    print(divisible_list)

# test case
check_divisibility_in_range(54, 2, 10)
