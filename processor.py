
# LAB 7: Fuzz Testing for Input Validation Bugs
# Fixed application

# Function 1: Convert comma-separated values into integers
def parse_int_list(value):
    if not isinstance(value, str):
        return []

    result = []

    for item in value.split(","):
        item = item.strip()

        if item == "":
            continue

        try:
            result.append(int(item))
        except ValueError:
            continue

    return result


# Function 2: Calculate average of a list
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0.0

    return sum(numbers) / len(numbers)


# Function 3: Validate age
def validate_age(age):
    return type(age) is int and 0 <= age <= 120


# Main program
if __name__ == "__main__":
    print("LAB 7: FUZZ TESTING")
    print("-------------------------")

    print("Function 1:", parse_int_list("10,20,30"))
    print("Function 2:", calculate_average([10, 20, 30]))
    print("Function 3:", validate_age(25))

    print("-------------------------")
    print("Fixed application executed successfully.")
