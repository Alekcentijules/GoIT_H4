"""Module for calculating total and average salary from a file."""

from pathlib import Path

def total_salary(path):
    """
    Calculates the total and average salary from a text file.

    Args:
        path (str): Path to the data file (format: Name,salary).

    Returns:
        Union[Tuple[int, float], str]:
            - (total, average) — if the file is processed successfully.
            - str — error message (file not found, empty, incorrect format).

    Examples:
        >>> total_salary("data/salaries.txt")
        (6000, 2000.0)
        >>> total_salary("nonexistent.txt")
        'File nonexistent.txt not found!'
    """
    try:
        salaries = []
        with open(Path(path), "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                name, salary = line.split(",", 1)
                salaries.append(int(salary))
        if not salaries:
            return f"File {path} is empty or contains no valid data!"
        
        total = sum(salaries)
        average = total / len(salaries)
        return (total, average)
    
    except FileNotFoundError:
        return f"File {path} not found!"
    except ValueError:
        return "File format is incorrect!\nExpected: Name, Salary."
    except Exception as err:
        return f"An unexpected error occurred: {err}"

filename = input("Enter a path to file: ")
result = total_salary(filename)

if isinstance(result, tuple):
    total, average = result
    print(f"Total salary: {total}\nAverage salary: {average}")
else:
    print(result)