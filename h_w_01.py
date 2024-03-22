from pathlib import Path


"""return tuple of salaries sumary and average salary per person."""
def total_salary(path) -> tuple:

    # check if path/file exists if not return the message. 
    path = Path(path)
    if not path.exists():
        return 'file does not exists or the path is wrong.'
    
    # parse the salaries and count total salary and average salary
    try:
        salaries = get_salaries(path)
    except (ValueError):
        return print("\nError: File structure is not supported.\n")
    total_salary = 0
    for salary in salaries:
        total_salary += salary
    average_salary = total_salary // len(salaries)

    return (total_salary, average_salary)


"""return integer list with salaries."""
def get_salaries(path) -> list:
    salaries = []
    with open (path, 'r', encoding='UTF-8') as salary_file:
        for line in salary_file.readlines():

            # clear the last tab when no elements left
            line = line.strip()

            # take only salary from file. Than turn salary into int type and add it to the list 
            if line != '':
                _, salary = line.split(',')
                salaries.append(int(salary))

    return salaries


print(total_salary("example.txt"))