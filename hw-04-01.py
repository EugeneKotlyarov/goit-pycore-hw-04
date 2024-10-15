import pathlib


# total_salary function accepts relative path to salary text file
# and return tuple with total salary and avarage salary
# or
# error in string if something goes wrong
def total_salary(filename: str) -> tuple:

    # find path to our .py scrypt file
    current_dir = pathlib.Path(__file__).parent

    try:
        # trying to open file in current directory and read all the lines without "\n" signatures
        with open(current_dir / filename, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

            # variables for: dict of tuples of all our workers, resulting total and average salary
            workers = []
            salary_total = 0
            salary_avrg = 0

            # next 3 parts is function itself: create dictionary, calcuate results
            for l in lines:
                workers.append(tuple(l.split(",")))

            for w in range(len(workers)):
                salary_total += int(workers[w][1])

            salary_avrg = float(salary_total / len(workers))

    # exceptions in cases: file not found or any other
    except FileNotFoundError:
        return "Не вдалося знайти файл з зарплатнею."

    except Exception as e:
        return str(e) + " error in total_salary()"

    return (salary_total, salary_avrg)


# test
def main():
    result = total_salary("hw-04-01-salary.txt")

    if type(result) == str:
        print(result)
    else:
        total, average = result[0], result[1]
        print(
            f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
        )


if __name__ == "__main__":
    main()
