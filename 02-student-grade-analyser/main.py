
def add_student(dictionary_):

    try:
        num = int(input("How many students are there? "))
        if num <= 0:
            print("Please enter a number greater than 0")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    while num > len(dictionary_):
        try:
            x = input("Enter the students name: ")
            if x in dictionary_:
                print("That student already exists, please enter a different name.")
                continue
            y = input(f"Enter the {x}'s grades: ")

            dictionary_[x] = int(y)

        except ValueError:
            print("Please enter a valid number.")
            continue

    
    if not check_dict(dictionary_):
        print("No students were registered.")
        return


    print("These are the students and their grades:", dictionary_)


def maximum(dictionary_: dict[str, int]):
    if not check_dict(dictionary_):
        print("No students were registered.")
        return

    max_name, max_num = next(iter(dictionary_.items()))
    for name, value in dictionary_.items():
        if value > max_num:
            max_num = value
            max_name = name
    return max_name


def minimum(dictionary_: dict[str, int]):
    if not check_dict(dictionary_):
        print("No students were registered.")
        return


    min_name, min_num = next(iter(dictionary_.items()))
    for name, value in dictionary_.items():
        if value < min_num:
            min_num = value
            min_name = name
    return min_name


def average(dictionary_: dict[str, int]):

    total = 0
    for num in dictionary_.values():
        total += num
    return total/len(dictionary_)


def search_stu(stu, dictionary_):
    if not check_dict(dictionary_):
        print("No students were registered.")
        return

    if stu in dictionary_:
        stu_score = dictionary_[stu]
        return stu_score
    else:
        return

def check_dict(dictionary_: dict[str, int]) -> bool:
    if len(dictionary_) == 0:
        return False
    return True

# MAIN FUNCTION

def main():    
    stu_n_grades = dict()
    while True:
        print("=====STUDENT GRADE ANALYSER=====\n1. Add student\n2. View students\n3. Find max scorer\n4. Find min scorer\n5. Find class average\n6.Search for student\n7.Exit")

        try:
            choice = int(input("Please enter the number corresponding to your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            add_student(stu_n_grades)
        elif choice == 2:
            if not check_dict(stu_n_grades):
                print("There are no students added.")
                continue
            for key, value in stu_n_grades.items():
                print(f"{key} scored {value} marks.")
                print()
        elif choice == 3:
            print(f"The maximum scorer is: {maximum(stu_n_grades)}")
        elif choice == 4:
            print(f"The minimum scorer is: {minimum(stu_n_grades)}")
        elif choice == 5:
            if not check_dict(stu_n_grades):
                print("There are no students added.")
                continue
            print(f"The class average is {average(stu_n_grades)}")
        elif choice == 6:
            stu = input("Enter student's name: ")
            stu_score = search_stu(stu, stu_n_grades)
            if stu_score is not None:
                print(f"{stu} scored {stu_score}")
            else:
                print("Student not found.")
                continue
        elif choice == 7:
            break
        else:
            print("Invalid option")
            continue
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")