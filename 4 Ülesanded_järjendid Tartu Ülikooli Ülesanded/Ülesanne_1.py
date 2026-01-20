from random import randint

def generate_number_list(smallest: int, largest: int) -> list[int]:
    result = []
    for i in range(10):
        random_number = randint(smallest, largest)
        result.append(random_number)
    return result

def ask_user_int(question: str) -> int:
    user_input = input(question)
    while not user_input.isdigit():
        print("Input not a integer. Please try again.")
        user_input = input(question)
    return int(user_input)

def multiply_list(numbers: list[int], multiplier: int) -> list[int]:
    result = []
    for number in numbers:
        result.append(number * multiplier)
    return result

def show_result(original_numbers: list[int], multiplier: int, resulting_numbers: list[int]):
    for i in range (len(original_numbers)):
        print(f"{original_numbers[i]} * {multiplier} = {resulting_numbers[i]}")

if __name__ == '__main__':
    numbers_list = generate_number_list(1, 10)
    multiplier = ask_user_int("Please insert multiplier: ")
    multiplyed_list = multiply_list(numbers_list, multiplier)
    show_result(numbers_list, multiplier, multiplyed_list)