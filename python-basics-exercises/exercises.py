def get_largest_number(numbers):
    """Gets the largest number from the list received.

    You CANNOT use `max` built-in method.

    Examples:
        >>> print get_largest_number([4, 500, 250, 499.9, 4.1, 3.9])
        500

        >>> print get_largest_number([1, 2, 4, 4, -3, 3, 1, -1])
        4

    :param numbers: List containing corresponding numbers
    :return: Largest number found
    """
    return sorted(numbers)[-1]


def get_smallest_number(numbers):
    """Gets the smallest number from the list received.

    You CANNOT use `min` built-in method.

    Examples:
        >>> print get_smallest_number([4, 500, 250, 499.9, 4.1, 3.9])
        3.9

        >>> print get_smallest_number([1, 2, 4, 4, -3, 3, 1, -1])
        -3

    :param numbers: List containing corresponding numbers
    :return: Smallest number found
    """
    return sorted(numbers)[0]


print get_smallest_number([4, 500, 250, 499.9, 4.1, 3.9])
print get_smallest_number([1, 2, 4, 4, -3, 3, 1, -1])


def get_even_numbers(numbers):
    """Gets all even numbers from the list received.

    This function MUST NOT modify the received `numbers` list.

    Examples:
        >>> print get_even_numbers([1, 3, 3, 0, 4, 5, 17, 22, 209, 100, -2, -7, -90])
        [0, 4, 22, 100, -2, -90]

        >>> print get_even_numbers([1, 15, 27, -3, -5])
        []

    :param numbers: - List containing corresponding numbers
    :return: New list containing all even numbers found
    """
    mylist = []
    for i in numbers:
        if i % 2 == 0:
            mylist.append(i)
    return mylist


def filter_even_numbers(numbers):
    """Filters even numbers in the list received.

    This function MUST modify the received `numbers` list.

    Examples:
        >>> print filter_even_numbers([1, 3, 3, 0, 4, 5, 17, 22, 209, 100, -2, -7, -90])
        None

        >>> print get_even_numbers([1, 15, 27, -3, -5])
        None

    :param numbers: List containing corresponding numbers
    :return: Nothing
    """

    for i in numbers[:]:
        if i % 2 != 0:
            numbers.remove(i)

    return numbers

def draw_solid_rectangle(x, y):
    """Generates a string with a solid rectangle made of * symbols with `x` columns and `y` rows.

    Examples:
        >>> print draw_solid_rectangle(1, 1)
        *

        >>> print draw_solid_rectangle(2, 2)
        **
        **

        >>> print draw_solid_rectangle(3, 3)
        ***
        ***
        ***

        >>> print draw_solid_rectangle(5, 9)
        *****
        *****
        *****
        *****
        *****
        *****
        *****
        *****
        *****

        >>> print draw_solid_rectangle(9, 5)
        *********
        *********
        *********
        *********
        *********

    :param x: Number of columns (width)
    :param y: Number of rows (height)
    :return: String containing corresponding solid rectangle
    """
    cadena = ""
    for a in range(y):
        for b in range(x):
            cadena = cadena + "*"
        cadena = cadena + "\n"
    return cadena.rstrip()




def draw_rectangle_borders(x, y):
    """Generates a string with a rectangle borders made of * symbols with `x` columns and `y` rows.

    Examples:
        >>> print draw_rectangle_borders(1, 1)
        *

        >>> print draw_rectangle_borders(2, 2)
        **
        **

        >>> print draw_rectangle_borders(3, 3)
        ***
        * *
        ***

        >>> print draw_rectangle_borders(5, 9)
        *****
        *   *
        *   *
        *   *
        *   *
        *   *
        *   *
        *   *
        *****

        >>> print draw_rectangle_borders(9, 5)
        *********
        *       *
        *       *
        *       *
        *********

    :param x: Number of columns (width)
    :param y: Number of rows (height)
    :return: String containing corresponding rectangle border
    """
    cadena = ""
    for a in range(y):
        for b in range(x):
            cadena = cadena + "*" + ""
        cadena = cadena + "\n"
    return cadena.rstrip()

def draw_pyramid(height):
    """Generates a string with a pyramid made of * symbols and `height` rows.

    Examples:
        >>> print draw_pyramid(1)
        *

        >>> print draw_pyramid(2)
         *
        ***

        >>> print draw_pyramid(5)
            *
           ***
          *****
         *******
        *********

    :param height: Number of rows (height)
    :return: String containing corresponding pyramid
    """
    cad = ""
    spaces = height - 1
    asterist = 1
    for lines in range(height):
        while spaces >= 0:
            cad = cad + '{}{}'.format((' ' * spaces), ('*' * asterist)) + "\n"
            spaces -= 1
            asterist += 2
    return cad.rstrip()


def draw_inverted_pyramid(height):
    """Generates a string with a inverted pyramid made of * symbols and `height` rows.

    Examples:
        >>> print draw_pyramid(1)
        *

        >>> print draw_pyramid(2)
        ***
         *

        >>> print draw_pyramid(5)
        *********
         *******
          *****
           ***
            *

    :param height: Number of rows (height)
    :return: String containing corresponding inverted pyramid
    """
    cad = ""
    spaces = 0
    asterist = (height*2)-1
    for lines in range(height):
        while spaces <= (height - 1):
            cad = cad + '{}{}'.format((' ' * spaces), ('*' * asterist)) + "\n"
            spaces += 1
            asterist -= 2
    return cad.rstrip()


def chars_counter(string):
    """Counts number of times each char appears in a string.

    You CANNOT use `collections.Counter` class.

    Note that uppercase and lowercase are different letters (e.g. 'A' is different from 'a')

    Examples:
        >>> print chars_counter("hello world!")
        {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}

    :param string: String to count chars
    :return: Dictionary with char and counter key-value pairs
    """
    diccionario = {}

    for letra in string:
        if diccionario.has_key(letra):
            diccionario[letra] = diccionario[letra] + 1
        else:
            diccionario[letra] = 1

    return diccionario

def sort_list_ascending(elements):
    """Sorts list received in a new list with ascending order.

    You CANNOT use `sorted` built-in method.

    Examples:
        >>> print sort_list_ascending([6, 4, 3, 1, 1, 2, 0, -1, 15, 7])
        [-1, 0, 1, 1, 2, 3, 4, 6, 7, 15]

        >>> print sort_list_ascending(['b', 'Z', 'c', 'a', 'A', 'e'])
        ['A', 'Z', 'a', 'b', 'c', 'e']

    :param elements: List of elements to be sorted
    :return: New list with elements sorted
    """
    elements = [6, 4, 3, 1, 1, 2, 0, -1, 15, 7]
    for recorrido in range(1, len(elements)):
        for posicion in range(len(elements) - recorrido):
            if elements[posicion] > elements[posicion+1]:
                temp = elements[posicion]
                elements[posicion] = elements[posicion+1]
                elements[posicion+1] = temp

    return elements


def check_date(day, month, year):
    """Checks if received date is valid or not.

    You CANNOT use `datetime` nor `calendar` modules

    Be careful with leap years ;)

    Examples:
        >>> print check_date(1, 1, 1)
        True

        >>> print check_date(4, 9, 1990)
        True

        >>> print check_date(4, 9, -1)
        False

        >>> print check_date(0, 9, 1991)
        False

        >>> print check_date(30, 13, 1991)
        False

        >>> print check_date(31, 5, 1989)
        True

        >>> print check_date(31, 4, 1989)
        False

        >>> print check_date(29, 2, 2017)
        False

        >>> print check_date(29, 2, 1900)
        False

        >>> print check_date(29, 2, 2020)
        True

        >>> print check_date(29, 2, 2000)
        True

    :param day: Day number
    :param month: Month number
    :param year: Year number
    :return: True if date is valid, False otherwise
    """
    pass  # <--- remove this `pass` and put your code here


def check_palindrome(string):
    """Checks if received string is palindrome or not.

    Be careful with white spaces, special symbols, lowercase and uppercase ;)

    Examples:
        >>> print check_palindrome("y")
        True

        >>> print check_palindrome("nope")
        False

        >>> print check_palindrome("racecar")
        True

        >>> print check_palindrome("Madam")
        True

        >>> print check_palindrome("A man, a plan, a canal, Panama!")
        True

        >>> print check_palindrome("Was it a car or a cat I saw?")
        True

        >>> print check_palindrome("Was it a dog or a cat I saw?")
        False

        >>> print check_palindrome("No 'x' in Nixon")
        True

        >>> print check_palindrome("1234321")
        True

        >>> print check_palindrome("123321")
        True

        >>> print check_palindrome("123421")
        False

    :param string: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    string = string.replace(' ', '').lower().replace("!", "").replace(",", "").replace("'", "").replace("?", "")
    return string == string[::-1]



def join_strings(strings):
    """Concatenates a list of words with intervening occurrences of comma.

    You CANNOT use `str.join` method.

    Example:
        >>> print join_strings(["red", "blue", "yellow", "green"])
        red,blue,yellow,green

        >>> print join_strings(["hello", "world"])
        hello,world

        >>> print join_strings(["oops"])
        oops

    :param strings: List of strings to be concatenated
    :return: Concatenated string
    """
    suma = ""
    for i in range(len(strings)):
        suma = suma + strings[i] + ","
    return suma.rstrip(",")

if __name__ == '__main__':
    # if you need to execute custom code to check results, do it here!
    pass
