def return_10():
    return 10


def add(number_1, number_2):
    return number_1 + number_2


print(add(1, 2))


def subtract(number_1, number_2):
    return number_1 - number_2


print(subtract(10, 5))


def multiply(number_1, number_2):
    return number_1 * number_2


print(multiply(4, 2))


def divide(number_1, number_2):
    return number_1/number_2


print(divide(10, 2))


def length_of_string(string_length):
    return len(string_length)


print(length_of_string("HelloHelloHelloHelloo"))


def join_string(string_1, string_2):
    return string_1 + string_2


print(join_string("Mary had a little lamb,", " its fleece was white as snow"))


def add_string_as_number(string_1, string_2):
    string_1 = "1"
    string_2 = "2"
    return int(string_1) + int(string_2)


print(add_string_as_number("1", "2"))


def number_to_full_month_name(number_of_month):
    month = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    if number_of_month == 1:
        return "January"
    elif number_of_month == 3:
        return "March"
    elif number_of_month == 9:
        return "September"
    elif number_of_month == 4:
        return "April"
    elif number_of_month == 10:
        return "October"


print(number_to_full_month_name(1))
print(number_to_full_month_name(3))
print(number_to_full_month_name(9))


def number_to_short_month_name(number_of_month):

    return number_to_full_month_name(number_of_month)[0:3]


print(number_to_short_month_name(1))
print(number_to_short_month_name(4))
print(number_to_short_month_name(10))


def volume_of_cube(side):
    return side * side * side


print(volume_of_cube(3))


def reverse_a_string(reversed_string):
    return (reversed_string)[::-1]


print(reverse_a_string("Hello"))


def convert_to_celsius(celsius):
    return (celsius * 1.8 + 32)


print(convert_to_celsius(10))
