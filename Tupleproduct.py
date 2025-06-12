def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
user_input = input("enter numbers")
try:
    number_tuple = tuple(int(num.strip()) for num in user_input.split(","))
    user_product = int(input("Enter the product you expect: "))
    actual_product = calculate_product(number_tuple)
    if actual_product == user_product:
        print("Correct! The product matches.")
    else:
        print(f"Incorrect. The actual product is {actual_product}.")
except ValueError:
    print("Please enter only valid integers.")