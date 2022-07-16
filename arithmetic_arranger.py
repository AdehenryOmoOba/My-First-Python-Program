import re

test_one = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
test_two = ["192 - 21", "4212 - 0", "41 + 843", "13 + 911"]


def arithmetic_arranger(problems, evaluate=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    first = ''
    second = ''
    lines = ''
    sumx = ''
    string = ''

    for problem in problems:
        if re.search('[/]', problem) or re.search('[*]', problem):
            return "Error: Operator must be '+' or '-'"
        if (re.search("[^\s0-9.+-]", problem)):
            return "Error: Numbers must only contain digits"

        first_number = problem.split(' ')[0]
        second_number = problem.split(' ')[2]
        operator = problem.split(' ')[1]

        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more that 4 digits"

        sum = ''

        if operator == '+':
            sum = str(int(first_number) + int(second_number))

        if operator == '-':
            sum = str(int(first_number) - int(second_number))

        length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(length)
        bottom = operator + str(second_number).rjust(length - 1)
        line = ''
        result = str(sum).rjust(length)

        for i in range(length):
            line = line + '-'

        if problem != problems[-1]:
            first = first + top + '    '
            second = second + bottom + '    '
            lines = lines + line + '    '
            sumx = sumx + result + '    '
        else:
            first = first + top
            second = second + bottom
            lines = lines + line
            sumx = sumx + result

    if evaluate:
        string = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
        string = first + '\n' + second + '\n' + lines

    return string


result_one = arithmetic_arranger(test_one, False)

result_two = arithmetic_arranger(test_two, True)

# print(result_one)
print(result_two)
