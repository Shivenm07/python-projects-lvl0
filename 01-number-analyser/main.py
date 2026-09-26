def maximum_number(list_of_numbers: list[int]) -> int:
    max_num = list_of_numbers[0]
    for num in list_of_numbers:
        if num > max_num:
            max_num = num
    return max_num

def minimum_number(list_of_numbers: list[int]) -> int:
    min_num = list_of_numbers[0]
    for num in list_of_numbers:
        if num < min_num:
            min_num = num
    return min_num


def main():
    numbers: list = []
    even_numbers: list = []
    odd_numbers: list = []
    numbers_above_average: list = []

    try:
        num_of_numbers = int(input("How many numbers do you want to input?: "))
        if num_of_numbers <= 1:
            print("Please enter a number greater than 1")
            return
    except:
        print("Please enter a valid number")
        return

    total = 0
    counter = 1

    while num_of_numbers > len(numbers):
        try:
            x = int(input(f"What is number {counter}: "))
        except:
            print("Please enter a valid number.")
            continue
        numbers.append(x)
        total += x

        if x % 2 == 0:
            even_numbers.append(x)
        else:
            odd_numbers.append(x)
        counter += 1

    average = total/num_of_numbers

    for num in numbers:
        if num > average:
            numbers_above_average.append(num)


    print(f"Maximum number is: {maximum_number(numbers)}")
    print(f"Minimum number is: {minimum_number(numbers)}")
    print("The average is", average)
    print("The odd numbers are:", odd_numbers)
    print("The even numbers are:", even_numbers)
    print("The numbers above average are", numbers_above_average)




if __name__ == "__main__":
    main()